
import aiohttp
import asyncio
from tonsdk.boc import Cell as TonSdkCell
from tonsdk.provider import ToncenterClient
from tonsdk.utils import Address as TonSdkAddress
from tonsdk.contract.wallet import WalletVersionEnum, Wallets


JACKPOT_CONTRACT_ADDRESS: str = "EQDeyCNNa8GMjpc6ZWl4rxuG-HFeBLDGdSw-nUrI2IMndZ8L"
TON_CENTER_API_KEY: str = "cc90579e5a9bb6dac7ae2c95616a682e43fee8e217a7c2575435492075b6281c"
WALLET_MNEMONIC: str = ['cushion', 'unaware', 'dune', 'garbage', 'soap', 'recipe', 'manual', 'garment', 'sorry', 'mass', 'raccoon', 'punch', 'pony', 'rifle', 'amazing', 'grant', 'panda', 'casino', 'indoor', 'suspect', 'alien', 'orient', 'thought', 'vault']

async def async_init():
    try:
        _, _, _, wallet = Wallets.from_mnemonics(WALLET_MNEMONIC, WalletVersionEnum.v4r2, 0)
        return wallet
    except Exception as error:
         print(error)

def get_wallet_addred(wallet):
    return wallet.address.to_string(True, True, True)

async def execute(to_run: dict, single_query=True):
    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        if single_query:
            to_run = [to_run]
        tasks = []
        for task in to_run:
            tasks.append(task["func"](session, *task["args"], **task["kwargs"]))

        return await asyncio.gather(*tasks, return_exceptions=True)
        
async def get_wallet_balance(wallet, client):
    adr_state_result_task = client.raw_get_account_state(wallet.address.to_string())
    adr_state_result = await execute(to_run=adr_state_result_task)
    return adr_state_result[0].get('balance')


async def get_wallet_seqno(wallet, client):
    cur_adr_seq_no_task = client.raw_run_method(wallet.address.to_string(), 'seqno', [])
    cur_adr_seq_result = await execute(to_run=cur_adr_seq_no_task)
    cur_seq_no = int(cur_adr_seq_result[0].get('stack')[0][1], 16)
    return cur_seq_no

async def send_payload_to_adr(wallet, client, current_seqno: int, payload: TonSdkCell, address: str, forward_ton_amont: int = 0):
    transfer_query = wallet.create_transfer_message(
        to_addr=TonSdkAddress(address).to_string(),
        seqno=current_seqno,
        amount=(int(10**9) * forward_ton_amont),
        payload=payload
    )
    transfer_boc = transfer_query['message'].to_boc(False)
    transfer_task = client.raw_send_message(transfer_boc)
    transfer_result = await execute(to_run=transfer_task)

    print(f"[CURRENT SEQNO] --> {current_seqno}, [WAITING FOR {current_seqno + 1} SEQNO]")
    while await get_wallet_seqno(wallet=wallet, client=client) == current_seqno:
        await asyncio.sleep(1)

    print(f"[TRANSACTION CONFIRMED]\n[TRANSFER RESULT] --> {transfer_result}")

async def do():
    client_tc = ToncenterClient(base_url="https://toncenter.com/api/v2/", api_key=TON_CENTER_API_KEY)
    wallet_tc = await async_init()

    # wallet_address = get_wallet_addred(wallet=wallet_tc)
    # wallet_seqno = await get_wallet_seqno(wallet=wallet_tc, client=client_tc)
    # wallet_balance = await get_wallet_balance(wallet=wallet_tc, client=client_tc)

    tonsdk_coin_flip_cell: TonSdkCell = TonSdkCell()
    tonsdk_coin_flip_cell.bits.write_uint(777, 32) # CoinFlip operation code

    tons_amount: int = 1

    for iteration in range(1, 101):
        print(f"[iteration: {iteration}/100]---------------------------------------------------------------------")
        print("[TONS AMOUNT] --> ", tons_amount)

        wallet_balance_before = await get_wallet_balance(wallet=wallet_tc, client=client_tc)
        wallet_balance_before = int(wallet_balance_before)
        print(f"[WALLET BALANCE BEFORE] --> {wallet_balance_before / 1e9} TON")

        if ((wallet_balance_before / 1e9) < 1):
            print("Nice try! =(")
            break

        current_seqno = await get_wallet_seqno(wallet=wallet_tc, client=client_tc)
        await send_payload_to_adr(wallet=wallet_tc, client=client_tc, current_seqno=current_seqno, payload=tonsdk_coin_flip_cell, address=JACKPOT_CONTRACT_ADDRESS, forward_ton_amont=tons_amount)

        print("Transaction confirmed! Wait 60 secs")
        await asyncio.sleep(60)

        wallet_balance_after = await get_wallet_balance(wallet=wallet_tc, client=client_tc)
        wallet_balance_after = int(wallet_balance_after)
        print(f"[WALLET BALANCE AFTER] --> {wallet_balance_after / 1e9} TON")

        if (wallet_balance_after > wallet_balance_before):
            print(f"You've won {(wallet_balance_after - wallet_balance_before) / 1e9} TON, reducing the bid to 1 TON\n")
            tons_amount = 1
        else:
            print(f"You have lost {tons_amount} TON, we increase the bet by 2 times!\n")
            tons_amount *= 2

if __name__ == "__main__":
    asyncio.run(do())

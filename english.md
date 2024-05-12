# Intelligence, investment, or the ability to invest?

<img src="https://github.com/taiga-labs/jackpot-cracking/assets/105946529/f666ff90-f2e1-4365-846a-2b2a69661909" width="200" height="200">

## Casino Smart Contract

In search of new opportunities to increase capital, the Taiga Labs team came across an interesting smart contract. This contract, which is part of a series of different contacts from the casino project on TON, provides an opportunity to double the coins sent with a 50% probability. The effectiveness of such investments depends on the right strategy and mathematical calculations.

Therefore, the necessary logic is executed every year
![image-1](https://i.ibb.co/kDkRwTf/image.png)

The rand() function has not been rewritten, an assembler primitive is used, so everything is clean
![image0](https://i.ibb.co/CV0RTwf/image.png)

## Our tactics

Let's say you start with an initial bet of 1 TON. If your bet loses, you double the bet to 2 TON coins on the next round. If you lose again, your next bet will be 4 TON coins, and so on. Once you win, you return to the initial bet of 1 TON coin.

### Mathematical calculation/example:

1. The starting bid: 1 coin. Loss.
2. The bid: 2 coins. Loss. Total spent: 3 coins.
3. Bet: 4 coins. Loss. Total spent: 7 coins.
4. The bid: 8 coins. A win. Total spent: 15 coins.

The winnings amount to 16 coins (since the bet of 8 coins doubles when winning), of which 15 coins are funds spent on bets, and 1 coin is net income.

### Visualization on the chart
#### The probability of losing N times = 1/(2^N) X 100%

on the X scale - the number of bets in a row
on the Y scale - the probability of losing as a percentage

In this photo, the arrow shows the probability of losing with a single bet, as expected, it is 50%
![image1](https://i.ibb.co/rH2FF6b/image.png)

And this photo with a larger scale, the probability of losing decreases exponentially. The probability of losing 7 times is less than 0.5% (with the 7th bet, you would have sent 128 TON to the contract)
![image2](https://i.ibb.co/vLKCxmt/image.png)

### Why is that?

A series of losses are joint events, so the probabilities multiply.
Therefore, the probability that we will lose 5 times is 100 X (0.5 X 0.5 X 0.5 X 0.5 X 0.5) = 3.125 %

## This strategy is called the "Martingale Strategy"

The Martingale strategy is a popular betting system based on doubling the bet after each loss. The essence of the strategy is that when the player wins for the first time, he returns all previous losses and goes into the plus for the initial bet.

The use of the Martingale strategy, especially in 50/50 games such as betting on a coin toss, theoretically allows you to win in the long run, compensating for all previous losses with one winning round.
This strategy is a reliable way to achieve permanent winnings, provided that there is sufficient capital to cover losing streaks and the ability to control emotions and maintain betting discipline.

## Demonstration of the 70 TON -> 100 TON strategy

In just 50 iterations, we managed to earn a net 30 TON, you can find the full list of logs below. Although the initial balance was 65, the logs are shown from 70, he managed to earn 35 TON.

![image3](https://i.ibb.co/ZNQHFYq/image.png)
![image4](https://i.ibb.co/GQDKc4B/image.png)

## Interesting points

It was like a series of victories,
![image5](https://i.ibb.co/qkc6nJb/image.png)

so the moments are more dangerous...
![image6](https://i.ibb.co/T18xH6j/image.png)

It is important to understand that the more money on the balance sheet, the higher the probability of not losing your investments, that is, the more likely it is to get out of a series of failures.

Thank you for your attention, 
Taiga Labs

## Logs

[iteration: 1/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 70.162249905 TON
[CURRENT SEQNO] --> 306, [WAITING FOR 307 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349194.888914:8:0.7724156989782643'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 71.159111092 TON
You've won 0.996861187 TON, reducing the bid to 1 TON

[iteration: 2/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 71.159111092 TON
[CURRENT SEQNO] --> 307, [WAITING FOR 308 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349228.349967:8:0.2972076074514326'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 72.155972283 TON
You've won 0.996861191 TON, reducing the bid to 1 TON

[iteration: 3/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 72.155972283 TON
[CURRENT SEQNO] --> 308, [WAITING FOR 309 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349261.9241388:9:0.43052188216521103'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 71.153629873 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 4/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 71.153629873 TON
[CURRENT SEQNO] --> 309, [WAITING FOR 310 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349301.0098438:2:0.4799523796802756'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 73.150491065 TON
You've won 1.996861192 TON, reducing the bid to 1 TON

[iteration: 5/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 73.150491065 TON
[CURRENT SEQNO] --> 310, [WAITING FOR 311 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349329.178351:9:0.9235295037304437'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 72.148148657 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 6/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 72.148148657 TON
[CURRENT SEQNO] --> 311, [WAITING FOR 312 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349357.0669675:3:0.8402529279606545'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 74.145009844 TON
You've won 1.996861187 TON, reducing the bid to 1 TON

[iteration: 7/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 74.145009844 TON
[CURRENT SEQNO] --> 312, [WAITING FOR 313 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349407.5872517:0:0.5183978269506466'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 75.141871025 TON
You've won 0.996861181 TON, reducing the bid to 1 TON

[iteration: 8/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 75.141871025 TON
[CURRENT SEQNO] --> 313, [WAITING FOR 314 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349479.9492142:9:0.8234654907653771'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 74.139528615 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 9/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 74.139528615 TON
[CURRENT SEQNO] --> 314, [WAITING FOR 315 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349513.5199227:5:0.6978717670674072'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 72.137186205 TON
You have lost 2 TON, we increase the bet by 2 times!

[iteration: 10/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  4
[WALLET BALANCE BEFORE] --> 72.137186205 TON
[CURRENT SEQNO] --> 315, [WAITING FOR 316 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349548.7106173:0:0.7441283281886585'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 76.133882595 TON
You've won 3.99669639 TON, reducing the bid to 1 TON

[iteration: 11/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 76.133882595 TON
[CURRENT SEQNO] --> 316, [WAITING FOR 317 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349582.8981323:8:0.17106454522324865'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 75.131540182 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 12/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 75.131540182 TON
[CURRENT SEQNO] --> 317, [WAITING FOR 318 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349632.5812595:8:0.09508677172744417'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 77.128401374 TON
You've won 1.996861192 TON, reducing the bid to 1 TON

[iteration: 13/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 77.128401374 TON
[CURRENT SEQNO] --> 318, [WAITING FOR 319 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349671.2641022:3:0.5958275020826529'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 76.126058959 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 14/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 76.126058959 TON
[CURRENT SEQNO] --> 319, [WAITING FOR 320 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349727.595957:3:0.4766334012852296'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 74.123716547 TON
You have lost 2 TON, we increase the bet by 2 times!

[iteration: 15/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  4
[WALLET BALANCE BEFORE] --> 74.123716547 TON
[CURRENT SEQNO] --> 320, [WAITING FOR 321 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349766.3618417:8:0.7130383472705604'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 70.121374134 TON
You have lost 4 TON, we increase the bet by 2 times!

[iteration: 16/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  8
[WALLET BALANCE BEFORE] --> 70.121374134 TON
[CURRENT SEQNO] --> 321, [WAITING FOR 322 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349816.27617:5:0.6671015478488255'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 78.118067323 TON
You've won 7.996693189 TON, reducing the bid to 1 TON

[iteration: 17/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 78.118067323 TON
[CURRENT SEQNO] --> 322, [WAITING FOR 323 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349854.9105554:9:0.27505894469179715'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 79.114928512 TON
You've won 0.996861189 TON, reducing the bid to 1 TON

[iteration: 18/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 79.114928512 TON
[CURRENT SEQNO] --> 323, [WAITING FOR 324 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349887.800706:10:0.9969819147642807'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 80.111789696 TON
You've won 0.996861184 TON, reducing the bid to 1 TON

[iteration: 19/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 80.111789696 TON
[CURRENT SEQNO] --> 324, [WAITING FOR 325 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349952.9668214:10:0.5195848092835512'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 81.108650887 TON
You've won 0.996861191 TON, reducing the bid to 1 TON

[iteration: 20/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 81.108650887 TON
[CURRENT SEQNO] --> 325, [WAITING FOR 326 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715349986.620605:7:0.48476606679828604'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 80.106308468 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 21/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 80.106308468 TON
[CURRENT SEQNO] --> 326, [WAITING FOR 327 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350057.5670922:11:0.9780841324083496'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 82.103169654 TON
You've won 1.996861186 TON, reducing the bid to 1 TON

[iteration: 22/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 82.103169654 TON
[CURRENT SEQNO] --> 327, [WAITING FOR 328 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350112.5126317:9:0.1655097664832461'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 83.100030842 TON
You've won 0.996861188 TON, reducing the bid to 1 TON

[iteration: 23/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 83.100030842 TON
[CURRENT SEQNO] --> 328, [WAITING FOR 329 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350152.2208285:9:0.8946161018390824'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 84.096892034 TON
You've won 0.996861192 TON, reducing the bid to 1 TON

[iteration: 24/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 84.096892034 TON
[CURRENT SEQNO] --> 329, [WAITING FOR 330 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350185.2111957:2:0.88123572291788'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 83.094549623 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 25/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 83.094549623 TON
[CURRENT SEQNO] --> 330, [WAITING FOR 331 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350223.7884166:5:0.7353123953968892'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 81.092207215 TON
You have lost 2 TON, we increase the bet by 2 times!

[iteration: 26/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  4
[WALLET BALANCE BEFORE] --> 81.092207215 TON
[CURRENT SEQNO] --> 331, [WAITING FOR 332 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350256.843055:4:0.0012013951825859959'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 85.088903602 TON
You've won 3.996696387 TON, reducing the bid to 1 TON

[iteration: 27/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 85.088903602 TON
[CURRENT SEQNO] --> 332, [WAITING FOR 333 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350306.2991953:3:0.07493973557200728'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 86.085764786 TON
You've won 0.996861184 TON, reducing the bid to 1 TON

[iteration: 28/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 86.085764786 TON
[CURRENT SEQNO] --> 333, [WAITING FOR 334 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350366.5805464:10:0.7202586880837496'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 87.082625977 TON
You've won 0.996861191 TON, reducing the bid to 1 TON

[iteration: 29/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 87.082625977 TON
[CURRENT SEQNO] --> 334, [WAITING FOR 335 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350399.6556845:10:0.7188047563537376'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 86.080283567 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 30/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 86.080283567 TON
[CURRENT SEQNO] --> 335, [WAITING FOR 336 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350438.1256244:10:0.7190863490174059'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 84.077941159 TON
You have lost 2 TON, we increase the bet by 2 times!

[iteration: 31/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  4
[WALLET BALANCE BEFORE] --> 84.077941159 TON
[CURRENT SEQNO] --> 336, [WAITING FOR 337 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350465.7262273:4:0.19610691150162118'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 88.074637548 TON
You've won 3.996696389 TON, reducing the bid to 1 TON

[iteration: 32/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 88.074637548 TON
[CURRENT SEQNO] --> 337, [WAITING FOR 338 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350509.745301:7:0.18873621398927598'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 87.072295137 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 33/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 87.072295137 TON
[CURRENT SEQNO] --> 338, [WAITING FOR 339 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350564.112318:2:0.2999840930669475'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 89.069156321 TON
You've won 1.996861184 TON, reducing the bid to 1 TON

[iteration: 34/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 89.069156321 TON
[CURRENT SEQNO] --> 339, [WAITING FOR 340 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350613.7886214:11:0.4978230524592132'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 90.066017512 TON
You've won 0.996861191 TON, reducing the bid to 1 TON

[iteration: 35/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 90.066017512 TON
[CURRENT SEQNO] --> 340, [WAITING FOR 341 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350647.206827:3:0.5664878870079246'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 89.0636751 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 36/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 89.0636751 TON
[CURRENT SEQNO] --> 341, [WAITING FOR 342 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350690.6367106:9:0.030753901659993033'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 91.060536286 TON
You've won 1.996861186 TON, reducing the bid to 1 TON

[iteration: 37/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 91.060536286 TON
[CURRENT SEQNO] --> 342, [WAITING FOR 343 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350740.2640276:3:0.6968222842723714'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 92.057397477 TON
You've won 0.996861191 TON, reducing the bid to 1 TON

[iteration: 38/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 92.057397477 TON
[CURRENT SEQNO] --> 343, [WAITING FOR 344 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350779.0317776:10:0.5996512454202966'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 91.055055069 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 39/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 91.055055069 TON
[CURRENT SEQNO] --> 344, [WAITING FOR 345 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350817.9424164:10:0.6457903768367005'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 93.051916248 TON
You've won 1.996861179 TON, reducing the bid to 1 TON

[iteration: 40/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 93.051916248 TON
[CURRENT SEQNO] --> 345, [WAITING FOR 346 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350883.9992824:9:0.028530374048176044'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 94.048777434 TON
You've won 0.996861186 TON, reducing the bid to 1 TON

[iteration: 41/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 94.048777434 TON
[CURRENT SEQNO] --> 346, [WAITING FOR 347 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350939.0958292:9:0.49505018305406734'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 95.045638621 TON
You've won 0.996861187 TON, reducing the bid to 1 TON

[iteration: 42/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 95.045638621 TON
[CURRENT SEQNO] --> 347, [WAITING FOR 348 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715350983.8411863:3:0.5385656654241076'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 94.043296204 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 43/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 94.043296204 TON
[CURRENT SEQNO] --> 348, [WAITING FOR 349 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715351054.648612:5:0.24368212696860714'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 96.040157392 TON
You've won 1.996861188 TON, reducing the bid to 1 TON

[iteration: 44/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 96.040157392 TON
[CURRENT SEQNO] --> 349, [WAITING FOR 350 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715351093.6209161:11:0.07112917934470542'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 95.037814982 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 45/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 95.037814982 TON
[CURRENT SEQNO] --> 350, [WAITING FOR 351 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715351137.9498284:7:0.21707012367641076'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 97.034676171 TON
You've won 1.996861189 TON, reducing the bid to 1 TON

[iteration: 46/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 97.034676171 TON
[CURRENT SEQNO] --> 351, [WAITING FOR 352 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715351182.4806652:10:0.6502297450361036'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 96.03233376 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 47/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 96.03233376 TON
[CURRENT SEQNO] --> 352, [WAITING FOR 353 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715351215.6470141:5:0.37018149318480764'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 98.029194947 TON
You've won 1.996861187 TON, reducing the bid to 1 TON

[iteration: 48/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 98.029194947 TON
[CURRENT SEQNO] --> 353, [WAITING FOR 354 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715351270.5421655:0:0.02095182964766873'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 99.026056135 TON
You've won 0.996861188 TON, reducing the bid to 1 TON

[iteration: 49/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  1
[WALLET BALANCE BEFORE] --> 99.026056135 TON
[CURRENT SEQNO] --> 354, [WAITING FOR 355 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715351309.2462118:3:0.9454950134490546'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 98.023713723 TON
You have lost 1 TON, we increase the bet by 2 times!

[iteration: 50/100]---------------------------------------------------------------------
[TONS AMOUNT] -->  2
[WALLET BALANCE BEFORE] --> 98.023713723 TON
[CURRENT SEQNO] --> 355, [WAITING FOR 356 SEQNO]
[TRANSACTION CONFIRMED]
[TRANSFER RESULT] --> [{'@type': 'ok', '@extra': '1715351358.441982:5:0.5713955891403768'}]
Transaction confirmed! Wait 10 secs
[WALLET BALANCE AFTER] --> 100.020574906 TON
You've won 1.996861183 TON, reducing the bid to 1 TON

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

<img src="![image](https://github.com/taiga-labs/jackpot-cracking/assets/105946529/27e0d2d7-bdbb-4cf0-b90c-01e98b7dd057)" width="200" height="200">

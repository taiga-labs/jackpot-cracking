# Ум, инвестиции, или умение инвестировать?


## Смарт-контракт

В поисках новых возможностей для увеличения капитала, команда Taiga Labsстолкнулась с интересным смарт-контрактом. Данный контракт, входящий в серию разных контактов от проекта казино на TON, предоставляет возможность удвоить отправленные монеты с вероятностью 50%. Эффективность таких инвестиций зависит от правильной стратегии и математических расчетов.

По этому оп-коду исполняется нужная логика
![image-1](https://i.ibb.co/kDkRwTf/image.png)

Функция rand() не переписана, используется ассемблерный примитив, поэтому всё чисто
![image0](https://i.ibb.co/CV0RTwf/image.png)

## Наша такика

Предположим, вы начинаете с первоначальной ставки в размере 1 TON. Если ваша ставка проигрывает, вы удваиваете ставку до 2 монет TON на следующем раунде. Если проиграете снова, ваша следующая ставка будет уже 4 монеты TON, и так далее. Как только вы выигрываете, вы возвращаетесь к начальной ставке в 1 монету TON.

#### Математическая выкладка/пример:

1. Стартовая ставка: 1 монета. Потеря.
2. Ставка: 2 монеты. Потеря. Суммарно потрачено: 3 монеты.
3. Ставка: 4 монеты. Потеря. Суммарно потрачено: 7 монет.
4. Ставка: 8 монет. Выигрыш. Суммарно потрачено: 15 монет.

Выигрыш составляет 16 монет (поскольку ставка в 8 монет удваивается при выигрыше), из которых 15 монет — это потраченные на ставки средства, и 1 монета — чистый доход.

### Визуализация
##### Вероятность проиграть N раз = 1/(2^N) X 100%

#### На графике:

по шкале Х - количество ставок подряд 
по шкале Y - вероятность проигрыша в процентах

На этой фотографии стрелкой показана вероятность проигрыша при единичной ставке, как и ожидалось, она составляет 50%
![image1](https://i.ibb.co/rH2FF6b/image.png)

А эта фотография с более большим масштабом, вероятность проиграть понижается экспоненциально. Вероятность проиграть 7 раз меньше, чем 0.5% (при 7-ой ставке вы бы отправили на контракт 128 TON)
![image2](https://i.ibb.co/Gv8q4Qb/image.png)

##### Почему так? 

Череда проигрышей - это совместные события, поэтому вероятности перемножаются.
Поэтому, вероятность того, что мы проиграем 5 раз - это 100 Х (0.5 Х 0.5 Х 0.5 Х 0.5 Х 0.5) = 3.125 %

## Данная стратегия называется "Стратегией Мартингейла"

Стратегия Мартингейла — это популярная беттинговая система, основанная на удвоении ставки после каждого проигрыша. Суть стратегии заключается в том, что при первом выигрыше игрок возвращает все предыдущие потери и выходит в плюс на изначальную ставку.

Применение стратегии Мартингейла, особенно в играх с возможностью 50/50, таких как ставка на бросок монеты, теоретически позволяет в долгосрочной перспективе оставаться в выигрыше, компенсируя все предыдущие потери одним выигрышным раундом.
Эта стратегия является надежным способом достижения постоянных выигрышей, при условии наличия достаточного капитала для покрытия проигрышных серий и умения контролировать эмоции и соблюдать дисциплину ставок.

## Демонстрация стратегии 70 TON -> 100 TON

Всего за 50 итераций удалось заработать чистыми 30 TON, полный список логов вы можете найти ниже. Хоть и изначальный баланс был 65, логи показаны с 70, того удалось заработать 35 TON.

![image3](https://i.ibb.co/ZNQHFYq/image.png)
![image4](https://i.ibb.co/GQDKc4B/image.png)

## Интересные моменты

Были как череды побед,
![image5](https://i.ibb.co/qkc6nJb/image.png)

так и моменты опаснее...
![image6](https://i.ibb.co/T18xH6j/image.png)

## Логи

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

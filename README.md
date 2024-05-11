# Ум, инвестиции, или умение инвестировать?

<img src="https://github.com/taiga-labs/jackpot-cracking/assets/105946529/f666ff90-f2e1-4365-846a-2b2a69661909" width="200" height="200">

## Смарт-контракт казино

В поисках новых возможностей для увеличения капитала, команда Taiga Labs столкнулась с интересным смарт-контрактом. Данный контракт, входящий в серию разных контактов от проекта казино на TON, предоставляет возможность удвоить отправленные монеты с вероятностью 50%. Эффективность таких инвестиций зависит от правильной стратегии и математических расчетов.

По этому оп-коду исполняется нужная логика
![image-1](https://i.ibb.co/kDkRwTf/image.png)

Функция rand() не переписана, используется ассемблерный примитив, поэтому всё чисто
![image0](https://i.ibb.co/CV0RTwf/image.png)

## Наша такика

Предположим, вы начинаете с первоначальной ставки в размере 1 TON. Если ваша ставка проигрывает, вы удваиваете ставку до 2 монет TON на следующем раунде. Если проиграете снова, ваша следующая ставка будет уже 4 монеты TON, и так далее. Как только вы выигрываете, вы возвращаетесь к начальной ставке в 1 монету TON.

### Математическая выкладка/пример:

1. Стартовая ставка: 1 монета. Потеря.
2. Ставка: 2 монеты. Потеря. Суммарно потрачено: 3 монеты.
3. Ставка: 4 монеты. Потеря. Суммарно потрачено: 7 монет.
4. Ставка: 8 монет. Выигрыш. Суммарно потрачено: 15 монет.

Выигрыш составляет 16 монет (поскольку ставка в 8 монет удваивается при выигрыше), из которых 15 монет — это потраченные на ставки средства, и 1 монета — чистый доход.

### Визуализация на графике
#### Вероятность проиграть N раз = 1/(2^N) X 100%

по шкале Х - количество ставок подряд 
по шкале Y - вероятность проигрыша в процентах

На этой фотографии стрелкой показана вероятность проигрыша при единичной ставке, как и ожидалось, она составляет 50%
![image1](https://i.ibb.co/rH2FF6b/image.png)

А эта фотография с более большим масштабом, вероятность проиграть понижается экспоненциально. Вероятность проиграть 7 раз меньше, чем 0.5% (при 7-ой ставке вы бы отправили на контракт 128 TON)
![image2](https://i.ibb.co/Gv8q4Qb/image.png)

### Почему так? 

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

Важно понимать, что чем больше денег на балансе, тем выше вероятность не потерять свои вложения, то есть тем больше вероятность выбраться из серии неудач.

Спасибо за вниание,
Taiga Labs

## Логи

<img src="![image](https://github.com/taiga-labs/jackpot-cracking/assets/105946529/27e0d2d7-bdbb-4cf0-b90c-01e98b7dd057)" width="200" height="200">


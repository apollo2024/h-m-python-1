#  Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#  Сколько журавликов сделал каждый ребенок, если известно,
#  что Петя и Сережа сделали одинаковое количество журавликов,
#  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

from random import randrange

s = randrange(6, 1002, 3)
if s % 2 == 0:
    pety = s // 6
    sergey = pety
    katy = (pety + sergey) * 2
    print(f'всего сделано {s}')
    print(f'петя сделал {pety}, сергей сделал {sergey}, катя сделала {katy}')

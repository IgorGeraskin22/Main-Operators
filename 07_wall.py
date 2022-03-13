# -*- coding: utf-8 -*-

# (цикл for)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

#  здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич
# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)

BRICK_SIZE = sd.get_point(100, 50)
right_top_brick = sd.get_point(100, 50)
left_bottom_brick = sd.get_point(0, 0)
i = 0
for y in range(0, sd.resolution[1], BRICK_SIZE.y):
    i += 1
    if i % 2 == 0:  # Определяем при каждом цикле переменная i четная или не четная.
        # Если в остатке целое число то четное,если нет то не четное.
        left_bottom_brick.x = 50
        right_top_brick.x = 150

    else:
        right_top_brick.x = 100
        left_bottom_brick.x = 0

    for x in range(0, sd.resolution[0], BRICK_SIZE.x):
        sd.rectangle(left_bottom=left_bottom_brick, right_top=right_top_brick, color=sd.COLOR_RED, width=4)
        right_top_brick.x += 100
    right_top_brick.y += 50
    left_bottom_brick.y += 50

sd.pause()

# зачет!

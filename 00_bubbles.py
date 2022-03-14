# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)
#
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
for x in range(50, 65, 5):
    sd.circle(center_position=sd.get_point(600, 300), radius=x, width=2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point, step, radius):
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=sd.COLOR_RED, width=2)


bubble(point=sd.get_point(300, 300), step=10, radius=50)

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    bubble(point=sd.get_point(x, 100), step=5, radius=50)

# Нарисовать три ряда по 10 пузырьков
# Здесь используется вложенный цикл
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        bubble(point=sd.get_point(x, y), step=5, radius=50)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    bubble(point=sd.random_point(), step=5, radius=50)

sd.pause()

# зачет!

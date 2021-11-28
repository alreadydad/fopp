### Импортируем черепашью графику
import turtle
turtle.colormode(255)

### Получаем данные от пользователя
sides =int(input('Введите количество сторон в правильном многоугольнике:'))
lenght = float(input('Введите длину стороны:'))
color = input('Введите цвет линий словом или в RGB формате (через запятую-пробел):')
fill = input('Введите цвет заливки:')

### Считаем кол-во "слов" в заданных пользователем цветах
color_count = len(color.split(','))
fill_count = len(fill.split(','))

### Если цвет задан несколькими словами (RGB), конвертируем цвет в кортеж
if color_count > 1:
    color = tuple(map(int, color.split(', ')))

if fill_count > 1:
    fill = tuple(map(int, fill.split(', ')))

### Импортируем экран
wn = turtle.Screen()

### Присваиваем цвет черепашке и заливке исходя из полученных данных
turtle.pencolor(color)
#turtle.pensize(2)
turtle.fillcolor(fill)

### Рассчитываем угол правильного многоугольника исходя из кол-ва сторон
angle = 360/sides

### Инициализируем заливку фигуры
turtle.begin_fill()

### Цикл отображения фигуры
for _ in range(sides):
    turtle.forward(lenght)
    turtle.left(angle)

### Выключаем заливку
turtle.end_fill()

### Закрытие программы по нажатию
wn.exitonclick()
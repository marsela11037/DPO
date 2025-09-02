import turtle
import random
import time

#глобальные переменные (не принятая практика с точки зрения организации функций)
sc = None
t1 = None # объект библиотеки Turtle (черепашка) красного цвета 
t2 = None # объект библиотеки Turtle (черепашка) красного цвета
win = False

# функция 
def setup():
    global sc, t1, t2
    sc = turtle.Screen()
    sc.setup(500,500)
    t1 = turtle.Turle()
    t2 = turtle.Turle()
    t1.color('ped')
    t2.color('green')
    t1.shape('turtle')
    t2.shape('turtle')
    t1.penup()
    t2.penup()
    t1.goto(-150,50)
    t2.goto(-150,-50)
    
    #функция для запуска игры 
    def start_race():
        global win
        for i in range(100):
            t1.forward(random.randint(1,5))
            t2.forward(random.randint(1,5))





#функция для определения победителя 
def check_winner():
    global win 
    if t1.xcor() > 150:
        print('победила красная черепашка')
        win = True
    if t2.xcor() > 150:
        print('победила зеленая черепашка')
        win = True

#код запуска
setup()
start_race()


'''проблемаика данного кода:
1. использлование глобальных переменных в функциях.
2. смешение логики и представления (логика настроек программы 
и логика гонки еаходятся в одном месте). 
3. отсуствие структуры (весь алгоритм написан в фунциях, а не класах).

4. код невозможно переиспользовать, поскольку он не представляет собой модуль'''


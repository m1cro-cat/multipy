from random import *
from time import *
from turtle import *
import base64
import pelmen_fun
print("Привет! Это Project PelmenBot! Мои функции: \n1-посмотреть старые функции \n2-тест \n3- игра угадай число \n4-о чатботе \n5-что нового? \n6-погода \n7-секудомер \n8-таймер обратного отсчета \n9-генератор цифр \n10-шифратор паролей в base64 \n11-проверка длинны пароля \n12-игра КНБ \n13-бросить кубик \n14-Генератор фигур\nВыбирай цифру!")
ipt = int(input("Что вы хотите сделать?(введите 0 для выхода):"))
while ipt != 0:
    if ipt == 1:
        ipt2 = int(input("У нас есть: 1 - старый заказ еды. 2 - старая погода. Выбирай!"))
        if ipt2 == 1:
            pelmen_fun.eda()
        elif ipt2 == 2:
            pelmen_fun.pogod()
    elif ipt == 3:
        print("Угадайте число от 1 до 100!")
        count = randint(1,100)
        price = int(input("Введите число: "))
        while price != count:
            if price > 101:
                print("Сказали же, ДО 100 xD")
            elif price > count:
                print("Число меньше!")
            elif price < count:
                print("Число больше!")
            else:
                break
            price = int(input("Введите число: "))
        if price == count:
                print("Вы угадали!")
        if price != count:
            print("Повезет в другой раз!")
    elif ipt == 4:
        print("Программа projectpb(Пельмень). Версия 2.0.0 от 29.07.23. Все права съедены шлепой. Некоторые пункты взяты из интернета, я не писал их сам.")
    elif ipt == 5:
        pelmen_fun.info()
    elif ipt == 6:
        city = input("Введите название города: ")
        weather = pelmen_fun.get_weather(city)
        print(weather)
    elif ipt == 7:
        sec_start = int(input("1 - запустить таймер, 0 - выйти"))
        if sec_start == 1:
            start = time()
            sec_end = int(input("0 - стоп"))
            end = time()
            total_time = (end - start)
            print("Время -",round(total_time, 3))
    elif ipt == 8:
        timer1 = int(input("Таймер обратного отсчета. Введите секунды."))
        for i in range(timer1, -1, -1):
            print(i)
            sleep(1)
    elif ipt == 9:
        passw = "0"
        gen_ipt = int(input("Введите длинну пароля:"))
        for i in range(gen_ipt):
            passw += str(randint(0,9))
        print("Ваш пароль:", passw)
    elif ipt == 10:
        q = input("Введите пароль: ")
        b = q.encode("UTF-8")
        e = base64.b64encode(b)
        s1 = e.decode("UTF-8")
        print(s1)
    elif ipt == 11:
        per3 = input("Введите пароль: ")
        print("Длинна пароля:", len(per3))
    elif ipt == 12:
            pelmen_fun.knb() 
    elif ipt == 13:
        print("Вам выпало", randint(1,6))
    elif ipt == 14:
        def fun1():
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color2 = (r, g, b)
            for i in range(20):
                color(color1)
                forward(100)
                left(120)
                left(10)
                color(color2)
                forward(100)
                left(120)
                left(10)  
        def fun2(color1):
            # задаю цвет
            colormode(255)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color1 = (r, g, b)
            pencolor(color1)
            #скорость
            speed(10)
            # генерация 
            pensize(randint(4, 10))
            ran3 = randint(10, 200)
            ran2 = randint(1,11)
            # рандомные координаты
            penup()
            goto(randint(-200, 200), randint(-200, 200))
            pendown()
            if ran2 == 1:
                #круг 1
                circle(ran3)
            if ran2 == 2:
                # круг с заливкой 1
                begin_fill()
                circle(ran3)
                end_fill()
            if ran2 == 3:
                # звезда
                begin_fill()
                for i in range(5):
                    forward(150)
                    left(144)
                end_fill()
            if ran2 == 4:
                # поворот на 90
                left(90)
            if ran2 == 5:
                # квадрат
                for i in range(4):
                    forward(100)
                    left(90)
            if ran2 == 6:
                # круг 2
                circle(ran3)
            if ran2 == 7:
                # треугольник
                for i in range(3):
                    forward(ran3)
                    left(120)
            if ran2 == 8:
                # спираль
                per11 = 0
                for i in range(randint(10, 36)):
                    forward(per11)  
                    per11 += 5
                    left(90) 
            if ran2 == 9:
                # круг с заливкой 2 
                begin_fill()
                circle(ran3)
                end_fill()
            if ran2 == 10:
                # какая то фигня
                fun1()
            if ran2 == 11:
                left(randint(0,360))
                for i in range(2):
                    left(45)
                    forward(100)
                    left(135)
                    forward(100)
        while True:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color1 = (r, g, b)
            fun2(color1)
    elif ipt == "?":
        print("Мои функции: \n1-посмотреть старые функции \n2-пусто \n3- игра угадай число \n4-о чатботе \n5-что нового? \n6-погода \n7-секудомер \n8-таймер обратного отсчета \n9-генератор цифр \n10-шифратор паролей в base64 \n11-проверка длинны пароля \n12-игра КНБ \n13-бросить кубик \n14-Генератор картинок(сам по себе)\nВыбирай цифру!")
    elif ipt == 2:
        print("пока тут пусто")
    else: 
        print("Прости, я тебя не понял:(")
    ipt = int(input("Что вы хотите сделать?(введите 0 для выхода):"))
print("Пока ;)")
from random import *
from time import *
from turtle import *
import os
import base64
import requests
import shutil
import main_fun
import main_beta
current_version = "3.0.4.1" 
def update_program():
        url = 'https://github.com/devcat86/multipy/archive/master.zip'
        update_zip = os.path.join('cache', 'update.zip')
        response = requests.get(url)
        with open(update_zip, 'wb') as f:
            f.write(response.content)
        shutil.unpack_archive(update_zip, 'update')
        os.remove(update_zip)
        src_dir = os.path.join('update', '<repo>-master')
        dest_dir = os.path.dirname(os.path.abspath(__file__))
        for src_name in os.listdir(src_dir):
            src_path = os.path.join(src_dir, src_name)
            dest_path = os.path.join(dest_dir, src_name)
            if os.path.exists(dest_path):
                os.remove(dest_path)
            shutil.move(src_path, dest_dir)
        shutil.rmtree(os.path.join('update'))
        print("Обновление завершено успешно!")
def check_for_updates():
  cache_folder = 'cache'
  if not os.path.exists(cache_folder):
    os.mkdir(cache_folder)
  latest_version_url = 'https://raw.githubusercontent.com/devcat86/multipy/master/version.txt'
  latest_version_path = os.path.join(cache_folder, 'latest_version.txt')
  if not os.path.exists(latest_version_path):
    response = requests.get(latest_version_url)
    with open(latest_version_path, 'w') as f:
      f.write(response.text)
  with open(latest_version_path) as f:
    latest_version = f.read().strip()
  if latest_version > current_version:
    print(f"Доступна новая версия {latest_version}")
    update = input("Хотите обновиться? (y/n) ")
    if update.lower() == 'y':
      print("Обновляемся...")
      update_program()
if __name__ == '__main__':
  check_for_updates()
try:
    def prt():
        print(" <<MultiPy>> \n 1 - PaintGPT \n 2 - О MultiPy \n 3 - Что нового? \n 4 - игра КНБ \n 5 - игра Угадай число \n 6 - Секундомер \n 7 - Таймер обратного отсчета \n 8 - Сверх-Таймер обратного отсчета \n 9 - Бросить кубик \n 10 - Погода \n 11 - Генератор \n 12 - Base64 \n 13 - Узнать длинну строки(len) \n 14 - beta \n 15 - ping")
    prt()
    ipt = int(input("Что вы хотите сделать? (Введите 0 или Ctrl+C для выхода):"))
    while ipt != 0:
        if ipt == 1:
            try:
                def paint():
                    # задаю цвет
                    colormode(255)
                    r = randint(0, 255)
                    g = randint(0, 255)
                    b = randint(0, 255)
                    color1 = (r, g, b)
                    r = randint(0, 255)
                    g = randint(0, 255)
                    b = randint(0, 255)
                    color2 = (r, g, b)
                    color(color1, color2)
                    #скорость
                    speed(10)
                    # генерация 
                    pensize(randint(4, 10))
                    cur1 = randint(10, 200)
                    ran1 = randint(2,9)
                    # рандомные координаты
                    penup()
                    goto(randint(-250, 250), randint(-250, 250))
                    pendown()
                    if ran1 == 2:
                        # звезда
                        begin_fill()
                        for i in range(5):
                            forward(150)
                            left(144)
                        end_fill()
                    if ran1 == 3:
                        # квадрат 1
                        if randint(1,2) == 1:
                            begin_fill()
                            for i in range(4):
                                forward(100)
                                left(90)
                            end_fill()
                        else:
                            for i in range(4):
                                forward(100)
                                left(90)
                    if ran1 == 4:
                        # круг 2
                        if randint(1,2) == 1:
                            begin_fill()
                            circle(cur1)
                            end_fill()
                        else:
                            circle(cur1)
                    if ran1 == 5:
                        # треугольник
                        if randint(1,2) == 1:
                            begin_fill()
                            for i in range(3):
                                forward(cur1)
                                left(120)
                            end_fill()
                        else:
                            for i in range(3):
                                forward(cur1)
                                left(120)
                    if ran1 == 6:
                        # спираль
                        per11 = 0
                        for i in range(randint(10, 36)):
                            forward(per11)  
                            per11 += 5
                            left(90) 
                    if ran1 == 7:
                        # пончик
                        speed(15)
                        r = randint(0, 255)
                        g = randint(0, 255)
                        b = randint(0, 255)
                        color2 = (r, g, b)
                        for i in range(18):
                            color(color1)
                            forward(100)
                            left(120)
                            left(10)
                            color(color2)
                            forward(100)
                            left(120)
                            left(10) 
                        speed(10)
                    if ran1 == 8:
                        # ромб
                        ran2 = randint(50,150)
                        left(randint(0,360))
                        for i in range(2):
                            left(45)
                            forward(ran2)
                            left(135)
                            forward(ran2)
                    if ran1 == 9:
                        # шестиугольник
                        ran2 = randint(50,150)
                        if randint(1,2) == 1:
                            for i in range(6):
                                forward(ran2)
                                left(60)
                        else:
                            ran2 = randint(50,150)
                            begin_fill()
                            for i in range(6):
                                forward(ran2)
                                left(60)
                            end_fill()
                while True:
                    paint()
            except Exception:
                print("PaintGPT закрыт")
        elif ipt == 2:
            print(f"Программа MultiPy. Версия {current_version} от 18.08.23. Некоторые пункты взяты из интернета, я не писал их сам. Также спасибо 4vanyek и ChatGPT за помощь в некоторых командах и моментах")
            print("Последняя стабильная версия: 3.0.2")
        elif ipt == 3:
            main_fun.info()
        elif ipt == 4:
            main_fun.knb() 
        elif ipt == 5:
            c1 = 0
            count1 = 1
            print("Угадайте число от 1 до 100! (Введите 0 если хотите сдаться)")
            count = randint(1,100)
            if randint(1,100) == 3:
                count = randint(5,20)**40
            price = int(input("Введите число: "))
            while price != count:
                count1 += 1
                if price > 101:
                    print("Сказали же, ДО 100 xD")
                elif count1 > 100:
                    print("Вам с шансем 1% выпало число больше 100! Число", count)
                elif price > count:
                    print("Число меньше!")
                elif price < count:
                    print("Число больше!")
                elif price == 0:
                    print("Число:", count)
                    break
                else:
                    break
                price = int(input("Введите число: "))
            if price == count:
                    print("Вы угадали!")
                    print("Количество попыток:", count1)
        elif ipt == 6:
            sec_start = int(input("1 - запустить секундомер, 0 - выйти: "))
            if sec_start == 1:
                start = time()
                sec_end = int(input("0 - стоп: "))
                end = time()
                total_time = (end - start)
                print("Время -",round(total_time, 3)) 
        elif ipt == 7:
            timer1 = int(input("Таймер обратного отсчета. Введите секунды: "))
            for i in range(timer1, -1, -1):
                print(i)
                sleep(1)
        elif ipt == 8:
            timer1 = int(input("Супер-Таймер обратного отсчета. Введите что либо: "))
            for i in range(timer1, -1, -1):
                print(i)
        elif ipt == 9:
            print("Вам выпало", randint(1,6))
        elif ipt == 10:
            print("Команда полностью написана через ChatGPT")
            city = input("Введите название города: ")
            weather = main_fun.get_weather(city)
            print(weather)
        elif ipt == 11:
            per1 = int(input("1 - генератор букв, 2 - генератор цифр, 3 - генератор пароля(буквы + цифры): "))
            if per1 == 1:
                per2 = ""
                dsds = int(input("Введите длинну: "))
                alfeu = "abcdefghijklmnopqrstuvwxyz"
                alfru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                gdh = input("А какой язык? eu / ru / all? ").lower()
                if gdh == "ru":
                    alf = alfru
                if gdh == "eu":
                    alf = alfeu
                if gdh == "all":
                    alf = ""
                    alf += alfru
                    alf += alfeu
                for i in range(dsds):
                    per2 += alf[randint(0, (len(alf) - 1))]
                print(per2)
            if per1 == 2:
                dsds = int(input("Введите длинну пароля: "))
                per1 = ""
                for i in range(dsds):
                    per1 += str(randint(0,9))
                print(per1)
            if per1 == 3:
                per2 = ""
                dsds = int(input("Введите длинну: "))
                alfeu = "abcdefghijklmnopqrstuvwxyz"
                alfru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                gdh = input("А какой язык? eu / ru / all? ").lower()
                if gdh == "ru":
                    alf = alfru
                elif gdh == "eu":  
                    alf = alfeu
                elif gdh == "all":
                    alf = "" 
                    alf += alfru
                    alf += alfeu
                for i in range(dsds):
                    per2 += alf[randint(0, len(alf)-1)]
                    if randint(1,3) == 1:
                        for i in range(randint(1, 3)):
                            per2 += str(randint(0,9))
                if len(per2) > dsds:
                    per2 = per2[:dsds]
                print(per2)
        elif ipt == 12:
            q = int(input("1 - зашифровать, 2 - расшифровать: "))
            if q == 2:
                encoded_string = input("Введите строку для расшифрования: ")
                decoded_bytes = base64.b64decode(encoded_string)
                decoded_string = decoded_bytes.decode("utf-8")
                print(decoded_string)
            if q == 1:
                q = input("Введите строку для шифрования: ")
                b = q.encode("UTF-8")
                e = base64.b64encode(b)
                s1 = e.decode("UTF-8")
                print(s1)
        elif ipt == 13:
            per3 = input("Введите строку: ")
            print("Длинна строки:", len(per3))
        elif ipt == 14:
            main_beta.beta()
        elif ipt == 15:
            i1 = input("Введите ip, или доменное имя для пинга(укажите после ip -t если надо пинговать бесконечно): ")
            print(os.system(f"ping {i1}"))
        else: 
            print("???")
        ipt = input("Нажмите Enter чтобы показать меню ")
        if ipt == "":
            prt()
            ipt = int(input("Что вы хотите сделать? (Введите 0 или Ctrl+C для выхода): "))
    print("exit...")
except KeyboardInterrupt:
    print("\nexit...")

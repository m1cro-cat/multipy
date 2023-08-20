current_version = "3.1.2.4"
version_date = "20.08.23"

from random import *
from time import *
from turtle import *
import os
import sys
import base64
import requests
import shutil
import main_beta

def prt():
    print(" <<MultiPy>> \n 1 - PaintGPT \n 2 - О MultiPy \n 3 - Что нового? \n 4 - Игра КНБ \n 5 - Игра Угадай число \n 6 - Секундомер \n 7 - Таймер обратного отсчета \n 8 - Разное \n 9 - Бросить кубик \n 10 - Погода \n 11 - Генератор \n 12 - Base64 \n 13 - Узнать длину строки (len) \n 14 - beta \n 15 - ping \n 16 - Проверить обновления")

def updateProgram():
    url = 'https://github.com/devcat86/multipy/archive/master.zip'
    update_zip = os.path.join('cache', 'update.zip')
    response = requests.get(url)
    with open(update_zip, 'wb') as f:
        f.write(response.content)
    shutil.unpack_archive(update_zip, 'update')
    os.remove(update_zip)
    src_dir = os.path.join('update', 'multipy-main')
    dest_dir = os.path.dirname(os.path.abspath(__file__))
    for src_name in os.listdir(src_dir):
        src_path = os.path.join(src_dir, src_name)
        dest_path = os.path.join(dest_dir, src_name)
        if os.path.exists(dest_path):
            os.remove(dest_path)
        shutil.move(src_path, dest_dir)
    shutil.rmtree(os.path.join('update'))
    shutil.rmtree(os.path.join('cache'))
    print("Обновление завершено успешно!\n")
    args = [sys.executable] + sys.argv
    os.execv(sys.executable, args)

def checkForUpdates():
    print("Проверка обновлений.. ")
    cache_dir = os.path.join('cache')
    if os.path.isdir(cache_dir):
        shutil.rmtree(cache_dir)
    cache_folder = 'cache'
    if not os.path.exists(cache_folder):
        os.mkdir(cache_folder)
    latest_version_url = 'https://raw.githubusercontent.com/devcat86/multipy/main/latest_version.txt'
    latest_version_path = os.path.join(cache_folder, 'latest_version.txt')
    if not os.path.exists(latest_version_path):
        response = requests.get(latest_version_url)
        with open(latest_version_path, 'w') as f:
            f.write(response.text)
    with open(latest_version_path) as f:
        latest_version = f.read().strip()
    if latest_version > current_version:
        print(f"Доступна новая версия {latest_version}")
        update = input("Хотите обновиться? (y/n): ")
        if update.lower() == 'y':
            print("Обновляемся...")
            updateProgram()
        elif update.lower() == 'n':
            sleep(0.3)
            print("Обновление отменено\n")
            shutil.rmtree(os.path.join('cache'))
    else:
        print("Обновления не найдены!")
        shutil.rmtree(os.path.join('cache'))

def paintgpt():
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

def info():
    print(f"\nПрограмма MultiPy.\nВерсия {current_version} от {version_date}.\nНекоторые пункты взяты из интернета, я не писал их сам.\nТакже спасибо MystieHum и ChatGPT за помощь в некоторых командах и моментах")

def igraUgadaika():
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

def stopwatch():
    print("Нажмите Enter чтобы начать, Ctrl+C чтобы остановить")
    try:
        input()
        start = perf_counter()

        while True:
            elapsed = perf_counter() - start
            hours = str(int(elapsed / 3600)).zfill(2)
            minutes = str(int(elapsed / 60) % 60).zfill(2) 
            seconds = str(int(elapsed) % 60).zfill(2)
            milliseconds = str(int(elapsed * 1000) % 1000).zfill(3)
            print("\r{0}:{1}:{2}:{3}".format(hours, minutes, seconds, milliseconds), end="")

    except KeyboardInterrupt:
        print("\nСекундомер остановлен!")

def timer():
    try:
        my_time = int(input("Таймер обратного отсчета. Введите секунды: "))
                
        end = time() + my_time
        while time() < end:
            remaining = end - time()
            hours = int(remaining / 3600) 
            minutes = int(remaining / 60) % 60
            seconds = int(remaining) % 60
            milliseconds = int(remaining * 1000) % 1000
            
            print(f"\r{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}", end="")
            print("\r", end="")
            sleep(0.01)
                    
        print("\r\nВремя вышло!")
                
    except ValueError:
        print("Неправильное значение!")

def raznoe():
    ipt1 = int(input("1 - Интересный узор\nВыберите что-нибудь: "))
    if ipt1 == 1:
        try:
            hideturtle()
            per2 = 10
            per1 = 1
            while True:
                speed(per2)
                forward(per1)
                left(90)
                per1 += 1
                per2 += 1
        except Exception:
            print("Закрыто")
    else:
        print("???")

def weather():
    print("Команда полностью написана через ChatGPT")
    city = input("Введите название города: ")
    api_key = '9f847b92b31f51a681d9792e18973c03'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    if weather_data['cod'] == 200:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Температура в городе {str(city).capitalize()}: {temperature}°C, {description}")
    else:
        print("Не удалось получить данные о погоде") 

def gen():
    per1 = int(input("1 - генератор букв, 2 - генератор цифр, 3 - генератор пароля(буквы + цифры): "))
    if per1 == 1:
        per2 = ""
        passLength = int(input("Введите длину: "))
        # alph - это алфавит
        alphEn = "abcdefghijklmnopqrstuvwxyz"
        alphRu = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        lang = input("А какой язык? en / ru / all? ").lower()
        if lang == "ru":
            alph = alphRu
        if lang == "en":
            alph = alphEn
        if lang == "all":
            alph = ""
            alph += alphRu
            alph += alphEn
        for i in range(passLength):
            per2 += alph[randint(0, (len(alph) - 1))]
        print(per2)
    if per1 == 2:
        passLength = int(input("Введите длину пароля: "))
        per1 = ""
        for i in range(passLength):
            per1 += str(randint(0,9))
        print(per1)
    if per1 == 3:
        per2 = ""
        passLength = int(input("Введите длину: "))
        alphEn = "abcdefghijklmnopqrstuvwxyz"
        alphRu = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        lang = input("А какой язык? en / ru / all? ").lower()
        if lang == "ru":
            alph = alphRu
        elif lang == "en":  
            alph = alphEn
        elif lang == "all":
            alph = "" 
            alph += alphRu
            alph += alphEn
        for i in range(passLength):
            per2 += alph[randint(0, len(alph)-1)]
            if randint(1,3) == 1:
                for i in range(randint(1, 3)):
                    per2 += str(randint(0,9))
        if len(per2) > passLength:
            per2 = per2[:passLength]
        print(per2)

def base64fun():
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

def length():
    per3 = input("Введите строку: ")
    print("Длина строки:", len(per3))

def ping():
    i1 = input("Введите ip, или доменное имя для пинга (укажите после ip -t если надо пинговать бесконечно): ")
    print(os.system(f"ping {i1}"))

def changelog():
    print("\nЛист обновлений!\n")
    print("3.1.1 / 3.1.2 - 20.08.23")
    print("Перенос всех функций в отдельный файл, крч внутренняя переделка:)\n")
    print("3.1.0 - 20.08.23")
    print("Проверка и установка обновлений\nПеределанный таймер и секундомер\nМелкие исправления\n")
    print("3.0.4 - 18.08.23")
    print("Фиксы, улучшение кода PaintGPT\n")
    print("3.0.3 - 17.08.23")
    print("Много разных фиксов от MystieHum\n")
    print("3.0.1 / 3.0.2 - 15-16.08.23")
    print("Минификсы, улучшение PaintGPT, других команд.\n")
    print("3.0.0 - 11.08.23")
    print("Полностью переписан интерфейс, улучшен код)\n")
    print("2.2.1 - 11.08.23")
    print("Финальная версия 2.x\n")
    print("2.2.0 - 11.08.23")
    print("Переименование программы \nОптимизация кода\n")
    print("2.1.0 - 09.08.23")
    print("Переделка некоторых функций, и добавление новых\n")
    print("2.0.0 - 28.07.23")
    print("Полная переделка кода, убрал лишние функции, которые уже не актуальны. Также добавил кучу всего!\n")
    print("1.5.0 - 16.07.23")
    print("Переименовал в projectpb \nДобавил много функций\n")
    print("1.4.0 - 13.07.23")
    print("Сделал удобнее управление \nПеределал работу погоды \nДобавил таймер и секундомер \nДобавил игру КНБ\n")
    print("1.3.1 - 12.07.23")
    print("Добавил имена комментаторов!\n")
    print("1.3 - 12.07.23")
    print("Добавил функцию DevSettingsOn (тест всего разного))\n")
    print("1.2 - 05.07.23")
    print("Несколько небольших изменений\n")
    print("1.1 - 04.07.23")
    print("Удален пункт мерч, как так он никому не нужен")
    print("Добавлены новые функции\n")

def knb():
    response = int(input("Камень(1), ножницы(2), или бумага?(3) (0 - выход, если вы обиделись введите 4): "))
    while response != 0:
        randomAnswer = randint(1,3)
        if randomAnswer == 1 and response == 1:
            per1 = "Камень, ничья!"
        if randomAnswer == 1 and response == 2:
            per1 = "Камень, я победил!"
        if randomAnswer == 1 and response == 3:
            per1 = "Камень, ты победил!"
        if randomAnswer == 2 and response == 1:
            per1 = "Ножницы, ты победил!"
        if randomAnswer == 2 and response == 2:
            per1 = "Ножницы, ничья!"
        if randomAnswer == 2 and response == 3:
            per1 = "Ножницы, я победил!"
        if randomAnswer == 3 and response == 1:
            per1 = "Бумага, я победил!"
        if randomAnswer == 3 and response == 2:
            per1 = "Бумага, ты победил!"
        if randomAnswer == 3 and response == 3:
            per1 = "Бумага, ничья!"
        elif response == 4:
            print("Игра закончена, вы победили и получаете шоколадную медальку! :3")
            break
        print(per1)
        response = int(input("Камень(1), ножницы(2), или бумага?(3) (0 - выход, если вы обиделись введите 4): "))
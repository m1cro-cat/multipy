from random import *
import requests
import string
def eda():
    per1 = input("Еда - это вкусно! И это точно! Советую поесть, нехотите? Введите 1 чтобы заказать еду, и 0 если вы не хотите:")
    if per1 == "1":
        eda = input("В кафе Долголетие есть блюда на выбор с: курицей, грибами и творогом:")
        if eda == "курица":
            perzakaz1 = input("Есть курица в сливочном соусе с салатом! Будете заказывать?")
            if perzakaz1 == "да":
                print("Заказал, ожидайте доставки! Приятного аппетита!")
        if eda == "грибы":
            perzakaz1 = input("Есть картофельное пюре с грибами, Будете заказывать?")
            if perzakaz1 == "да":
                print("Заказал, ожидайте доставки! Приятного аппетита!")
        if eda == "творог":
            perzakaz1 = input("Есть сырники с джемом, Будете заказывать?")
            if perzakaz1 == "да":
                print("Заказал, ожидайте доставки! Приятного аппетита!")
        if per1 == "0":
            print("Ну ладно!")
def pogod():
    osadki0 = randint(1,5)
    temp0 = randint(1,4)
    pogoda0 = randint(1,2)
    if osadki0 == 1:
        osadki1 = "дождь"
    if osadki0 == 2:
            osadki1 = "кислотный дождь"
    if osadki0 == 3:
            osadki1 = "град"
    if osadki0 == 4:
            osadki1 = "без осадков"
    if osadki0 == 5:
            osadki1 = "торнадо"
    if temp0 == 1:
            temp1 = "+30"
    if temp0 == 2:
            temp1 = "+754"
    if temp0 == 3:
            temp1 = "+7 -7 +15 -20 xD"
    if temp0 == 4:
            temp1 = "-195.. Кто пролил жидкий азот?!?!"
    if pogoda0 == 1:
            pogoda1 = "Солнечно"
    if pogoda0 == 2:
            pogoda1 = "Пасмурно"
    print("Сегодня",pogoda1,",",temp1,",",osadki1)
def info():
        print("Лист обновлений!")
        print("1.5.0 - 16.07.23")
        print("Переименовал в projectpb \nДобавил много функций")
        print("1.4.0 - 13.07.23")
        print("Сделал удобнее управление \nПеределал работу погоды \nДобавил таймер и секундомер \nДобавил игру КНБ")
        print("1.3.1 - 12.07.23")
        print("Добавил имена комментаторов!")
        print("1.3 - 12.07.23")
        print("Добавил функцию DevSettingsOn (тест всего разного))")
        print("1.2 - 05.07.23")
        print("Несколько небольших изменений")
        print("1.1 - 04.07.23")
        print("Удален пункт мерч, как так он никому не нужен")
        print("Добавлены новые функции")
def knb():
        khbi = int(input("Камень(1) ножницы(2) или бумага?(3) (0-выход)"))
        while khbi != 0:
            khb = randint(1,3)
            if khb == 1 and khbi == 1:
                per1 = "камень, ничья!"
            if khb == 1 and khbi == 2:
                per1 = "камень, я победил!"
            if khb == 1 and khbi == 3:
                per1 = "камень, ты победил!"
            if khb == 2 and khbi == 1:
                per1 = "ножницы, ты победил!"
            if khb == 2 and khbi == 2:
                per1 = "ножницы, ничья!"
            if khb == 2 and khbi == 3:
                per1 = "ножницы, я победил!"
            if khb == 3 and khbi == 1:
                per1 = "бумага, я победил!"
            if khb == 3 and khbi == 2:
                per1 = "бумага, ты победил!"
            if khb == 3 and khbi == 3:
                per1 = "бумага, ничья!"
            print(per1)
            khbi = int(input("Камень(1) ножницы(2) или бумага?(3) (0-выход)"))
def get_weather(city):
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
                return f"Температура в городе {city}: {temperature}°C, {description}"
            else:
                return "Не удалось получить данные о погоде"
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(characters) for _ in range(length))
    return password
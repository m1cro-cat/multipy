from random import *
import requests
import string
def info():
        print("Лист обновлений!")
        print("3.0.3 - 17.08.23")
        print("Рисовалка теперь не вылетает, а нормально закрывается")
        print("3.0.1, 3.0.2 - 15-16.08.23")
        print("Минификсы, улучшение paintgpt, других команд.")
        print("3.0.0 - 11.08.23")
        print("Полностью переписан интерфейс, улучшен код)")
        print("2.2.0 - 11.08.23")
        print("Переименование программы \n Оптимизация кода")
        print("2.1.0 - 09.08.23")
        print("Переделка некоторых функций, и добавление новых")
        print("2.0.0 - 28.07.23")
        print("Полная переделка кода, убрал лишние функции, которые уже не актуальны. Также добавил кучу всего!")
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
        khbi = int(input("Камень(1) ножницы(2) или бумага?(3) (0-выход, если вы обиделись введите 4): "))
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
            elif khbi == 4:
                 print("Игра закончена, вы победили и получаете шоколадную медальку! :3")
                 break
            print(per1)
            khbi = int(input("Камень(1) ножницы(2) или бумага?(3) (0-выход, если вы обиделись введите 4): "))
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

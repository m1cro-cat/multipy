from functions import *
try:
    prt()
    ipt = int(input("Что вы хотите сделать? (Введите 0 или Ctrl+C для выхода): "))
    while ipt != 0:
        if ipt == 1:
            lite()
        elif ipt == 2:
            info()
        elif ipt == 3:
            changelog()
        elif ipt == 4:
            knb() 
        elif ipt == 5:
            igraUgadaika()
        elif ipt == 6:
            stopwatch()
        elif ipt == 7:
            timer()
        elif ipt == 8:
            raznoe()
        elif ipt == 9:
            print("Вам выпало", randint(1,6))
        elif ipt == 10:
            weather()
        elif ipt == 11:
            gen()
        elif ipt == 12:
            base64fun()
        elif ipt == 13:
            length()
        elif ipt == 14:
            ping()
        elif ipt == 15:
            lite()
        elif ipt == 16:
            convertor()
        else: 
            print("???")
        ipt1 = input("\nНажмите Enter чтобы показать меню ")
        if ipt1 == "":
            prt()
            ipt = int(input("Что вы хотите сделать? (Введите 0 или Ctrl+C для выхода): "))
    print("exit...")
except KeyboardInterrupt:
    print("\nexit...")
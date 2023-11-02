from random import *
from time import *
from turtle import *
from functions import *
import os
import base64
import main_beta
import datetime
def old():
        print("Чтобы получить архив этой программы, пишите .... нету у меня больше дискорда..")
def beta1():
    ipt = int(input(" <<MultiPyBETA>> \n 0 - выход \n 1 - : "))
    while ipt != 0:
        ipt = int(input(" <<MultiPyBETA>> \n 0 - выход \n 1 -  :"))
def beta():
    t1 = int(input(" <<MENU>> \n 1 - старый бот(до переделки) \n 2 - бета версии новых функций: "))
    if t1 == 1:
        old()   
    elif t1 == 2:
        beta1()    
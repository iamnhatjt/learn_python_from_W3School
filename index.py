import sys
import datetime
import math
from math import pi
import calendar
def bai1():
    print("Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. Twinkle, twinkle, little star, \n\tHow I wonder what you are")

def bai2():
    print('your version: ', sys.version)

def bai3():
    print('current time: ', datetime.datetime.now())

def bai4():
    a = float(input('input your current: '))
    print('your area: ', a*a*pi)

def bai5():
    fname = str(input('your first name: '))
    lname = str(input('your last name: '))
    print('your name: ', lname, fname)

def bai6():
    values = input('input your number: ')
    listNumber = values.split(',')
    tupleNumber = tuple(listNumber)
    print(listNumber)
    print(tupleNumber)

def bai7():
    filename = input('input your file: ')
    fname = filename.split('.')
    print(fname[-1])

def bai8():
    listInput = input('input your list color: ')
    listColor = listInput.split(',')
    print('first color: '+ listColor[0], ',last color: '+ listColor[-1])

def bai9():
    inputDate = input('input your date: ')
    listDate = inputDate.split(',')
    print('your date start:', listDate[0],'/',listDate[1], '/', listDate[2])

def bai10():
    inputInter = int(input('input your number: '))
    print(inputInter+ inputInter*10 +inputInter + inputInter*100+inputInter*10 + inputInter)

def bai11():
    inputNumber = input('input your number: ')
    print(math.fabs( int(inputNumber)))

def bai12():
    y = int(input('input your year: '))
    m = int(input('input your month: '))
    print(calendar.month(y,m))



bai12()
import threading as td
from time import sleep
from string import ascii_lowercase as al
from random import randint


def counter():
    for i in range(10):
        print(i)
        sleep(1)


def alphabet():
    for a in al:
        print(a)
        print(f"active threads count = {td.active_count()}")
        sleep(1)


def randoms():
    for p in range(20):
        print(randint(11, 100))
        sleep(0.6)


x = td.Thread(target=counter)
x.start()

y = td.Thread(target=randoms)
y.start()
alphabet()

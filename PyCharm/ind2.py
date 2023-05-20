#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Lock, Thread
from queue import Queue
import math

EPS = .0000001
q = Queue()
lock = Lock()


def sum_func(x, q):
    summa = 1.0
    temp = 0
    n = 1
    while abs(summa - temp) > EPS:
        temp = summa
        summa += math.sin(n*x) / n
        n += 1
    q.put(summa)


def check_func(x, q):
    summa = q.get()
    res = - math.log(2 * math.sin(0.5 * x))

    print(f"Sum is {summa}")
    print(f"Check: {res}")


if __name__ == '__main__':
    x = math.pi
    th1 = Thread(target=sum_func, args=(x, q)).start()
    th2 = Thread(target=check_func, args=(x, q)).start()

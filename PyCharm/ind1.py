#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from queue import Queue
from threading import Lock, Thread


def manager():
    lock.acquire()  # Захватываем блокировку
    tasks = []
    while not q.empty():  # Пока очередь не пуста
        task = q.get()  # Извлекаем задачу из очереди
        worker = random.choice(workers)  # Случайным образом выбираем работника
        print(f"Менеджер передал задачу '{task}' работнику {worker}")
        tasks.append({
            "Задача": task,
            "Работник": worker
        })

    lock.release()  # Освобождаем блокировку

    # Выводим информацию о нераспределенных задачах
    for task in tasks:
        if task["Работник"] is None:
            print(f"Задача '{task['Задача']}' ожидает выполнения")


def worker():
    lock.acquire()
    while not q.empty():
        task = q.get()
        print(f"Работник {worker_id} выполняет задачу: '{task}'")
        lock.release()
        lock.acquire()
    lock.release()


if __name__ == "__main__":
    tasks = ["Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5"]
    workers = ["Работник A", "Работник B", "Работник C"]
    lock = Lock()
    q = Queue()

    # Заполняем очередь задачами
    for task in tasks:
        q.put(task)

    # Запускаем потоки работников
    for worker_id in workers:
        Thread(target=worker).start()

    # Запускаем поток менеджера
    Thread(target=manager).start()

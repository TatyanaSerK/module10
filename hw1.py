import time
from threading import Thread


def test1():
    # выводит числа от 1 до 10 с интервалом в 1 секунду
    for num in range(1, 11):
        print(num)
        time.sleep(1)

def test2():
    # выводит буквы от 'a' до 'j' с интервалом в 1 секунду
    for elem in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'):
        print(elem)
        time.sleep(1)



th1 = Thread(target=test1)       # Создаём поток
th1.start()                      # запускаем его

th2 = Thread(target=test2)        # Создаём поток
th2.start()                      # запускаем его

# заморозки интерпретации
th1.join()
th2.join()













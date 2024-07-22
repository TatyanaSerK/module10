import threading
import time
from threading import Thread, Lock  # импорт библиотеки threading
import queue


class Table:
    # '''класс для столов '''
    def __init__(self, number=int, is_busy=True):
        super().__init__()
        self.number = number  #номер стола
        self.is_busy = is_busy  #(bool) - занят стол или нет

class Cafe:
    # '''класс для симуляции процессов в кафе'''
    def __init__(self, tables):
        super().__init__()
        self.queue = queue.Queue() # очередь для посетителей
        self.queue_t = queue.Queue()  # очередь для столов
        self.tables = tables # номер стола

    def customer_arrival(self):
        # '''моделирует приход посетителя каждую секунду'''
        self.customer = 0
        while self.customer < 20: # всего посетителей 20
            self.customer += 1
            print(f"Посетитель {self.customer} прибыл.")
            self.queue.put(self.customer)  # посетитель поступает в очередь
            self.serv_customer(self.customer) #начинаем обслуживание
            time.sleep(1)


    def serv_customer(self, customer):
# '''моделирует обслуживание посетителя.
# Проверяет наличие свободных столов, в случае наличия стола -
#  начинает обслуживание посетителя (запуск потока),
#  в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.'''

        for i in range(len(tables)): #проверяет наличие свободных столов
            if tables[i].is_busy:
                table = i + 1
                self.queue_t.put(table)  # стол поступает в очередь
                while self.queue.empty() == False:
                    customer = self.queue.get()
                    if self.queue_t.empty() == False:
                        print(f"Посетитель {self.customer} ожидает свободный стол.")
                    table = self.queue_t.get()
                    tr = Customer(table, customer)
                    tr.start() # начинаем обслуживание посетителя (запуск потока)
                    if not tables[i].is_busy:
                        tr.join()


class Customer(Thread):
    # '''класс (поток) посетителя. Запускается, если есть свободные столы.'''

    def __init__(self, table, customer):
        super().__init__()
        self.customer = customer
        self.table = table
        # self.lock = Lock()

    def run(self):

        if tables[self.table - 1].is_busy:
            print(f"Посетитель номер {self.customer} сел за стол {self.table}.")
            tables[self.table - 1].is_busy = False  # стол занят

            if not tables[self.table - 1].is_busy:
                print(f"Столик {self.table} занят")
                time.sleep(5)  # обслуживается 5 сек
                print(f"Посетитель номер {self.customer} покушал и ушёл.")
                tables[self.table - 1].is_busy = True  # стол освободился


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
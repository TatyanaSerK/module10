from threading import Thread, Lock  # импорт библиотеки threading


class BankAccount(Thread):  # банковский счет
    def __init__(self):
        self.lock = Lock()  # блокировка доступа к общему ресурсу
        self.balance = 1000  # баланс на счету
        print(f'Balance - {self.balance}')  # выводим

    def deposit(self, amount):  # для пополнения
        with self.lock:  # используем блокировку
            self.balance += amount  # пополняем на необходимую сумму
        print(f'Deposited {amount}, new balance is {self.balance}')  # выводим

    def withdraw(self, amount):  # для снятия
        with self.lock:  # используем блокировку
            self.balance -= amount  # снимаем с баланса
            print(f'Withdrew {amount}, new balance is {self.balance}')  # выводим


def deposit_task(account, amount):  # функция пополнения повторяется 5 раз
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):  # функция снятия повторяется 5 раз
    for _ in range(5):
        account.withdraw(amount)


# вызываем класс
account = BankAccount()

# создаем потоки
deposit_thread = Thread(target=deposit_task, args=(account, 100))  # пополнение на 100
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))  # снятие 150
# запускаем потоки
deposit_thread.start()
withdraw_thread.start()
# ждем завершения потоков
deposit_thread.join()
withdraw_thread.join()

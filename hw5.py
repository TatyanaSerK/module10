from threading import Thread

class WarehouseManager(Thread):

    def __init__(self):
        super().__init__()
        # self.requests = requests
        self.data = {}  # ключ - название продукта, а значение - его кол-во

    def process_request(self, request):  # реализует запрос (действие с товаром), принимая request - кортеж.
        act = request[1]  # действие(добавить/убрать)
        prod = request[0]  # название продукта
        quantity = int(request[2])  # количество продукта

        if act == 'receipt':  # receipt - получение
            if prod in self.data.keys():  # В случае получения данные должны поступить в data
                a = self.data[prod]  # значение ключа
                self.data[prod] = a + quantity  # изменить значение ключа, если позиция уже была в словаре
            else:
                self.data[prod] = quantity      # добавить пару, если её не было

        if act == 'shipment':  # shipment - отгрузка.

            if prod in self.data.keys():  # если товар есть в data
                a = self.data[prod]  # значение ключа
                if a > 0:  # если товара больше чем 0
                    self.data[prod] = a - quantity  # В случае отгрузки данные товара должны уменьшаться
        return self.data  # возвращаем словарь

    def run(self, requests):  # принимает запросы и создаёт для каждого свой параллельный процесс
        for request in requests:
            my_thread = Thread(target=self.process_request, args=(request, ))
            my_thread.start()  # запускает его(start)
            my_thread.join()  # замораживает(join)


# Создаем менеджера склада
manager = WarehouseManager

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)]

# Запускаем обработку запросов
manager.run(requests)
# Выводим обновленные данные о складских запасах
print(manager.data)

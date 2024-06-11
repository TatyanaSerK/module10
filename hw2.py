import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        enemy = 100                                #кол-во врагов
        day = 0
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            time.sleep(1)                           #1 день = 1 сек
            day += 1
            enemy = enemy - self.skill              #каждый день врагов меньше
            print(f'{self.name}, сражается {day} день(дня)..., осталось {enemy} воинов.')
        if enemy == 0:
            print(f' {self.name} одержал победу спустя {day} дней!')


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()

print("Все битвы закончились!")

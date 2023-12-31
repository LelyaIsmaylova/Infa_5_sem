# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
    
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
    
class PinkDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'розовый'

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(x)
        return self.__quest

class BlueDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'голубой'

    def question(self):
        n = randint(1, 100)
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        if d * d > n:
            is_prime = 1
        else:
            is_prime = 2

        self.__quest = f'Простое ли число {n}. Если да, пиши 1, иначе 2'
        self.set_answer(is_prime)
        return self.__quest
    



enemy_types = [GreenDragon, RedDragon, BlackDragon, PinkDragon, BlueDragon]
# enemy_types = [BlueDragon]

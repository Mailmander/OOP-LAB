import random
from Interface import GamePrint
class Field():
    name = "Default"
    field_type = 0 #0 - старт, 1 - цветная, 2 - станция, 3 - специальная, 4 - шанс, 5 - вход в тюрьму, 6 - тюрьма, 7 - налог, 8 - сверхналог, 9 - стоянка. 
    field_number = -1
    def __init__(self):
        pass

class Cell_buyable(Field):
    cost_of_cell = 0
    owner = None
    number = -1
    def buy(self, player):
        owner = player


class Cell_buyable_color(Cell_buyable):
    field_type = 1
    color = "Default"
    houses = 0
    houses_cost = 0
    base_arend = 0
    def cost(self):
        return self.base_arend*self.houses+1000

class Cell_buyable_stations(Cell_buyable):
    field_type = 2
    arend_rail = [25, 50, 100, 200]
    def cost(self, number_of_builds):
        return self.arend_rail[number_of_builds-1]

class Cell_buyable_spec(Cell_buyable):
    field_type = 3
    arend_spec = [400, 1000]
    def cost(self, number_of_builds): #без dice:     def cost(self, dice, number_of_builds):
        return self.arend_spec[number_of_builds-1]# * dice

class Cell_Chance (Field):
    field_type = 4
    def chance(self):
        k = random.randint(1, 10)
        GamePrint.chance_print(k)
        match k:
            case 1:
                return -1000
            case 2:
                return -200
            case 3:
                return 200
            case 4:
                return 300
            case 5:
                return -300
            case 6:
                return -200
            case 7:
                return -200
            case 8:
                return -200
            case 9:
                return -200
            case 10:
                return -200

class Cell_5 (Field):
class Cell_6(Field):
class Cell_7(Field):
class Cell_8(Field):
class Cell_9(Field):







import random

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
    def cost(self, dice, number_of_builds):
        return self.arend_spec[number_of_builds-1] * dice

class Cell_Chance (Field):
    field_type = 4
    def chance(self):
        k = random.randint(1, 10)
        match k:
            case 1: 
                print("Травонувся шаурмою, мінус 1000 гривень на ліки")
                return -1000
            case 2: 
                print("Пацани з НАУ набили лице за 35-м корпусом, мінус 200")
                return -200
            case 3: 
                print("Ви з пацанами набили лице студенту НАУ, плюс 200")
                return 200
            case 4: 
                print("Мінарченко дав гроші за макулатуру для розтаплювання дачі, плюс 300")
                return 300
            case 5: 
                print("У вас днюха! Ві всіх пригощаете пивом на поляні. Мінус 300")
                return -300
            case 6: 
                print("Джекпот! Вам скинулись за паль РГР по ЧМ! Плюс 1000!")
                return -200
            case 7: 
                print("Тест шанса, как же много надо придумывать, -200iq momment")
                return -200
            case 8: 
                print("Тест шанса, как же много надо придумывать, -200iq momment")
                return -200
            case 9: 
                print("Тест шанса, как же много надо придумывать, -200iq momment")
                return -200
            case 10: 
                print("Тест шанса, как же много надо придумывать, -200iq momment")
                return -200


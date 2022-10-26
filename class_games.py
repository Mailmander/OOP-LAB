class Field():
    name = "Default"
    field_type = 0 #0 - старт, 1 - цветная, 2 - станция, 3 - специальная, 4 - шанс, 5 - вход в тюрьму, 6 - тюрьма, 7 - налог, 8 - сверхналог, 9 - стоянка. 
    def __init__(self):
        pass

class Cell_buyable(Field):
    cost = int(0)
    owner = None
    number = -1
    def buy(self, player):
        owner = player

# class Cell_Jail_enter(Field):
#     def __init__(self):
#         pass

# class Cell_Jail(Field):
#     def __init__(self):
#         pass

class Cell_buyable_color(Cell_buyable):

    color = "Default"
    houses = 0
    houses_cost = 0
    arend = [0, 0, 0, 0, 0, 0]
    def cost(self):
        return self.arend[self.houses]

class Cell_buyable_stations(Cell_buyable):
    arend_rail = [25, 50, 100, 200]
    def cost(self, number_of_builds):
        return self.arend_rail[number_of_builds-1]

class Cell_buyable_spec(Cell_buyable):
    arend_spec = [4, 10]
    def cost(self, cubics, number_of_builds):
        return self.arend_spec[number_of_builds-1] * cubics

class Cell_Chance (Field):
    def chance(self):
        return "Тест шанса, как же много надо придумывать, -200iq momment", -200


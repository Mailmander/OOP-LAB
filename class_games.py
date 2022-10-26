class Field():
    def __init__(self):
        pass

class Cell_buyable(Field):
    name = "Default"
    cost = int(0)
    owner = None
    number = -1

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

class Cell_buyable_spec(Cell_buyable):
    arend_rail = [4, 10]
    def cost(self, cubics):
        return self.arend_rail[1] * cubics

class Cell_Chance (Field):
    def chance(self):
        return "Тест шанса, как же много надо придумывать, -200iq momment", -200


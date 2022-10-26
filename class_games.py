class Field():
    def __init__(self):
        pass

class Cell_buyable(Field):
    cost = int(0)
    owner = None

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
    # def cost():
    #     return self.arend[self.houses]

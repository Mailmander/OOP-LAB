import random
from Interface import GamePrint
from Player_class import Player

class Field():
    name = "Default"
    field_type = 0 #0 - старт, 1 - цветная, 2 - станция, 3 - специальная, 4 - шанс, 5 - вход в тюрьму, 6 - тюрьма, 7 - налог, 8 - сверхналог, 9 - стоянка. 
    field_number = -1
    def __init__(self):
        pass

    def action(self):
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

    def action(self, Player, field, players_array):
        if field.owner == None:
            if GamePrint.buyoption():
                # BUY
                if (Player.buy_newfield(field.cost_of_cell, Player.current_field) == 1):
                    field.owner = Player
                GamePrint.actionend()
            else:
                # AUKCION
                if (Player.auction(field.cost_of_cell, Player.current_field, players_array) == 1):
                    field.owner = Player

                GamePrint.actionend()
        elif field.owner == Player:
            # YOUR FIELD
            if GamePrint.field_update(field, Player):  # self from GameConditions in Class_Games won't work
                Player.money_withdraw(field.houses_cost)
                field.houses += 1
            GamePrint.actionend()
        else:
            # NALOG (num of houses in ownership)
            Player.tax(field.cost(),
                       field.owner)
            GamePrint.actionend()


class Cell_buyable_stations(Cell_buyable):
    field_type = 2
    arend_rail = [25, 50, 100, 200]
    def cost(self, number_of_builds):
        return self.arend_rail[number_of_builds-1]
    def action(self, Player, field, players_array):
        if field.owner == None:
            if GamePrint.buyoption():
                # BUY
                if (Player.buy_newfield(field.cost_of_cell, Player.current_field) == 1):
                    field.owner = Player
                    Player.stations += 1
                GamePrint.actionend()
            else:
                # AUKCION
                if (Player.auction(field.cost_of_cell, Player.current_field, players_array) == 1):
                    field.owner = Player

                GamePrint.actionend()
        elif field.owner == Player:
            # YOUR FIELD
            GamePrint.station_info(Player)
            GamePrint.actionend()
        else:
            # NALOG(num of stations in ownership)
            Player.tax(field.cost(Player.stations), field.owner)
            GamePrint.actionend()


class Cell_buyable_spec(Cell_buyable):
    field_type = 3
    arend_spec = [400, 1000]
    def cost(self, number_of_builds): #без dice:     def cost(self, dice, number_of_builds):
        return self.arend_spec[number_of_builds-1]# * dice
    def action(self, Player, field, players_array):
        if field.owner == None:
            if GamePrint.buyoption():
                # BUY
                if (Player.buy_newfield(field.cost_of_cell, Player.current_field) == 1):
                    field.owner = Player
                    Player.specials += 1
                GamePrint.actionend()
            else:
                # AUKCION
                if (Player.auction(field.cost_of_cell, Player.current_field, players_array) == 1):
                    field.owner = Player
                GamePrint.actionend()
        elif field.owner == Player:
            # YOUR FIELD
            GamePrint.specialfields_info(Player)
            GamePrint.actionend()
        else:
            # NALOG(num of fields in ownership)
            Player.tax(field.cost(Player.specials), field.owner)
            GamePrint.actionend()


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
    @staticmethod
    def action(Player, chance_deposit):
        Player.money_deposit(chance_deposit)
        GamePrint.actionend()


class Cell_Prizon_Enter (Field):

    def action(self, Player):
        Player.current_field = 10
        Player.prisoner = 1
        GamePrint.prison_notification()
        GamePrint.actionend()

class Cell_Prizon(Field):
    def action(self, Player):
        if Player.prisoner:
            Player.prisoner = 0
            for i in range(3):
                A = random.randint(1, 6)
                B = random.randint(1, 6)
                dice = A + B
                GamePrint.prison_dice(A, B, dice)
                if A == B:
                    GamePrint.prison_success()
                    return
        else:
            GamePrint.actionend()

class Cell_Tax(Field):
    def action(self, Player):
        GamePrint.extratax(2000)
        Player.money_withdraw(2000)
        GamePrint.actionend()

class Cell_Super_Tax(Field):
    def action(self, Player):
        GamePrint.extratax(4000)
        Player.money_withdraw(4000)
        GamePrint.actionend()

class Cell_Waiter(Field):
    def action(self, Player):
        if Player.waiting == 0:
            Player.waiting = 1
            GamePrint.skip()
        else:
            Player.waiting = 0
            GamePrint.actionend()








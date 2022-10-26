
class Player():
    def __init__(self, playernumber):
        self.name = input("Enter Player name.\n")
        self.money = 20000
        self.playernumber = playernumber
        self.owned_fields=[]
        self.fields_tosell=[]
        self.current_field=0
        self.double = 0
        self.prisoner = 0
        self.waiting = 0

    def nextfield(self,dice):
        self.current_field=(self.current_field+dice)%40
        return self.current_field


    def buy_newfield(self,price,fieldnumber):
        if(self.money>price):
            self.money=self.money-price
            self.owned_fields.append(fieldnumber)
        else:
            print("Грошиків тобі не вистачає друже :(")

    def field_deposit(self):
        deposit=100
        if(self.owned_fields.count(2)!=0):
            self.owned_fields.remove(2)
            self.current_field.append(2)
            return

    def field_undeposit(self):
        deposit = 100
        if (self.owned_fields.count(2) != 0):
            self.owned_fields.remove(2)
            self.current_field.append(2)
            return



    def money_transferto(self,userto,sum):
        if(self.money>sum & sum > 0 ):
            self.money=self.money-sum
            userto.money = userto.money + sum
        else:
            print("В Цього Гравця нема таких грошей :(")











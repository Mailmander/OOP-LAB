
class Player():
    def __init__(self, playernumber):
        print("Введіть ім'я гравця №",playernumber+1)
        self.name = input()
        self.money = 20000
        self.playernumber = playernumber
        self.owned_fields=[]
        self.fields_tosell=[] #Wil be soon...
        self.current_field=0
        self.double = 0
        self.prisoner = 0
        self.waiting = 0
        self.alive = 1
        self.stations = 0
        self.specials = 0


    def isowner(self,fieldnumber):
        if(self.owned_fields.count(fieldnumber)!=0):
            return 1
    def money_deposit(self,amountofmoney):

        if(self.money>=-amountofmoney):
            self.money=self.money+amountofmoney
        else:
            self.alive=0
        return

    def money_withdraw(self,amountofmoney):

        if(self.money>amountofmoney):
            self.money=self.money-amountofmoney
        else:
            self.alive = 0
        return


    def nextfield(self,dice):

        self.current_field = (self.current_field + dice) % 40
        return self.current_field


    def buy_newfield(self,price,fieldnumber):
        if(self.money>price):
            self.money=self.money-price
            self.owned_fields.append(fieldnumber)
            return 1
        else:
            print("Грошиків тобі не вистачає друже :(")
            return 0

    def field_deposit(self,field,deposit):
        if(self.owned_fields.count(field)!=0):
            self.owned_fields.remove(field)
            self.fields_tosell.append(field)
            self.money=self.money+deposit
            return

    def field_undeposit(self,field,fromdeposit):
        if (self.fields_tosell.count(field) != field & self.money>fromdeposit):
            self.fields_tosell.remove(field)
            self.owned_fields.append(field)
            self.money = self.money - fromdeposit
            return



    def money_transferto(self,userto,sum):
        if(self.money>sum & sum > 0 ):
            self.money=self.money-sum
            userto.money = userto.money + sum
        else:
            print("В Цього Гравця нема таких грошей :(")

    def tax(self,fieldtax,owner):
        if(self.money>=fieldtax):
            print("Гравець ", self.name, "виплачує орендну плату у розмірі " , fieldtax , "Гравцю " , owner.name)
            self.money_transferto(owner,fieldtax)
        else:
            self.alive=0
            print("В Цього Гравця нема таких грошей :(")


    def auction(self,fieldprice,field,PlayersArray):
        print("Ця фіча буде додана в наступному глобальному оновленні")
        #i=len(PlayersArray)
        #m=i-1
        #will=1
        #newprice=fieldprice+100
        #while(i!=0):
         #   if(PlayersArray[m].playernumber != self.playernumber & PlayersArray[m].money>=newprice):
          #      print(PlayersArray[m].name + " може купити це поле за " + newprice)
           #     if(input("Так")):
            #        if(PlayersArray[m].buy_newfield(newprice,field)==1):
             #           return 1
              #  else:
               #     newprice=newprice+100
            #i=(i+1)%i
        return 0















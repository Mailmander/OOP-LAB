from Interface import GamePrint
class Player():
    def __init__(self, playernumber, playername):
        self.name = playername #GamePrint.type_name(self,playernumber)
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
        self.earned = 0
        self.spended = 0


    def isowner(self,fieldnumber):
        if(self.owned_fields.count(fieldnumber)!=0):
            return 1
    def money_deposit(self,amountofmoney):

        if(self.money>=-amountofmoney):
            self.money=self.money+amountofmoney
            self.earned=self.earned+amountofmoney
        else:
            self.alive=0
        return

    def money_withdraw(self,amountofmoney):

        if(self.money>amountofmoney):
            self.money=self.money-amountofmoney
            self.spended=self.spended-amountofmoney
        else:
            self.alive = 0
            print("Гравець ", self.playernumber+1, " відправився в НАУ")
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
            GamePrint.lowmoney()
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
            self.spended=self.spended-sum
            userto.money = userto.money + sum
            userto.earned = userto.earned + sum
        else:
            GamePrint.money_transfer_failure()

    def tax(self,fieldtax,owner):
        if(self.money>=fieldtax):
            GamePrint.tax_pay(self,fieldtax,owner)
            self.money_transferto(owner,fieldtax)
        else:
            self.alive=0
            GamePrint.money_transfer_failure()

    def stats(self):
        numofter=len(self.owned_fields)
        GamePrint.stat_print(self.name,self.earned,self.spended,numofter)


    def auction(self,fieldprice,field,PlayersArray):
        GamePrint.future_update()
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















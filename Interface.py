class GamePrint():
    Chances = ["Травонувся шаурмою, мінус 1000 гривень на ліки","Пацани з НАУ набили лице за 35-м корпусом, мінус 200","Ви з пацанами набили лице студенту НАУ, плюс 200","Мінарченко дав гроші за макулатуру для розтаплювання дачі, плюс 300","У вас днюха! Ві всіх пригощаете пивом на поляні. Мінус 300","Джекпот! Вам скинулись за паль РГР по ЧМ! Плюс 1000!","Тест шанса, как же много надо придумывать, -200iq momment","Тест шанса, как же много надо придумывать, -200iq momment","Тест шанса, как же много надо придумывать, -200iq momment","Тест шанса, как же много надо придумывать, -200iq momment"]
    FieldsTypes = ["старт", "кольорова", "станція", "спеціальна", "шанс", "вхід у в'язницю", "в'язниця", "податок",
                   "надподаток", "стоянка"]
    @staticmethod
    def Numberofplayers():
        plnumber = int(input("Введіть к-ть гравців.\n"))
        return plnumber
    def StartPrint(self,Player):
        print("\nХід ", Player.playernumber + 1, "-го гравця, ", Player.name)
        print("Гравець стоїть на ", Player.current_field, " полі, типу '",
              GamePrint.FieldsTypes[self.FieldsArray[Player.current_field].field_type], "', під назвою '",
              self.FieldsArray[Player.current_field].name, "'")
        if ((self.FieldsArray[Player.current_field].field_type >= 1 and self.FieldsArray[
            Player.current_field].field_type <= 3) and self.FieldsArray[Player.current_field].owner != None):
            print("Власником цього поля є ", self.FieldsArray[Player.current_field].owner.name)
        print("Грошики: ", Player.money)
        print("У гравця є такі поля: ", Player.owned_fields)
        if self.FieldsArray[Player.current_field].field_type:
            print("Ваші дії ----------------------")

    @staticmethod
    def buyoption():
        decision = (input("Купляємо? (1/0):   "))
        return decision

    @staticmethod
    def actionend():
        print("-------------------------------")
    def field_update(self,Player):
        print("Ви потрапили на власне поле з ", self.FieldsArray[Player.current_field].houses, "будівлями."
                                                                                               "\nНова будівля коштуватиме: ",
              self.FieldsArray[Player.current_field].houses_cost)
        if int(input("Бажаєте придбати будівлю? (1/0):   ")):
            return 1
        print("-------------------------------")
    def station_info(Player):
        print("Ви потрапили на власне поле, у вас ", Player.stations, "станцій.")
    def specialfields_info(Player):
        print("Ви потрапили на власне поле, у вас ", Player.specials, "спеціальних полів.")

    @staticmethod
    def prison_notification():
        print("Щасливої прогулянки до в'язниці!")
    def prison_dice(A,B,dice):
        print("Ваші кубики(дубль щоби вийти): ", A, " + ", B, " = ", dice)
    @staticmethod
    def prison_success():
        print("Ви вийшли завчасно і робите наступний крок")
        print("-------------------------------")
    @staticmethod
    def prison_failure():
        print("Пропуск кроку")

    def nextstep_dice(A,B,dice):
        print("Ваші кубики: ", A, " + ", B, " = ", dice)


    def extratax(tax):
        print("Ви сплачуєте ", tax ," як податок")

    @staticmethod
    def skip():
        print("Пропуск кроку")
    def current_field(Player):
        print("Гравець", Player.name, "зараз на", Player.current_field, "полі")
    def type_name(self,playernumber):
        print("Введіть ім'я гравця №", playernumber + 1)
        name = input()
        return name

    @staticmethod
    def lowmoney():
        print("Грошиків тобі не вистачає друже :(")

    @staticmethod
    def money_transfer_failure():
        print("В Цього Гравця нема таких грошей :(")
    def tax_pay(self,fieldtax,owner):
        print("Гравець ", self.name, "виплачує орендну плату у розмірі ", fieldtax, "Гравцю ", owner.name)
    @staticmethod
    def future_update():
        print("Ця фіча буде додана в наступному глобальному оновленні")

    @staticmethod
    def chance_print(id):
        print(GamePrint.Chances[id])

    @staticmethod
    def menu_out():
        print()
        print()
        print()
        print()


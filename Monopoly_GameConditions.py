from cgi import FieldStorage
from Player_class import Player
import random
from class_games import Field
from class_games import Cell_buyable_color
from class_games import Cell_buyable_stations
from class_games import Cell_buyable_spec
from class_games import Cell_Chance


class GameConditions():

	NumOfFields = 40
	PlayersArray = []
	FieldsArray = []
	FieldsTypes = ["старт", "кольорова", "станция", "спеціальна", "шанс", "вхід у в'язницю", "в'язниця", "податок", "надподаток", "стоянка"]

	def CreatePlayers(self):
		self.NumOfPlayers = int(input("Введіть к-ть гравців.\n"))
		for i in range(self.NumOfPlayers):
			self.PlayersArray.append(Player(i))
		return

	def CreateFields(self):
		# Клетка 0 - старт
		cell_cur = Field()
		cell_cur.field_type = 0
		cell_cur.field_number = 0
		self.FieldsArray.append(cell_cur)
		#Клетка 1 - Лавочка напротив 7 общаги 
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 1
		cell_cur.color = "purple"
		cell_cur.name = "Лавочка напроти 7 общаги"
		cell_cur.houses_cost = 1000 
		cell_cur.cost_of_cell = 1500
		cell_cur.base_arend = 500
		self.FieldsArray.append(cell_cur)
		#Клетка 2 - Налог
		cell_cur = Field()
		cell_cur.name = "Податок"
		cell_cur.field_type = 7
		cell_cur.field_number = 2
		self.FieldsArray.append(cell_cur)
		#Клетка 3 - Лавочка напротив 14 общаги 
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 3
		cell_cur.color = "purple"
		cell_cur.name = "Лавочка напроти 14 общаги"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 4 - Шанс 
		cell_cur = Cell_Chance()
		cell_cur.name = "Шанс"
		cell_cur.field_number = 4
		self.FieldsArray.append(cell_cur)
		#Клетка 5 - Автобус 410, Семён неси сахар
		cell_cur = Cell_buyable_stations()
		cell_cur.field_number = 5
		cell_cur.name = "Автобус 410"
		cell_cur.cost_of_cell = 1500
		self.FieldsArray.append(cell_cur)
		#Клетка 6 - Паравоз
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 6
		cell_cur.color = "light blue"
		cell_cur.name = "Паротяг"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 7 - Шанс 
		cell_cur = Cell_Chance()
		cell_cur.name = "Шанс"
		cell_cur.field_number = 7
		self.FieldsArray.append(cell_cur)
		#Клетка 8 - Алея Сакур 
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 8
		cell_cur.color = "light blue"
		cell_cur.name = "Алея Сакур"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 9 - Арка КПИ 
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 9
		cell_cur.color = "light blue"
		cell_cur.name = "Арка КПІ"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 10 - Тюрьма
		cell_cur = Field()
		cell_cur.name = "Тюрьма"
		cell_cur.field_type = 6
		cell_cur.field_number = 10
		self.FieldsArray.append(cell_cur)
		#Клетка 11 - Общага номер 6
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 11
		cell_cur.color = "pink"
		cell_cur.name = "Общага номер 6"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 12 - КПИтелеком
		cell_cur = Cell_buyable_spec()
		cell_cur.field_number = 12
		cell_cur.name = "КПIтелеком"
		cell_cur.cost_of_cell = 1500
		self.FieldsArray.append(cell_cur)
		#Клетка 13 - Общага номер 7
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 13
		cell_cur.color = "pink"
		cell_cur.name = "Общага номер 7"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 14 - Общага номер 14
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 14
		cell_cur.color = "pink"
		cell_cur.name = "Общага номер 14"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 15 - Трамвай 
		cell_cur = Cell_buyable_stations()
		cell_cur.field_number = 15
		cell_cur.name = "Трамвай"
		cell_cur.cost_of_cell = 1500
		self.FieldsArray.append(cell_cur)
		#Клетка 16 - 7 корпус
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 16
		cell_cur.color = "orange"
		cell_cur.name = "7 корпус"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 17 - Шанс 
		cell_cur = Cell_Chance()
		cell_cur.name = "Шанс"
		cell_cur.field_number = 17
		self.FieldsArray.append(cell_cur)
		#Клетка 18 - 18 корпус
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 18
		cell_cur.color = "orange"
		cell_cur.name = "18 корпус"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 19 - 35 корпус
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 19
		cell_cur.color = "orange"
		cell_cur.name = "35 корпус"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 20 - Стояночка
		cell_cur = Field()
		cell_cur.name = "Стояночка"
		cell_cur.field_type = 9
		cell_cur.field_number = 20
		self.FieldsArray.append(cell_cur)
		#Клетка 21 - АТБ
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 21
		cell_cur.color = "red"
		cell_cur.name = "АТБ"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 22 - Шанс 
		cell_cur = Cell_Chance()
		cell_cur.name = "Шанс"
		cell_cur.field_number = 22
		self.FieldsArray.append(cell_cur)
		#Клетка 23 - Сильпо
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 23
		cell_cur.color = "red"
		cell_cur.name = "Сільпо"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 24 - Фора
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 24
		cell_cur.color = "red"
		cell_cur.name = "Фора"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 25 - Метро Шулявская 
		cell_cur = Cell_buyable_stations()
		cell_cur.field_number = 25
		cell_cur.name = "Метро Шулявська"
		cell_cur.cost_of_cell = 1500
		self.FieldsArray.append(cell_cur)
		#Клетка 26 - Арома Кава
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 26
		cell_cur.color = "yellow"
		cell_cur.name = "Арома Кава"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 27 - Pancake
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 27
		cell_cur.color = "yellow"
		cell_cur.name = "Pancake"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 28 - Сервери ЕКампуса
		cell_cur = Cell_buyable_spec()
		cell_cur.field_number = 28
		cell_cur.name = "Сервери ЕКампуса"
		cell_cur.cost_of_cell = 1500
		self.FieldsArray.append(cell_cur)
		#Клетка 29 - Шаурмечна
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 29
		cell_cur.color = "yellow"
		cell_cur.name = "Шаурмечна"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 30 - Вход у тюрму
		cell_cur = Field()
		cell_cur.name = "До тюрьми!"
		cell_cur.field_type = 5
		cell_cur.field_number = 30
		self.FieldsArray.append(cell_cur)
		#Клетка 31 - Поляна
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 31
		cell_cur.color = "green"
		cell_cur.name = "Поляна"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 32 - Парк КПІ
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 32
		cell_cur.color = "green"
		cell_cur.name = "Парк КПІ"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 33 - Шанс 
		cell_cur = Cell_Chance()
		cell_cur.name = "Шанс"
		cell_cur.field_number = 33
		self.FieldsArray.append(cell_cur)
		#Клетка 34 - Сосновий парк
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 34
		cell_cur.color = "green"
		cell_cur.name = "Сосновий парк"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 35 - Метро Політехнічний інститут 
		cell_cur = Cell_buyable_stations()
		cell_cur.field_number = 35
		cell_cur.name = "Метро Політехнічний інститут "
		cell_cur.cost_of_cell = 1500
		self.FieldsArray.append(cell_cur)
		#Клетка 36 - Шанс
		cell_cur = Cell_Chance()
		cell_cur.name = "Шанс"
		cell_cur.field_number = 36
		self.FieldsArray.append(cell_cur)
		#Клетка 37 - Перший корпус
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 37
		cell_cur.color = "blue"
		cell_cur.name = "Перший корпус"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		#Клетка 38 - Надподаток
		cell_cur = Field()
		cell_cur.name = "Надподаток"
		cell_cur.field_type = 8
		cell_cur.field_number = 38
		self.FieldsArray.append(cell_cur)
		#Клетка 39 - Бібліотека
		cell_cur = Cell_buyable_color()
		cell_cur.field_number = 39
		cell_cur.color = "blue"
		cell_cur.name = "Бібліотека"
		cell_cur.houses_cost = 1100 
		cell_cur.cost_of_cell = 1600
		cell_cur.base_arend = 600
		self.FieldsArray.append(cell_cur)
		
	def PrintFields(self):
		for i in range(0, 40):
			print(self.FieldsArray[i].field_number, "   ", self.FieldsArray[i].name)

	def GameStart(self):
		self.CreatePlayers()
		self.CreateFields()
		counter = -1
		while True:
			counter = (counter+1)%self.NumOfPlayers
			if(self.PlayersArray[counter].alive == 1):
				self.Turn(self.PlayersArray[counter])
				while self.PlayersArray[counter].double:
					self.Turn(self.PlayersArray[counter])

	def Turn(self, Player):
		print("\nХід ", Player.playernumber, "-го гравця, ", Player.name)
		print("Гравець стоїть на ", Player.current_field," полі, типу '", self.FieldsTypes[self.FieldsArray[Player.current_field].field_type], "', під назвою '", self.FieldsArray[Player.current_field].name, "'")
		if ((self.FieldsArray[Player.current_field].field_type>=1 and self.FieldsArray[Player.current_field].field_type<=3) and self.FieldsArray[Player.current_field].owner != None):
			print("Власником цього поля є ", self.FieldsArray[Player.current_field].owner.name)
		print("Грошики: ", Player.money)
		print("У гравця є такі поля: ", Player.owned_fields)
		if self.FieldsArray[Player.current_field].field_type:
			print("Ваші дії -------------------------------")

		field = self.FieldsArray[Player.current_field].field_type
		match field:
			case 0:
				self.ThrowDice(Player)
			case 1:
				if self.FieldsArray[Player.current_field].owner == None :
					if int(input("Купляємо? (1/0):   ")):
						#BUY
						if(Player.buy_newfield(self.FieldsArray[Player.current_field].cost_of_cell,Player.current_field)==1):
							self.FieldsArray[Player.current_field].owner=Player
						print("-------------------------------")
						self.ThrowDice(Player)
					else:
						#AUKCION
						if(Player.auction(self.FieldsArray[Player.current_field].cost_of_cell,Player.current_field)==1):
							self.FieldsArray[Player.current_field].owner = Player
						print("-------------------------------")
						self.ThrowDice(Player)
				elif self.FieldsArray[Player.current_field].owner == Player:
					#YOUR FIELD
					print("Ви потрапили на власне поле з ", self.FieldsArray[Player.current_field].houses, "будівлями."
						"\nНова будівля коштуватиме: ", self.FieldsArray[Player.current_field].houses_cost)
					if int(input("Бажаєте придбати будівлю? (1/0):   ")):
						Player.money -= self.FieldsArray[Player.current_field].houses_cost
						self.FieldsArray[Player.current_field].houses += 1
					print("-------------------------------")
					self.ThrowDice(Player)
				else:
					# NALOG (num of houses in ownership)
					Player.tax(self.FieldsArray[Player.current_field].cost(),
							   self.FieldsArray[Player.current_field].owner)
					print("-------------------------------")
					self.ThrowDice(Player)
			case 2:
				if self.FieldsArray[Player.current_field].owner == None:
					if int(input("Купляємо? (1/0):   ")):
						#BUY
						if (Player.buy_newfield(self.FieldsArray[Player.current_field].cost_of_cell,Player.current_field) == 1):
							self.FieldsArray[Player.current_field].owner = Player
							Player.stations += 1
						print("-------------------------------")
						self.ThrowDice(Player)
					else:
						#AUKCION
						if (Player.auction(self.FieldsArray[Player.current_field].cost_of_cell,Player.current_field) == 1):
							self.FieldsArray[Player.current_field].owner = Player
						print("-------------------------------")
						self.ThrowDice(Player)
				elif self.FieldsArray[Player.current_field].owner == Player:
					#YOUR FIELD
					print("Ви потрапили на власне поле, у вас ", Player.stations, "станцій.")
					print("-------------------------------")
					self.ThrowDice(Player)
				else:
					#NALOG(num of stations in ownership)
					Player.tax(self.FieldsArray[Player.current_field].cost(Player.stations), self.FieldsArray[Player.current_field].owner)
					print("-------------------------------")
					self.ThrowDice(Player)
			case 3:
				if self.FieldsArray[Player.current_field].owner == None:
					if int(input("Купляємо? (1/0):   ")):
						#BUY
						if (Player.buy_newfield(self.FieldsArray[Player.current_field].cost_of_cell,Player.current_field) == 1):
							self.FieldsArray[Player.current_field].owner = Player
							Player.specials += 1
						print("-------------------------------")
						self.ThrowDice(Player)
					else:
						#AUKCION
						if (Player.auction(self.FieldsArray[Player.current_field].cost_of_cell,Player.current_field) == 1):
							self.FieldsArray[Player.current_field].owner = Player
						print("-------------------------------")
						self.ThrowDice(Player)
				elif self.FieldsArray[Player.current_field].owner == Player:
					#YOUR FIELD
					print("Ви потрапили на власне поле, у вас ", Player.specials, "спеціальних полів.")
					print("-------------------------------")
					self.ThrowDice(Player)
				else:
					#NALOG(num of fields in ownership)
					Player.tax(self.FieldsArray[Player.current_field].cost(Player.specials), self.FieldsArray[Player.current_field].owner)
					print("-------------------------------")
					self.ThrowDice(Player)
			case 4:
				Player.money_deposit(self.FieldsArray[Player.current_field].chance())
				print("-------------------------------")
				self.ThrowDice(Player)
			case 5:
				Player.current_field = 10
				Player.prisoner = 1
				print("Щасливої прогулянки до в'язниці!")
				print("-------------------------------")
			case 6:
				if Player.prisoner:
					Player.prisoner = 0
					for i in range(3):
						A = random.randint(1, 6)
						B = random.randint(1, 6)
						dice = A + B
						print("Ваши кубики: ", A, " + ", B, " = ", dice)
						if A==B:
							print("Ви вийшли завчасно і робите наступний крок")
							print("-------------------------------")
							self.ThrowDice(Player)
							return
					print("Пропуск кроку")
				else:
					print("-------------------------------")
					self.ThrowDice(Player)
			case 7:
				print("Ви сплачуєте 2000 як податок")
				Player.money_withdraw(2000)
				print("-------------------------------")
				self.ThrowDice(Player)
			case 8:
				print("Ви сплачуєте 4000 як надподаток")
				Player.money_withdraw(4000)
				print("-------------------------------")
				self.ThrowDice(Player)
			case 9:
				if Player.waiting == 0:
					Player.waiting = 1
					print("Пропуск кроку")
				else:
					Player.waiting = 0
					print("-------------------------------")
					self.ThrowDice(Player)


	def ThrowDice(self, Player):
		A = random.randint(1, 6)
		B = random.randint(1, 6)
		dice =  A + B
		print("Ваши кубики: ", A, " + ", B, " = ", dice)
		if Player.current_field + dice >= self.NumOfFields:
			Player.money_deposit(2000)
		if A == B:
			Player.double = 1
		else:
			Player.double = 0
		Player.nextfield(dice)
		print ("Гравець", Player.name, "зараз на", Player.current_field, "полі")


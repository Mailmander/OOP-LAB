from cgi import FieldStorage

from Iterator_Pattern import Iterator
#from Iterator_Pattern import Iter_Type_Field
#from Iterator_Pattern import Iter_Name
#from Iterator_Pattern import Iter_Plan

from Player_class import Player
from Interface import GamePrint
from Statistics import Stats
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


	def CreatePlayers(self):
		self.NumOfPlayers = GamePrint.Numberofplayers()
		for i in range(self.NumOfPlayers):
			self.PlayersArray.append(Player(i))
		return

	def CreateFields(self):
		# Клетка 0 - старт
		cell_cur = Field()
		cell_cur.name = "ДЕКАНАТ"
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
		self.death_check = 0
		while True:
			counter=counter+1
			if (counter == self.NumOfPlayers):
				counter = 0
				self.death_check = 0

			if (self.PlayersArray[counter].alive == 0):
				self.death_check+=1
				if self.death_check == self.NumOfPlayers-1:
					# ALL DEAAAAAAD, END OF GAME
					GamePrint.end_message(winner)
					Stats.Stat_Time(self.PlayersArray)
					break

			elif(self.PlayersArray[counter].alive == 1):
				winner = self.PlayersArray[counter].name
				Menu_result = self.Menu(self.PlayersArray[counter])
				if Menu_result == -1:
					break

				#self.Turn(self.PlayersArray[counter])

	def Menu(self, Player):
		answer = GamePrint.Menu_Main()
		match answer:
			case 1:
				self.Turn(Player)
				while Player.double:
					self.Turn(Player)

			case 2:
				iterator = Iterator(self.FieldsArray, self.PlayersArray, self.NumOfPlayers)
				sub_iterator = iterator.decise(Player)
				sub_iterator.search()


			case 3:
				Stats.Changestat(self,Player)

			case 4:
				GamePrint.Menu_end()
				return -1

	def Turn(self, Player):

		GamePrint.StartPrint(self, Player)  # previous version|      GamePrint.StartPrint(self, Player)

		type_of_field = self.FieldsArray[Player.current_field].field_type
		match type_of_field:
			case 0:
				pass
			case 1:
				self.FieldsArray[Player.current_field].action(Player, self.FieldsArray[Player.current_field], self.PlayersArray)
			case 2:
				self.FieldsArray[Player.current_field].action(Player, self.FieldsArray[Player.current_field], self.PlayersArray)
			case 3:
				self.FieldsArray[Player.current_field].action(Player, self.FieldsArray[Player.current_field], self.PlayersArray)
			case 4:
				self.FieldsArray[Player.current_field].action(Player, self.FieldsArray[Player.current_field].chance())
			case 5:
				self.FieldsArray[Player.current_field].action(Player)
			case 6:
				self.FieldsArray[Player.current_field].action(Player)
			case 7:
				self.FieldsArray[Player.current_field].action(Player)
			case 8:
				self.FieldsArray[Player.current_field].action(Player)
			case 9:
				self.FieldsArray[Player.current_field].action(Player)

		self.ThrowDice(Player)


	def ThrowDice(self, Player):
		if Player.waiting or Player.prisoner:
			return
		A = random.randint(1, 6)
		B = random.randint(1, 6)
		dice =  A + B
		GamePrint.nextstep_dice(A,B,dice)
		if Player.current_field + dice >= self.NumOfFields:
			Player.money_deposit(2000)
		if A == B:
			Player.double = 1
		else:
			Player.double = 0
		Player.nextfield(dice)
		GamePrint.current_field(Player)


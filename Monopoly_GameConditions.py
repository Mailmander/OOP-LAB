from Player_class import Player
import random

class GameConditions():

	NumOfFields = 40
	PlayersArray = []
	FieldsArray = []

	def CreatePlayers(self):
		self.NumOfPlayers = int(input("Введіть к-ть гравців.\n"))
		for i in range(self.NumOfPlayers):
			self.PlayersArray.append(Player(i))
		return

	def CreateFields(self):
		pass

	def GameStart(self):
		self.CreatePlayers()
		self.CreateFields()
		counter = -1
		while True:
			counter = (counter+1)%self.NumOfPlayers
			self.Turn(self.PlayersArray[counter])
			while Player.extra_turn:
				self.Turn(self.PlayersArray[counter])



	def Turn(self, Player):
		field = self.FieldsArray[Player.current_field].field_type

		match field:
			case "0":
				self.ThrowDice(Player)
			case "1":
				if self.FieldsArray[Player.current_field].owner != None:
					NALOG
				else:
					if int(input("Купляємо? (1/0)")):
						BUY
					else:
						AUKCION
			case "2":
				if self.FieldsArray[Player.current_field].owner != None:
					NALOG(num of stations in ownership)
				else:
					if int(input("Купляємо? (1/0)")):
						BUY
					else:
						AUKCION
			case "3":
				if self.FieldsArray[Player.current_field].owner != None:
					NALOG(num of fields in ownership)
				else:
					if int(input("Купляємо? (1/0)")):
						BUY
					else:
						AUKCION
			case "4":
				Player.money += self.FieldsArray[Player.current_field].chance()
			case "5":
				Player.current_field = 10
			case "6":

			case "7":
			case "8":
			case "9":


	def ThrowDice(self, Player):
		A = random.randint(1, 6)
		B = random.randint(1, 6)
		dice =  A + B
		if Player.current_field + dice >= self.NumOfFields:
			Player.money += 2000
		if A == B:
			Player.extra_turn = 1
		else:
			Player.extra_turn = 0
		Player.current_field = (Player.current_field + dice) % self.NumOfFields



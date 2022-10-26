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
					NALOG (num of houses in ownership)
					self.ThrowDice(Player)
				else:
					if int(input("Купляємо? (1/0)")):
						BUY
						self.ThrowDice(Player)
					else:
						AUKCION
						self.ThrowDice(Player)
			case "2":
				if self.FieldsArray[Player.current_field].owner != None:
					NALOG(num of stations in ownership)
					self.ThrowDice(Player)
				else:
					if int(input("Купляємо? (1/0)")):
						BUY
						self.ThrowDice(Player)
					else:
						AUKCION
						self.ThrowDice(Player)
			case "3":
				if self.FieldsArray[Player.current_field].owner != None:
					NALOG(num of fields in ownership)
					self.ThrowDice(Player)
				else:
					if int(input("Купляємо? (1/0)")):
						BUY
						self.ThrowDice(Player)
					else:
						AUKCION
						self.ThrowDice(Player)
			case "4":
				Player.money += self.FieldsArray[Player.current_field].chance()
				self.ThrowDice(Player)
			case "5":
				Player.current_field = 10
				Player.prisoner = 1
			case "6":
				if Player.prisoner:
					for i in range(3):
						A = random.randint(1, 6)
						B = random.randint(1, 6)
						dice = A + B
						print("Ваши кубики: ", A, " + ", B, " = ", dice)
						if A==B:
							self.ThrowDice(Player)
							break
					Player.prisoner = 0
				else:
					self.ThrowDice(Player)
			case "7":
				Player.money -= 4000
				self.ThrowDice(Player)
			case "8":
				Player.money -= 2000
				self.ThrowDice(Player)
			case "9":
				if Player.waiting == 0:
					Player.waiting = 1
				else:
					Player.waiting = 0
					self.ThrowDice(Player)





	def ThrowDice(self, Player):
		A = random.randint(1, 6)
		B = random.randint(1, 6)
		dice =  A + B
		print("Ваши кубики: ", A, " + ", B, " = ", dice)
		if Player.current_field + dice >= self.NumOfFields:
			Player.money += 2000
		if A == B:
			Player.double = 1
		else:
			Player.double = 0
		Player.current_field = (Player.current_field + dice) % self.NumOfFields



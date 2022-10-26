from Player_class import Player
import random

class GameConditions():

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
			self.Step(self.PlayersArray[counter])

	def Step(player):
		dice = random.randint(1, 6) + random.randint(1, 6)


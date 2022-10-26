from Player_class import Player

class GameConditions():

	PlayersArray = []

	def CreatePlayers(self):
		self.NumOfPlayers = int(input("Введіть к-ть гравців.\n"))
		for i in range(self.NumOfPlayers):
			self.PlayersArray.append(Player(i))
		return


	def GameStart(self):
		self.CreatePlayers()

	def Step(player):
		return

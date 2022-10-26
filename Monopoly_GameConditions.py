from Player_class import Player

class GameConditions():

	PlayersArray = []

	def CreatePlayers(self):
		self.NumOfPlayers = int(input("Enter number of player.\n"))
		for i in range(self.NumOfPlayers):
			self.PlayersArray[i] = Player(i)
#			print(self.PlayersArray[i].name)
#		print(self.PlayersArray[0].name)
		return#


	#def GameStart(self):
	#	self.CreatePlayers()

	def Step(player):
		return

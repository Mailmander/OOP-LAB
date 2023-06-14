import time
from cgi import FieldStorage
from tkinter import *
from Iterator_Pattern import Iterator
#from Iterator_Pattern import Iter_Type_Field
#from Iterator_Pattern import Iter_Name
#from Iterator_Pattern import Iter_Plan
from Player_class import Player
from Interface import GamePrint
import codecs
import io

from Statistics import Stats
import random
from class_games import Field
from class_games import Cell_buyable
from class_games import Cell_buyable_color
from class_games import Cell_buyable_stations
from class_games import Cell_buyable_spec
from class_games import Cell_Chance
from class_games import Cell_Prizon
from class_games import Cell_Prizon_Enter
from class_games import Cell_Tax
from class_games import Cell_Super_Tax
from class_games import Cell_Waiter



class GameConditions():

	NumOfFields = 40
	PlayersArray = []
	FieldsArray = []
	counter = -1
	winner= "---"
	winnernum = -1
	NumOfPlayers = 2

	def CreateFields(self):
		f = open('d:\stat_3.txt', encoding='utf-8')
		for line in f:
			stroka = line.split()
			type_cell = int(stroka[0])
			match type_cell:
				case 0:
					c = Cell_buyable()
					c.field_number = 0
					c.name = "Старт"
				case 1: 
					c = Cell_buyable_color()
					c.name = stroka[2]
					c.color = stroka[3]
					c.houses_cost = int(stroka[4])
					c.cost_of_cell = int(stroka[5])
					c.base_arend = int(stroka[6])
				case 2: 
					c = Cell_buyable_stations()
					c.name = stroka[2]
					c.cost_of_cell = int(stroka[3])
				case 3: 
					c = Cell_buyable_spec()
					c.name = stroka[2]
					c.cost_of_cell = int(stroka[3])
				case 4: 
					c = Cell_Chance()
					c.name = "Шанс"
				case 5: 
					c = Cell_Prizon_Enter()
					c.name = "Тюрьма (Прохід)"
				case 6: 
					c = Cell_Prizon()
					c.name = "Тюрьма"
				case 7: 
					c = Cell_Tax()
					c.name = "Податок"
				case 8: 
					c = Cell_Super_Tax
					c.name = "Надподаток"
				case 9:
					c = Cell_Waiter
					c.name = "Стоянка"
			self.FieldsArray.append(c)
			c.field_number = stroka[1]
				
	def PrintFields(self):
		for i in range(len(self.FieldsArray)):
			print(self.FieldsArray[i].field_number, "   ", self.FieldsArray[i].name)




	def GameContinue(self):
		while True:
			self.counter=self.counter+1
			if (self.counter == self.NumOfPlayers):
				self.counter = 0
				self.death_check = 0

			if (self.PlayersArray[self.counter].alive == 0):
				self.death_check+=1
				if self.death_check == self.NumOfPlayers-1:
					# ALL DEAAAAAAD, END OF GAME
					GamePrint.end_message(self.winner)
					self.winner="-_-_-_-"
					Stats.Stat_Time(self.PlayersArray)
					break

			elif(self.PlayersArray[self.counter].alive == 1):
				self.winner = self.PlayersArray[self.counter].name
				self.winnernum=self.counter
				Menu_result = -1 #self.Menu(self.PlayersArray[self.counter])
				self.Turn(self.PlayersArray[self.counter])
				if Menu_result == -1:
					break



				#self.Turn(self.PlayersArray[counter])
	def GameStart(self):
		self.Graphics()



	def Graphics(self):
		self.death_check = 0
		root = Tk()
		choice = IntVar()
		logo = PhotoImage(file='logo3.png')
		root.iconphoto(False, logo)

		root["bg"] = '#fafafa'
		root.title = 'Monopoly'
		root.wm_attributes('-alpha', 1)
		root.geometry('1200x1000')

		root.resizable(width=True, height=True)

		#canvas = Canvas(root, height=1200, width=1000)
		#canvas.pack()

		frame = Frame(root, bg='grey')
		frame.place(relx=0, rely=0, relwidth=0.15, relheight=0.5)


		windselection = Frame(root, bg='grey')
		windselection.place(relx=0.2, rely=0, relwidth=0.15, relheight=0.30)



		field = Frame(root, bg='white')
		field.place(relx=0.3, rely=0.3, relwidth=0.65, relheight=0.65)
		clit = [None] * 40

		photo = PhotoImage(file="./logo4.png")
		playerphot = PhotoImage(file="./logo5.png")
		jailph = PhotoImage(file="./jail.png")
		lavka = PhotoImage(file="./lavka.png")
		dekanat = PhotoImage(file="./dekan.png")
		obsh = PhotoImage(file="./obsh.png")
		mag = PhotoImage(file="./magaz.png")
		tpkorp = PhotoImage(file="./35.png")
		cafe = PhotoImage(file="./cafe.png")
		park = PhotoImage(file="./park.png")
		ark = PhotoImage(file="./ark.png")
		bibl = PhotoImage(file="./bibl.png")
		firstkorp = PhotoImage(file="./firstkorp.png")
		metro = PhotoImage(file="./metro.png")
		chance = PhotoImage(file="./chance.png")
		nalog = PhotoImage(file="./nalog.png")
		parking = PhotoImage(file="./parking.png")
		telec = PhotoImage(file="./kpitelec.png")
		for i in range(40):
			print(i)
			clit[i] = Label(field, image=photo, highlightthickness=1, width=50, height=50, bg='black')
			if (i == 0 ):
				clit[i].config(image=dekanat,bg="white")
			if(i==1 or i==3 ):
				clit[i].config(image=lavka,bg="purple")
			if (i == 6 or i == 8 or i == 9):
				clit[i].config(image=ark,bg="lightblue")
			if (i == 11 or i == 13 or i == 14):
				clit[i].config(image=obsh,bg="lightpink")
			if (i == 16 or i == 18 or i == 19):
				clit[i].config(image=tpkorp,bg="orange")
			if (i == 21 or i == 23 or i == 24):
				clit[i].config(image=mag,bg="red")
			if (i == 26 or i == 27 or i == 29):
				clit[i].config(image=cafe,bg="yellow")
			if (i == 31 or i == 32 or i == 34):
				clit[i].config(image=park,bg="darkgreen")
			if (i == 37 ):
				clit[i].config(image=firstkorp,bg="darkblue")
			if (i == 39):
				clit[i].config(image=bibl,bg="darkblue")
			if (i == 5 or i == 15 or i == 25 or i == 35):
				clit[i].config(image=metro,bg="black")
			if (i == 4 or i == 7 or i == 17 or i == 22 or i == 33 or i == 36):
				clit[i].config(image=chance, bg="black")
			if (i == 2 or i == 38):
				clit[i].config(image=nalog, bg="black")
			if (i == 10):
				clit[i].config(image=jailph,bg="green")
			if (i == 30):
				clit[i].config(image=jailph,bg="darkred")
			if (i == 20):
				clit[i].config(image=parking, bg="black")
			if (i == 12 or i == 28):
				clit[i].config(image=telec, bg="black")

		clitpl = [None] * 4
		colors = ['green', 'yellow', 'blue', 'red']
		for i in range(4):
			clitpl[i] = Label(field, text=i + 1, bg=colors[i])

		def winner():
			btncont.destroy()
			winsign = Label(field,text="YAAAAAAYYYY AND THE WINNER IS:").grid(row=5,column=5)
			winsign2 = Label(field,text=self.PlayersArray[self.winnernum].name).grid(row=5,column=6)
		def delete_dead():
			for i in range(self.NumOfPlayers):
				if(self.PlayersArray[i].alive!=1):
					clitpl[i].configure(text='dead',bg='black')
		def create_fields():
			field.config(bg="grey")
			for i in range(40):

				if (i >= 40):
					break
				if (i < 10):
					print(i)
					clit[i].grid(row=0, column=i)
				if (i < 20 and i >= 10):
					print(i)
					clit[i].grid(row=i - 10, column=10)
				if (i < 30 and i >= 20):
					print(i)
					clit[i].grid(row=10, column=10 - (i % 10))
				if (i < 40 and i >= 30):
					print(i)
					clit[i].grid(row=40 - i, column=0)

			btncont.place(relx=0.15, rely=0.65)
			#self.CreatePlayers()
			self.CreateFields()
		def namechoose():
			sign.config(text="Choose player names:")
			selectplayer.destroy()
			selectplayer2.destroy()
			selectplayer3.destroy()
			selectplayer4.destroy()
			self.NumOfPlayers = choice.get()
			for i in range(self.NumOfPlayers):
				namer[i].pack()

			nameselected.pack()

		def select_menu():
			sign.pack()
			selectplayer.pack()
			selectplayer2.pack()
			selectplayer3.pack()
			selectplayer4.pack()
		def create_points():
			for i in range(self.NumOfPlayers):
				playername=namer[i].get()
				self.PlayersArray.append(Player(i,playername))
				print(playername)
			windselection.destroy()

			# self.NumOfPlayers = GamePrint.Numberofplayers() - Удалить
			#self.CreatePlayers()
			#for i in range(self.NumOfPlayers):
			#	self.PlayersArray.append(Player(i))
			for i in range(self.NumOfPlayers):
				clitpl[i].grid(row=0, column=0)




		def game_start():
			print('Game started')
			btnstart.destroy()
			create_fields()
			select_menu()


		def game_leave():
			print("Game stopped!")
			exit()


		def returns():
			btnstatsign.config(text='')
			if(self.winner=="-_-_-_-"):
				winner()

			delete_dead()
			self.GameContinue()
			player_menu()
			print("Next")

		def game_settings():
			print("NO SETTINGS!")
			return 2

		def column_calc(place):
			if(place <= 10):
				return place
			elif(place > 10 and place <= 20):
				return 10
			elif (place > 20 and place <= 30):
				return 10 - place%20
			elif (place > 30 and place <= 40):
				return 0
		#def pattern_print():
		#	print()
		def row_calc(place):
			if (place <= 10):
				return 0
			elif (place > 10 and place <= 20):
				return place - 10
			elif (place > 20 and place <= 30):
				return 10
			elif (place > 30 and place <= 40):
				return 40 - place
		def player_menu():
			clitpl[self.counter].grid(row=row_calc(self.PlayersArray[self.counter].current_field),column=column_calc(self.PlayersArray[self.counter].current_field))
			playerinfo.grid(row =0 ,column=13)
			playerinfo.config(text=self.PlayersArray[self.counter].name)
			playerinfos[0].config(text='Player№:')
			playerinfos[1].config(text=self.counter+1)
			playerinfos[2].config(text='Money:')
			playerinfos[3].config(text=self.PlayersArray[self.counter].money)
			playerinfos[4].config(text="Current field:")
			playerinfos[5].config(text=self.PlayersArray[self.counter].current_field)
			playerinfos[6].config(text=self.FieldsArray[self.PlayersArray[self.counter].current_field].name)
			fields = ', '.join(map(str,self.PlayersArray[self.counter].owned_fields))
			playerinfos[7].config(text="Owned fields:")
			playerinfos[8].config(text=fields)
			for i in range(9):
				playerinfos[i].grid(row=1+i,column=13)
			btnstat.grid(row=10,column=13)
		def statistic():
			Stats.Changestat(self,self.PlayersArray[self.counter])
			btnstatsign.config(text='Changed')
			btnstatsign.grid(row=11,column=13)




		title = Label(frame, text='Menu', bg='gray', font=40)
		title.pack()
		playerinfo = Label(field, text='Player info', bg='gray', font=40)
		playerinfos = [None] * 9
		for i in range(9):
			playerinfos[i]= Label(field, text='Player info', bg='gray', font=40)
		btnstart = Button(frame, text="Start game", bg='green', command=game_start)
		btnstart.place(relx=0.15, rely=0.25)
		btnsettings = Button(frame, text="Settings", bg='yellow', command=game_settings)
		btnsettings.place(relx=0.15, rely=0.45)
		btnleave = Button(frame, text="Leave game", bg='red', command=game_leave)
		btnleave.place(relx=0.15, rely=0.65)
		btncont = Button(field, text="Next turn", bg='orange', command=returns)
		sign = Label(windselection, text='Select number of players:', bg='grey', font=40)
		selectplayer = Radiobutton(windselection, text="1", variable=choice, value=1, command=namechoose)
		selectplayer2 = Radiobutton(windselection, text="2", variable=choice, value=2, command=namechoose)
		selectplayer3 = Radiobutton(windselection, text="3", variable=choice, value=3, command=namechoose)
		selectplayer4 = Radiobutton(windselection, text="4", variable=choice, value=4, command=namechoose)
		nameselected = Button(windselection, text="Submit", bg='green', command=create_points)
		namer = [None] * 4
		for i in range(4):
			namer[i]= Entry(windselection)
		btnstat = Button(field, text="Turn On/Off Statistics", bg='orange', command=statistic)
		btnstatsign = Label(field, text='Changed', bg='gray', font=40)


		root.mainloop()

	def Menu(self, Player):
		answer = GamePrint.Menu_Main()
		match answer:
			case 1:
				self.Turn(Player)
				while Player.double:
					self.Turn(Player)
				return -1

			case 2:
				iterator = Iterator(self.FieldsArray, self.PlayersArray, self.NumOfPlayers)
				sub_iterator = iterator.decise(Player)
				sub_iterator.search()
				return -1


			case 3:
				Stats.Changestat(self,Player)
				return -1

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


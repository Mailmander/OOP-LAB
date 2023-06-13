from tkinter import *
from Player_class import Player
def Graphics(self):
    root = Tk()
    choice = IntVar()
    logo = PhotoImage(file='logo3.png')
    root.iconphoto(False, logo)

    root["bg"] = '#fafafa'
    root.title = 'Monopoly'
    root.wm_attributes('-alpha', 1)
    root.geometry('1200x1000')

    root.resizable(width=True, height=True)

    # canvas = Canvas(root, height=1200, width=1000)
    # canvas.pack()

    frame = Frame(root, bg='grey')
    frame.place(relx=0, rely=0, relwidth=0.15, relheight=0.5)

    windselection = Frame(root, bg='grey')
    windselection.place(relx=0.2, rely=0, relwidth=0.15, relheight=0.30)

    field = Frame(root, bg='white')
    field.place(relx=0.3, rely=0.3, relwidth=0.65, relheight=0.65)
    clit = [None] * 40

    photo = PhotoImage(file="./logo4.png")
    playerphot = PhotoImage(file="./logo5.png")
    for i in range(40):
        print(i)
        clit[i] = Label(field, image=photo, highlightthickness=1, width=50, height=50, bg='white')

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

        btncont = Button(field, text="Next turn", bg='orange', command=returns)
        btncont.place(relx=0.15, rely=0.65)
        # self.CreatePlayers()
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
            playername = namer[i].get()
            self.PlayersArray.append(Player(i, playername))
            print(playername)
        windselection.destroy()

        # self.NumOfPlayers = GamePrint.Numberofplayers() - Удалить
        # self.CreatePlayers()
        # for i in range(self.NumOfPlayers):
        #	self.PlayersArray.append(Player(i))
        clitpl = [None] * 4
        colors = ['green', 'yellow', 'blue', 'red']
        for i in range(self.NumOfPlayers):
            clitpl[i] = Label(field, text=i + 1, bg=colors[i])
            clitpl[i].grid(row=0, column=i)

    def game_start():
        print('Game started')
        btnstart.destroy()
        create_fields()
        select_menu()
        print('Game ended')

    def game_leave():
        print("Game stopped!")
        exit()

    def returns():
        self.GameContinue()
        print("Next")

    def game_settings():
        print("Game settings!")
        return 2

    title = Label(frame, text='Menu', bg='gray', font=40)
    title.pack()
    btnstart = Button(frame, text="Start game", bg='green', command=game_start)
    btnstart.place(relx=0.15, rely=0.25)
    btnsettings = Button(frame, text="Settings", bg='yellow', command=game_settings)
    btnsettings.place(relx=0.15, rely=0.45)
    btnleave = Button(frame, text="Leave game", bg='red', command=game_leave)
    btnleave.place(relx=0.15, rely=0.65)

    sign = Label(windselection, text='Select number of players:', bg='grey', font=40)
    selectplayer = Radiobutton(windselection, text="1", variable=choice, value=1, command=namechoose)
    selectplayer2 = Radiobutton(windselection, text="2", variable=choice, value=2, command=namechoose)
    selectplayer3 = Radiobutton(windselection, text="3", variable=choice, value=3, command=namechoose)
    selectplayer4 = Radiobutton(windselection, text="4", variable=choice, value=4, command=namechoose)
    nameselected = Button(windselection, text="Submit", bg='green', command=create_points)
    namer = [None] * 4
    for i in range(4):
        namer[i] = Entry(windselection)

    root.mainloop()
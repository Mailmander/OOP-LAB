from Monopoly_GameConditions import GameConditions
from tkinter import *
root = Tk()




def game_start():
    print("Game started!")
    Monopoly = GameConditions()
    Monopoly.GameStart()

def game_leave():
    print("Game stopped!")
def game_settings():
    print("Game settings!")
root["bg"] = '#fafafa'
root.title = 'Monopoly'
root.wm_attributes('-alpha',1)
root.geometry('300x250')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=600, width=500)
canvas.pack()

frame = Frame(root, bg='black')
frame.place(relx=0.15,rely=0.15,relwidth=0.7,relheight=0.7)

title = Label(frame,text='Menu',bg='gray',font=40)
title.pack()
btnstart = Button(frame,text="Start game",bg='green',command=game_start)
btnstart.place(relx=0.35,rely=0.25)
btnsettings = Button(frame,text="Settings",bg='yellow',command=game_settings)
btnsettings.place(relx=0.35,rely=0.45)
btnleave = Button(frame,text="Leave game",bg='red',command=game_leave)
btnleave.place(relx=0.35,rely=0.65)

root.mainloop()
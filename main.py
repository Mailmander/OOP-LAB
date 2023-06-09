from tkinter import *
from Monopoly_GameConditions import GameConditions
Monopoly = GameConditions()
Monopoly.GameStart()
# class screen():
#     @staticmethod
#     def menu():
#         root = Tk()
#
#         logo = PhotoImage(file='logo3.png')
#         root.iconphoto(False, logo)
#         def game_start():
#             print('Game started')
#             btnstart.destroy()
#             Monopoly.GameStart()
#             print('Game ended')
#
#
#
#         def game_leave():
#             print("Game stopped!")
#             exit()
#         def returns():
#             Monopoly.GameContinue()
#
#         def game_settings():
#             print("Game settings!")
#             return 2
#
#         root["bg"] = '#fafafa'
#         root.title = 'Monopoly'
#         root.wm_attributes('-alpha', 1)
#         root.geometry('1200x1000')
#
#         root.resizable(width=True, height=True)
#
#         canvas = Canvas(root, height=800, width=600)
#         canvas.pack()
#
#         frame = Frame(root, bg='grey')
#         frame.place(relx=0, rely=0, relwidth=0.15, relheight=0.5)
#
#         title = Label(frame, text='Menu', bg='gray', font=40)
#         title.pack()
#         btnstart = Button(frame, text="Start game", bg='green', command=game_start)
#         btnstart.place(relx=0.15, rely=0.25)
#         btnsettings = Button(frame, text="Settings", bg='yellow', command=game_settings)
#         btnsettings.place(relx=0.15, rely=0.45)
#         btnleave = Button(frame, text="Leave game", bg='red', command=game_leave)
#         btnleave.place(relx=0.15, rely=0.65)
#         field = Frame(root, bg='grey')
#         field.place(relx=0.3, rely=0.3, relwidth=0.65, relheight=0.65)
#         #clit1 = Label(field, text="|---|",bg='purple')
#         #clit1.image= PhotoImage(file='logo3.png')
#         clit= [None] * 40
#         photo = PhotoImage(file="./logo4.png")
#         for i in range(40):
#             print(i)
#             clit[i] = Label(field,image=photo,highlightthickness=1,width=50,height=50,bg='white')
#
#         clit1 = Label(field,text='1',bg='green')
#         clit2 = Label(field,text='2',bg='yellow')
#         clit3 = Label(field,text='3',bg='red')
#         clit4 = Label(field,text='4',bg='blue')
#
#         for i in range(40):
#
#             if(i>=40):
#                 break
#             if(i<10):
#                 print(i)
#                 clit[i].grid(row=0,column=i)
#             if (i < 20 and i>=10):
#                 print(i)
#                 clit[i].grid(row=i-10, column=10)
#             if (i < 30 and i>=20):
#                 print(i)
#                 clit[i].grid(row=10, column=10-(i%10))
#             if (i < 40 and i>=30):
#                 print(i)
#                 clit[i].grid(row=40-i, column=0)
#
#         clit1.grid(row=0, column=0)
#         clit2.grid(row=0, column=0)
#         clit3.grid(row=0, column=0)
#         clit4.grid(row=0, column=0)
#         btncont = Button(field, text="Next turn", bg='orange', command=returns)
#         btncont.place(relx=0.15, rely=0.65)
#         root.mainloop()
# screen.menu()
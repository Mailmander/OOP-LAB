from Interface import GamePrint
from Player_class import Player
class Stats ():
    PlayerStats=[]
    def AddForPlayers(self,id):
        Stats.PlayerStats.append(id)
        GamePrint.addstat_player(id+1)

    def RemovePlayer(self,id):
        Stats.PlayerStats.remove(id)
        GamePrint.removestat_player(id+1)

    def Subcheck(self,Playerid):
        counter=0
        for i in range(len(Stats.PlayerStats)):
            if(Stats.PlayerStats[counter]==Playerid):
                return 1
            counter=counter+1
        return 0


    def Changestat(self,Player):
        if(Stats.Subcheck(self,Player.playernumber)):
            Stats.RemovePlayer(self,Player.playernumber)
        elif(Stats.Subcheck(self,Player.playernumber)==0):
            Stats.AddForPlayers(self,Player.playernumber)

    @staticmethod
    def Stat_Time(Players):
        for i in range(len(Stats.PlayerStats)):
            Players[Stats.PlayerStats[i]].stats()



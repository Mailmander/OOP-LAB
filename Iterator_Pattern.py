from Interface import GamePrint

class Iterator():

    def __init__(self, fields_array, players_array, NumOfPlayers, map = []):
        self.fields_array = fields_array
        self.players_array = players_array
        self.NumOfPlayers = NumOfPlayers
        self.map = map


    #
    # вивід усіх полів за типом
    # пошук поля/гравця за назвою/ім'ям
    # планувальник маршруту /запланований
    #                       \ випадковий
    #

    def decise(self, Player):
        self.map = GamePrint.Iter_decise(Player)

        match self.map[0]:
            case 1:
                obj = Iter_Type_Field(self.fields_array, self.players_array, self.NumOfPlayers, self.map)
            case 2:
                obj = Iter_Name(self.fields_array, self.players_array, self.NumOfPlayers, self.map)
            case 3:
                obj = Iter_Plan(self.fields_array, self.players_array, self.NumOfPlayers, self.map)
        return obj


class Iter_Type_Field (Iterator):
    def search (self):
        match self.map[2]:
            case 1:
                for i in range(0, 40):
                    field_to_print = self.fields_array[i]
                    if field_to_print.field_type == 1:
                        GamePrint.Iter_print_field(field_to_print)
            case 2:
                for i in range(0, 40):
                    field_to_print = self.fields_array[i]
                    if field_to_print.field_type == 2 or field_to_print.field_type == 3:
                        GamePrint.Iter_print_field(field_to_print)
            case 3:
                for i in range(0, 40):
                    field_to_print = self.fields_array[i]
                    if not(field_to_print.field_type == 1 or field_to_print.field_type == 2 or field_to_print.field_type == 3):
                        GamePrint.Iter_print_field(field_to_print)
            case 4:
                for i in range(0, 40):
                    field_to_print = self.fields_array[i]
                    GamePrint.Iter_print_field(field_to_print)

class Iter_Name (Iterator):
    def search (self):
        match self.map[1]:
            case 1:
                for i in range(0, 40):
                    field_to_print = self.fields_array[i]
                    if self.map[2] == field_to_print.name:
                        GamePrint.Iter_print_field(field_to_print)
            case 2:
                for i in range(0, self.NumOfPlayers):
                    player_to_print = self.players_array[i]
                    if self.map[2] == player_to_print.name:
                        GamePrint.Iter_print_player(player_to_print)

class Iter_Plan (Iterator):
    def search (self):
        length = len(self.map[2])
        for i in range(0, length):
            field_to_print = self.fields_array[int(self.map[2][i])]
            GamePrint.Iter_print_field(field_to_print)

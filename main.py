class TicTacToe:
    def __init__(self):
        self.field = [1, 2, 3,
                      4, 5, 6,
                      7, 8, 9]
        self.gameIsRunning = True

        self.player1 = input("Spieler 1, wie heißt du? ")
        print("Hallo " + self.player1 + " dein Zeichen ist O")
        self.player2 = input("Spieler 2, wie heißt du? ")
        print("Hallo " + self.player2 + " dein Zeichen ist X")

    def start_game(self):
        player_on_move = self.player1
        while self.gameIsRunning:


            print(f"{self.field[0]} {self.field[1]} {self.field[2]}\n"
                  f"{self.field[3]} {self.field[4]} {self.field[5]}\n"
                  f"{self.field[6]} {self.field[7]} {self.field[8]}")

            self.move(player_on_move)

            if player_on_move == self.player1:
                player_on_move = self.player2
            else:
                player_on_move = self.player1

            self.check_winner()

    def move(self, player):
        while True:
            selected_field = input(player + " welches Feld möchtest du wählen? ")
            if (selected_field != "1" and selected_field != "2" and selected_field != "3"
                    and selected_field != "4" and selected_field != "5" and selected_field != "6"
                    and selected_field != "7" and selected_field != "8" and selected_field != "9"):
                print("Bitte wähle eins der Felder! ")
            else:
                break
        if player == self.player1:
            self.field[int(selected_field) - 1] = "O"
        else:
            self.field[int(selected_field) - 1] = "X"

    def check_winner(self):
        player_signs = ["O", "X"]
        for i in player_signs:
            if i == self.field[0] and i == self.field[1] and i == self.field[2]:
                if i == "O":
                    print("Herzlichen Glückwunsch " + self.player1 + ", du hast gewonnen")
                    self.gameIsRunning = False
                else:
                    print("Herzlichen Glückwunsch " + self.player2 + ", du hast gewonnen")
                    self.gameIsRunning = False

            elif i == self.field[3] and i == self.field[4] and i == self.field[5]:
                if i == "O":
                    print("Herzlichen Glückwunsch " + self.player1 + ", du hast gewonnen")
                    self.gameIsRunning = False
                else:
                    print("Herzlichen Glückwunsch " + self.player2 + ", du hast gewonnen")
                    self.gameIsRunning = False

            elif i == self.field[6] and i == self.field[7] and i == self.field[8]:
                if i == "O":
                    print("Herzlichen Glückwunsch " + self.player1 + ", du hast gewonnen")
                    self.gameIsRunning = False
                else:
                    print("Herzlichen Glückwunsch " + self.player2 + ", du hast gewonnen")
                    self.gameIsRunning = False


            elif i == self.field[0] and i == self.field[3] and i == self.field[6]:
                if i == "O":
                    print("Herzlichen Glückwunsch " + self.player1 + ", du hast gewonnen")
                    self.gameIsRunning = False
                else:
                    print("Herzlichen Glückwunsch " + self.player2 + ", du hast gewonnen")
                    self.gameIsRunning = False

            elif i == self.field[1] and i == self.field[4] and i == self.field[7]:
                if i == "O":
                    print("Herzlichen Glückwunsch " + self.player1 + ", du hast gewonnen")
                    self.gameIsRunning = False
                else:
                    print("Herzlichen Glückwunsch " + self.player2 + ", du hast gewonnen")
                    self.gameIsRunning = False

            elif i == self.field[2] and i == self.field[5] and i == self.field[8]:
                if i == "O":
                    print("Herzlichen Glückwunsch " + self.player1 + ", du hast gewonnen")
                    self.gameIsRunning = False
                else:
                    print("Herzlichen Glückwunsch " + self.player2 + ", du hast gewonnen")
                    self.gameIsRunning = False


            elif i == self.field[0] and i == self.field[4] and i == self.field[8]:
                if i == "O":
                    print("Herzlichen Glückwunsch " + self.player1 + ", du hast gewonnen")
                    self.gameIsRunning = False
                else:
                    print("Herzlichen Glückwunsch " + self.player2 + ", du hast gewonnen")
                    self.gameIsRunning = False

            elif i == self.field[2] and i == self.field[4] and i == self.field[6]:
                if i == "O":
                    print("Herzlichen Glückwunsch " + self.player1 + ", du hast gewonnen")
                    self.gameIsRunning = False
                else:
                    print("Herzlichen Glückwunsch " + self.player2 + ", du hast gewonnen")
                    self.gameIsRunning = False



if __name__ == "__main__":
    Game = TicTacToe()
    Game.start_game()

def print_board(board: dict[int, str]):
    print("\n " + board[1] + " | " + board[2] + " | " + board[3])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "\n")
    

class Board:
    def __init__(self) -> None:
        self.current_position = {i: " " for i in range(1, 10)}
        self.current_player = "X"


    def get_legal_squares(self) -> list[int]:
        return [i for i in range(1, 10) if self.current_position[i] == " "]
    

    def check_for_win(self):
        if (self.current_position[1] == self.current_position[2] and self.current_position[1] == self.current_position[3] and self.current_position[1] != ' '):
            return True
        elif (self.current_position[4] == self.current_position[5] and self.current_position[4] == self.current_position[6] and self.current_position[4] != ' '):
            return True
        elif (self.current_position[7] == self.current_position[8] and self.current_position[7] == self.current_position[9] and self.current_position[7] != ' '):
            return True
        elif (self.current_position[1] == self.current_position[4] and self.current_position[1] == self.current_position[7] and self.current_position[1] != ' '):
            return True
        elif (self.current_position[2] == self.current_position[5] and self.current_position[2] == self.current_position[8] and self.current_position[2] != ' '):
            return True
        elif (self.current_position[3] == self.current_position[6] and self.current_position[3] == self.current_position[9] and self.current_position[3] != ' '):
            return True
        elif (self.current_position[1] == self.current_position[5] and self.current_position[1] == self.current_position[9] and self.current_position[1] != ' '):
            return True
        elif (self.current_position[7] == self.current_position[5] and self.current_position[7] == self.current_position[3] and self.current_position[7] != ' '):
            return True
        else:
            return False
        
    def which_player_won(self, symbol):
        if (self.current_position[1] == self.current_position[2] and self.current_position[1] == self.current_position[3] and self.current_position[1] == symbol):
            return True
        elif (self.current_position[4] == self.current_position[5] and self.current_position[4] == self.current_position[6] and self.current_position[4] == symbol):
            return True
        elif (self.current_position[7] == self.current_position[8] and self.current_position[7] == self.current_position[9] and self.current_position[7] == symbol):
            return True
        elif (self.current_position[1] == self.current_position[4] and self.current_position[1] == self.current_position[7] and self.current_position[1] == symbol):
            return True
        elif (self.current_position[2] == self.current_position[5] and self.current_position[2] == self.current_position[8] and self.current_position[2] == symbol):
            return True
        elif (self.current_position[3] == self.current_position[6] and self.current_position[3] == self.current_position[9] and self.current_position[3] == symbol):
            return True
        elif (self.current_position[1] == self.current_position[5] and self.current_position[1] == self.current_position[9] and self.current_position[1] == symbol):
            return True
        elif (self.current_position[7] == self.current_position[5] and self.current_position[7] == self.current_position[3] and self.current_position[7] == symbol):
            return True

        return False
        
    
    def check_for_draw(self):
        for _, symbol in self.current_position.items():
            if symbol == " ":
                return False
        
        return True
    
    
    def add_symbol(self, idx):
        self.current_position[idx] = self.current_player

    
    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    


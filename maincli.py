from board import Board, print_board


def minimax(board: Board, is_max_player):
    if board.check_for_draw():
        return 0
    if board.which_player_won("X"):
        return 1
    if board.which_player_won("O"):
        return -1
    
    if is_max_player:
        value = -999999
        for idx in board.get_legal_squares():
            board.current_position[idx] = "X"
            score = minimax(board, False)
            board.current_position[idx] = " "
            value = max(value, score)
        return value
    elif not is_max_player:
        value = 999999
        for idx in board.get_legal_squares():
            board.current_position[idx] = "O"
            score = minimax(board, True)
            board.current_position[idx] = " "
            value = min(value, score)
        return value


def player_move(board: Board):
    if board.check_for_win() or board.check_for_draw():
        return False
    
    move_idx: str = input("Players turn (X):  ")

    if not move_idx.isnumeric():
        return None
    
    move_idx = int(move_idx)
    
    if not 1 <= int(move_idx) <= 9 or move_idx not in board.get_legal_squares():
        return None
    
    board.current_position[move_idx] = "X"
    return True


def comp_move(board: Board):
    legal_moves_idx = board.get_legal_squares()
    best_score = 999999
    best_move_idx  = 0

    for idx in legal_moves_idx:
        for idx in board.get_legal_squares():
            board.current_position[idx] = "O"
            score = minimax(board, True)
            board.current_position[idx] = " "
            if score < best_score:
                best_score = score
                best_move_idx = idx
            
    print(best_move_idx)
    board.current_position[best_move_idx] = "O"




def main():
    board = Board()

    while 1:
        print_board(board.current_position)
        player_response = player_move(board)
        if player_response is False:
            print("Game over!", board.current_player, "won")
            break
        elif player_response is None:
            print("Please provide a valid index")
            continue

        comp_move(board)


if __name__ == "__main__":
    main()
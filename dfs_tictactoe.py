
def initialize_board():
   return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
   for row in board:
       print("|".join(row))
       print("-" * 5)


def check_win(board):
   # Check rows, columns, and diagonals for a win
   for i in range(3):
       if board[i][0] == board[i][1] == board[i][2] != " " or \
          board[0][i] == board[1][i] == board[2][i] != " ":
           return True
   if board[0][0] == board[1][1] == board[2][2] != " " or \
      board[0][2] == board[1][1] == board[2][0] != " ":
       return True
   return False


def check_tie(board):
   for row in board:
       if " " in row:
           return False
   return True


def get_move(player):
   while True:
       try:
           row = int(input(f"Player {player}, enter your row (0-2): "))
           col = int(input(f"Player {player}, enter your column (0-2): "))
           if row in range(3) and col in range(3):
               return row, col
           else:
               print("Invalid input. Please try again.")
       except ValueError:
           print("Invalid input. Please enter numbers only.")


def play_game():
   board = initialize_board()
   current_player = "X"
   while True:
       print_board(board)
       row, col = get_move(current_player)
       if board[row][col] == " ":
           board[row][col] = current_player
       else:
           print("This spot is already taken. Please choose another spot.")
           continue


       if check_win(board):
           print_board(board)
           print(f"Player {current_player} wins!")
           break
       if check_tie(board):
           print_board(board)
           print("It's a tie!")
           break


       current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
   play_game()


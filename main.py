

#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.

# [1,2,3] + 1 = [1,2,4]
# [1,9,9] + 1 = [2,0,0]
# [9,9] + 1   = [1,0,0]

game_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

my_nums = [1,2,4]

def plus_one(nums):
    output = [1,2,5]

    return output


def print_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def start_game(board):
    name = input("What is your name: ")
    print(f'Welcome to the game: {name}')
    print_board(board)
    is_player_x = True

    for i in range(10):
        val = input("Position: ")

        if is_player_x:
            board[int(val)] = 'X'
        else:
            board[int(val)] = 'O'

        print_board(board)
        if is_player_x:
            if determine_winner(board, 'X'):
                return
        else:
            if determine_winner(board, 'O'):
                return

        is_player_x = not is_player_x


def determine_winner(board, current_player):
    if (board[1] == board[2] == board[3] != ' ') or (board[4] == board[5] == board[6] != ' ') or (board[7] == board[8] == board[9] != ' '):
        print("Horizontal")
        if current_player == 'X':
            print("Player X won")
        else:
            print("Player O won")
        return True
    elif (board[1] == board[4] == board[7] != ' ') or (board[2] == board[5] == board[8] != ' ') or (board[3] == board[6] == board[9] != ' '):
        print("Vertical")
        if current_player == 'X':
            print("Player X won")
        else:
            print("Player O won")
        return True
    elif (board[1] == board[5] == board[9] != ' ') or (board[3] == board[5] == board[7] != ' '):
        print("Diagonal")
        if current_player == 'X':
            print("Player X won")
        else:
            print("Player O won")
        return True
    return False


if __name__ == '__main__':
    # print(board.get(7))
    # start_game(game_board)
    print(plus_one(my_nums))
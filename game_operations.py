import sys
from game_board import *


def terminal_state(board: Board):
    result = board.check_win_state()
    if result == 1:
        print("User has won the game.\n")
        return 1
    elif result == 2:
        print("Computer has won the game.\n")
        return 2

    return 0


def user_move(board: Board) -> None:
    if terminal_state(board):
        return

    is_chain = False

    while True:
        x, y = str(input(
            "Enter the co-ordinates of the cell where you wish to place your ball : ")).strip().split(',')

        x = int(x)
        y = int(y)

        if board.check_boundary_conditions(x, y) and '2' not in board.board[x][y]:
            if board.board[x][y] == '0':
                board.board[x][y] = '1'
            else:
                board.board[x][y] += '1'

            if len(board.board[x][y]) == 3:
                is_chain = True
                board.perform_chain_reaction()

            break

        else:
            print("Please enter the co-ordinates of valid cell.\n")

    if not is_chain:
        board.print_board()

    computer_move(board)


def heuristic_function(board: Board, x: int, y: int, s: str) -> int:
    org_value = board.board[x][y]

    if org_value[0] == s[0]:
        board.board[x][y] += s[0]
    else:
        board.board[x][y] = s[0]

    computer_places = [[i, j] for i in range(board.rows) for j in range(
        board.columns) if '2' in board.board[i][j]]
    user_places = [[i, j] for i in range(board.rows) for j in range(
        board.columns) if '1' in board.board[i][j]]

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    computer_score, user_score = 0, 0

    for i, j in user_places:
        temp = []
        for x, y in directions:
            if board.check_boundary_conditions(i+x, j+y) and '1' not in board.board[i+x][j+y]:
                temp.append(board.board[i+x][j+y])

        if len(temp)==0:
            continue

        temp.sort()
        
        if len(temp[-1]) >= 3:
            computer_score += 0
        elif len(temp[-1]) == 2:
            computer_score += 1
        elif len(temp[-1]) == 1:
            if temp[-1] == '0':
                computer_score += 3
            else:
                computer_score += 2

    for i, j in computer_places:
        temp = []
        for x, y in directions:
            if board.check_boundary_conditions(i+x, j+y) and '2' not in board.board[i+x][j+y]:
                temp.append(board.board[i+x][j+y])

        if len(temp)==0:
            continue

        temp.sort()

        if len(temp[-1]) >= 3:
            user_score += 0
        elif len(temp[-1]) == 2:
            user_score += 1
        elif len(temp[-1]) == 1:
            if temp[-1] == '0':
                user_score += 3
            else:
                user_score += 2

    board.board[x][y] = org_value
    return computer_score-user_score


def min_max_algo(board: Board, turn: int, vis: list) -> list:
    result = board.check_win_state()

    if result == 1:
        return [[-1, -1], -100]
    elif result == 2:
        return [[-1, -1], 100]

    if turn == 2:
        maxi = -1*sys.maxsize
        helper = []
        for i in range(board.rows):
            for j in range(board.columns):
                if '1' not in board.board[i][j]:
                    temp = copy.deepcopy(board)

                    if temp.board[i][j] == '0':
                        temp.board[i][j] = '2'
                    else:
                        temp.board[i][j] += '2'

                    if [2, temp.board] in vis:
                        continue
                    
                    else:
                        vis.append([2, copy.deepcopy(temp.board)])

                    hval=heuristic_function(temp, i, j, '2')
                    if len(temp.board[i][j]) == 3:
                        temp.perform_chain_reaction(is_print=False)

                    rcall = min_max_algo(temp, 1, vis)

                    if rcall[1]+ hval> maxi:
                        maxi = rcall[1]+hval
                        helper = [i, j]

        return [helper, maxi]

    else:
        mini = sys.maxsize
        helper = []
        for i in range(board.rows):
            for j in range(board.columns):
                if '2' not in board.board[i][j]:
                    temp = copy.deepcopy(board)

                    if temp.board[i][j] == '0':
                        temp.board[i][j] = '1'
                    else:
                        temp.board[i][j] += '1'

                    if [1, temp.board] not in vis:
                        continue

                    else:
                        vis.append([1, copy.deepcopy(temp.board)])

                    hval=heuristic_function(temp, i, j, '1')
                    if len(temp.board[i][j]) == 3:
                        temp.perform_chain_reaction(is_print=False)

                    rcall = min_max_algo(temp, 2, vis)

                    if rcall[1]+hval < mini:
                        mini = rcall[1]+hval
                        helper = [i, j]

        return [helper, mini]


def computer_move(board: Board) -> None:
    if terminal_state(board):
        return

    print("Computer's move : ", end='\n')

    is_chain = False
    vis = []
    rcall = min_max_algo(board, 2, vis)
    x, y = rcall[0]
    if board.board[x][y] == '0':
        board.board[x][y] = '2'
    else:
        board.board[x][y] += '2'

    if len(board.board[x][y]) == 3:
        is_chain = True
        board.perform_chain_reaction()

    if not is_chain:
        board.print_board()

    user_move(board)


def start_game(m: int, n: int) -> list:
    board = Board(m, n)
    board.print_board()
    user_move(board)

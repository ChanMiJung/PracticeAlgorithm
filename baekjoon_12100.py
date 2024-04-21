from collections import deque
from copy import deepcopy

N = int(input())

max_value = 0

def left(board):
    for i in range(N):
        cursor = 0
        for j in range(N):
            if board[i][j][0] != 0:
                value, value_sum = board[i][j]
                if abs(cursor - j) > 1:
                    value_sum = True
                board[i][j] = [0, True]

                if board[i][cursor][0] == 0:
                    board[i][cursor] = [value, True]
                elif board[i][cursor][0] == value and board[i][cursor][1] and value_sum:
                    board[i][cursor] = [value*2, False]
                    cursor += 1
                else:
                    cursor += 1
                    board[i][cursor] = [value, True]
    return board

def right(board):
    for i in range(N):
        cursor = N-1
        for j in range(N-1, -1, -1):
            if board[i][j][0] != 0:
                value, value_sum = board[i][j]
                if abs(cursor - j) > 1:
                    value_sum = True
                board[i][j] = [0, True]

                if board[i][cursor][0] == 0:
                    board[i][cursor] = [value, True]
                elif board[i][cursor][0] == value and board[i][cursor][1] and value_sum:
                    board[i][cursor] = [value*2, False]
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = [value, True]
    return board

def up(board):
    for j in range(N):
        cursor = 0
        for i in range(N):
            if board[i][j][0] != 0:
                value, value_sum = board[i][j]
                if abs(cursor - i) > 1:
                    value_sum = True
                board[i][j] = [0, True]

                if board[cursor][j][0] == 0:
                    board[cursor][j] = [value, True]
                elif board[cursor][j][0] == value and board[cursor][j][1] and value_sum:
                    board[cursor][j] = [value*2, False]
                else:
                    cursor += 1
                    board[cursor][j] = [value, True]
    return board

def down(board):
    for j in range(N):
        cursor = N-1
        for i in range(N-1, -1, -1):
            if board[i][j][0] != 0:
                value, value_sum = board[i][j]
                if abs(cursor - i) > 1:
                    value_sum = True
                board[i][j] = [0, True]

                if board[cursor][j][0] == 0:
                    board[cursor][j] = [value, True]
                elif board[cursor][j][0] == value and board[cursor][j][1] and value_sum:
                    board[cursor][j] = [value*2, False]
                else:
                    cursor -= 1
                    board[cursor][j] = [value, True]
    return board

            
def dfs(board, depth):
    global max_value    
    if depth == 5:
        for x in range(N):
            for y in range(N):
                if board[x][y][0] > max_value:
                    max_value = board[x][y][0]
        
        return

    dfs(up(deepcopy(board)), depth+1)
    dfs(down(deepcopy(board)), depth+1)
    dfs(left(deepcopy(board)), depth+1)
    dfs(right(deepcopy(board)), depth+1)

board = [[[v, True] for v in list(map(int, input().split()))] for _ in range(N)]



dfs(deepcopy(board), 0)
print(max_value)
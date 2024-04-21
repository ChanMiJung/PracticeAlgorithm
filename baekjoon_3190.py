from collections import deque
from copy import deepcopy


N = int(input())

K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
move = [list(input().split()) for _ in range(L)]

# 우하좌상 D : +1 L : -1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]





snake = deque()
snake.append([1, 1])

def bfs():
    d = 0
    t = 0

    for m in move:
        while t < int(m[0]):
            # print(snake, t, d)
            x, y = snake[0]
            t += 1
        
            # 벽에 부딪히면 죽음
            if not (0 < x + dx[d] < N+1 and 0 < y + dy[d] < N+1):
                # print("not")
                return t
            # 자기 자신에게 부딪히면 죽음
            if [x + dx[d], y + dy[d]] in snake:
                # print("snake")
                return t

            snake.appendleft([x + dx[d], y + dy[d]])
            # 사과 있다면 먹고 늘어남
            if [x + dx[d], y + dy[d]] in apples:                
                apples.remove([x + dx[d], y + dy[d]])
            else:
                # 그냥 지나감
                snake.pop()
        if m[1] == 'D':
            if d == 3:
                d = 0
            else:    
                d += 1
        else:
            if d == 0:
                d = 3
            else:
                d -= 1
        
    t += 1
    while True:
        # print(snake, t, d)
        x,y = snake[0]
        if not (0 < x + dx[d] < N+1 and 0 < y + dy[d] < N+1):
            return t
        if [x + dx[d], y + dy[d]] in snake:
            return t
        snake.appendleft([x + dx[d], y + dy[d]])
        snake.pop()
        t += 1
    return t




print(bfs())





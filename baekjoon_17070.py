from collections import deque

# 가로 : 1, 세로 : 2, 대각선 : 3

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

count = 0

stack = deque()
stack.append((1, 2, 1))

while stack:
    x, y, dp = stack.pop()
    if x == N and y == N:
        count+= 1
        continue
    if x > N or y > N:
        continue

    if dp == 1:
        if y+1 <= N and house[x-1][y] == 0:
            stack.append((x, y+1, 1))
            if x+1 <= N and house[x][y-1] == 0 and house[x][y] == 0:
                stack.append((x+1, y+1, 3))
    elif dp == 2:
        if x+1 <= N and house[x][y-1] == 0:
            stack.append((x+1, y, 2))
            if y+1 <= N and house[x-1][y] == 0 and house[x][y] == 0:
                stack.append((x+1, y+1, 3))
    else:
        if y+1 <= N and house[x-1][y] == 0:
            stack.append((x, y+1, 1))
        if x+1 <= N and house[x][y-1] == 0:
            stack.append((x+1, y, 2))
        if y+1 <= N and house[x-1][y] == 0 and x+1 <= N and house[x][y-1] == 0 and house[x][y] == 0:
            stack.append((x+1, y+1, 3))

print(count)
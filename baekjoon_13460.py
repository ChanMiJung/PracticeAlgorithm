from collections import deque


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]
visited = []

count = 0

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for x in range(N):
        for y in range(M):
            if board[x][y] == 'R':
                rx, ry = x, y
            if board[x][y] == 'B':
                bx, by = x, y
    return rx, ry, bx, by

def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#':
        x += dx
        y += dy
        cnt += 1
        if board[x][y] == 'O':
            break
    return x, y, cnt



def bfs():
    rx, ry, bx, by = init()
    
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visited.append((rx, ry, bx, by))

    while queue:
        rx, ry, bx, by, result = queue.popleft()
        if result > 10:
            return -1
        
        for d in range(4):
            nrx, nry, rcount = move(rx, ry, dx[d], dy[d])
            nbx, nby, bcount = move(bx, by, dx[d], dy[d])
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return result
            
            if nrx == nbx and nry == nby:
                if rcount > bcount:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]
            
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, result+1))
    return -1

print(bfs())
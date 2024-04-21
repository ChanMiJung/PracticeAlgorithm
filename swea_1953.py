from collections import deque

# 상하좌우

def check_move(pipe, npipe, direction):
    if direction == 0:
        # 상
        if pipe in [1, 2, 4, 7] and npipe in [1, 2, 5, 6]:
            return True
    elif direction == 1:
        # 하
        if pipe in [1, 2, 5, 6] and npipe in [1, 2, 4, 7]:
            return True
    elif direction == 2:
        # 좌
        if pipe in [1, 3, 6, 7] and npipe in [1, 3, 4, 5]:
            return True
    elif direction == 3:
        # 우
        if pipe in [1, 3, 4, 5] and npipe in [1, 3, 6, 7]:
            return True
    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(int(input())):
    N, M, R, C, L = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[R][C] = 1
    
    queue = deque()
    queue.append([(R, C), 1])

    while queue:
        (x, y), l = queue.popleft()
        if l == L:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < N and -1 < ny < M and visited[nx][ny] == 0 and l+1 <= L:
                if check_move(blocks[x][y], blocks[nx][ny], d):
                    visited[nx][ny] = 1
                    queue.append([(nx, ny), l+1])
    
    count = 0
    for row in visited:
        count += row.count(1)
    print(f"#{t+1} {count}")
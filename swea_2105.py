from collections import deque

# 시계방향으로 3번 회전
for t in range(int(input())):

    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    queue = deque()
    for i in range(N-2):
        for j in range(1, N-1):
            queue.append([(i, j), (i, j), [cafe[i][j]], 0])
    max_value = -1
    while queue:
        start, (x, y), desserts, turn = queue.pop()
        # print(start, (x, y), desserts, turn, (x, y) == start)

        if turn == 3:
            if (x, y) == start:
                max_value = max(max_value, len(desserts))
            else:
                # 직진
                nx = x - 1
                ny = y + 1
                if -1 < nx < N and -1 < ny < N:
                    if (nx, ny) == start:
                        queue.append([start, (nx, ny), desserts[:], turn])    
                    elif cafe[nx][ny] not in desserts:
                        queue.append([start, (nx, ny), desserts[:] + [cafe[nx][ny]], turn])    
        
        elif turn == 0:
            # 직진
            nx = x + 1
            ny = y + 1
            if -1 < nx < N and -1 < ny < N and cafe[nx][ny] not in desserts:
                queue.append([start, (nx, ny), desserts[:] + [cafe[nx][ny]], turn])
            # turn
            nx = x + 1
            ny = y - 1
            if -1 < nx < N and -1 < ny < N and cafe[nx][ny] not in desserts:
                queue.append([start, (nx, ny), desserts[:] + [cafe[nx][ny]], turn+1])
        elif turn == 1:
            # 직진
            nx = x + 1
            ny = y - 1
            if -1 < nx < N and -1 < ny < N and cafe[nx][ny] not in desserts:
                queue.append([start, (nx, ny), desserts[:] + [cafe[nx][ny]], turn])
            # turn
            nx = x - 1
            ny = y - 1
            if -1 < nx < N and -1 < ny < N and cafe[nx][ny] not in desserts:
                queue.append([start, (nx, ny), desserts[:] + [cafe[nx][ny]], turn+1])
        elif turn == 2:
            # 직진
            nx = x - 1
            ny = y - 1
            if -1 < nx < N and -1 < ny < N and cafe[nx][ny] not in desserts:
                queue.append([start, (nx, ny), desserts[:] + [cafe[nx][ny]], turn])
            # turn
            nx = x - 1
            ny = y + 1
            if -1 < nx < N and -1 < ny < N:
                if (nx, ny) == start:
                    queue.append([start, (nx, ny), desserts[:], turn+1])
                elif cafe[nx][ny] not in desserts:
                    queue.append([start, (nx, ny), desserts[:] + [cafe[nx][ny]], turn+1])
    print(f"#{t+1} {max_value}")
    
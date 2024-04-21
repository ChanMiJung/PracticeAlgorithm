from collections import deque, defaultdict
from copy import deepcopy

islands = []

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
bridges = []
directorys = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(M)] for _ in range(N)]
def bfs(sx, sy):
    island = [(sx, sy)]
    visited[sx][sy] = 1
    directorys.append((sx, sy))
    queue = deque()
    queue.append((sx, sy))
    while queue:
        x, y = queue.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < N and -1 < ny < M and area[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                island.append((nx, ny))
                directorys.append((nx, ny))
                visited[nx][ny] = 1
    islands.append(island)


def find_islands():
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                visited[i][j] = 1


def find_island_number(i, j):
    for idx in range(len(islands)):
        if (i, j) in islands[idx]:
            return idx
    return -1

def left_bridge(i, j):
    cnt = 0
    j -= 1
    while -1 < i < N and -1 < j < M and area[i][j] == 0:
        j -= 1
        cnt += 1
    if -1 < j < M and area[i][j] == 1 and cnt > 1:
        return find_island_number(i, j), cnt

    return -1, -1
    
def right_bridge(i, j):
    cnt = 0
    j += 1
    while -1 < i < N and -1 < j < M and area[i][j] == 0:
        j += 1
        cnt += 1
    if -1 < j < M and area[i][j] == 1 and cnt > 1:
        return find_island_number(i, j), cnt

    return -1, -1

def up_bridge(i, j):
    cnt = 0
    i -= 1
    while -1 < i < N and -1 < j < M and area[i][j] == 0:
        i -= 1
        cnt += 1
    if -1 < i < N and area[i][j] == 1 and cnt > 1:
        return find_island_number(i, j), cnt

    return -1, -1

def down_bridge(i, j):
    cnt = 0
    i += 1
    while -1 < i < N and -1 < j < M and area[i][j] == 0:
        i += 1
        cnt += 1
    if -1 < i < N and area[i][j] == 1 and cnt > 1:
        return find_island_number(i, j), cnt

    return -1, -1


def find_bridge(x):
    island = islands[x][:]
    n = len(islands)
    min_value = [-1] * n

    for (i, j) in island:
        num, value = left_bridge(i, j)
        if x < num and (min_value[num] == -1 or min_value[num] > value):
            min_value[num] = value
        num, value = right_bridge(i, j)
        if x < num and (min_value[num] == -1 or min_value[num] > value):
            min_value[num] = value
        num, value = up_bridge(i, j)
        if x < num and (min_value[num] == -1 or min_value[num] > value):
            min_value[num] = value
        num, value = down_bridge(i, j)
        if x < num and (min_value[num] == -1 or min_value[num] > value):
            min_value[num] = value
    for idx, val in enumerate(min_value):
        if val > 1:
            bridges.append((x, idx, val))      

answer = -1
def bridge_dfs(visited, nodes, value):
    global answer
    if nodes.count(True) == len(nodes):
        if answer == -1 or answer > value:
            answer = value
        return
    if len(visited) == len(nodes):
        return

    for i in range(len(bridges)):
        if i in visited:
            continue
        if nodes[bridges[i][0]] and nodes[bridges[i][1]]:
            continue
        if nodes[bridges[i][0]] or nodes[bridges[i][1]]:
            new_nodes = deepcopy(nodes)
            new_nodes[bridges[i][0]] = True
            new_nodes[bridges[i][1]] = True
            new_visited = deepcopy(visited)
            new_visited.append(i)
            value += bridges[i][2]
            bridge_dfs(new_visited, new_nodes, value)
    return




def main():
    global answer
    find_islands()
    n = len(islands)
    for i in range(n-1):
        find_bridge(i)
    if n == 2 and len(bridges) == 0:
        return
    bridges.sort(key=lambda x : x[2])
    if n == 2 and len(bridges) > 0:
        answer = bridges[0][2]
        return 
        
    for i in range(len(bridges)):
        bridge_dfs([i], [True if j in bridges[i][:2] else False for j in range(n)], bridges[i][2])



main()
print(answer)
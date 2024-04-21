from collections import deque, defaultdict
# 상 : 1, 하 : 2, 좌 : 3, 우 : 4
# N : 셀 개수, M : 격리시간, K : 미생물 군집 개수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(int(input())):
    N, M, K = map(int, input().split())
    
    data = dict()
    for _ in range(K):
        x, y, c, d = map(int, input().split())
        data[(x, y)] = (c, d)
    
    for m in range(M):
        new_data = defaultdict(list)
        for key, value in data.items():
            if value[1] == 1:
                nx = key[0] - 1
                c = value[0]
                d = value[1]
                if nx == 0:
                    d = 2
                    c //= 2
                new_data[(nx, key[1])].append((c, d))
            elif value[1] == 2:
                nx = key[0] + 1
                c = value[0]
                d = value[1]
                if nx == N-1:
                    d = 1
                    c //= 2
                new_data[(nx, key[1])].append((c, d))
            elif value[1] == 3:
                ny = key[1] - 1
                c = value[0]
                d = value[1]
                if ny == 0:
                    d = 4
                    c //= 2
                new_data[(key[0], ny)].append((c, d))
            elif value[1] == 4:
                ny = key[1] + 1
                c = value[0]
                d = value[1]
                if ny == N-1:
                    d = 3
                    c //= 2
                new_data[(key[0], ny)].append((c, d))
        data = dict()
        for key, value in new_data.items():
            if len(value) > 1:
                sorted_value = sorted(value)
                cnt = 0
                for (c, d) in sorted_value:
                    cnt += c
                data[key] = (cnt, sorted_value[-1][1])
            else:
                data[key] = value[0]
    
    answer = 0
    for key, value in data.items():
        answer += value[0]

    print(f"#{t+1} {answer}")


                





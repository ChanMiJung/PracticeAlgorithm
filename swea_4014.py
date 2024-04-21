
def check_build(row, N, X):
    cnt = 1
    for i in range(1, N):
        if row[i] == row[i-1]:
            cnt += 1
        elif row[i] == row[i-1] + 1 and cnt >= X:
            cnt += 1
        elif row[i] + 1 == row[i-1] and cnt >= 0:
            cnt = -X + 1
        else:
            return 0
    if cnt >= 0:
        return 1
    return 0
        

for t in range(int(input())):

    N, X = map(int, input().split())
    blocks = []
    answer = 0
    for i in range(N):
        blocks.append(list(map(int, input().split())))
        answer += check_build(blocks[i], N, X)
    
    for j in range(N):
        answer += check_build([blocks[i][j] for i in range(N)], N, X)
    
    print(f"#{t+1} {answer}")       


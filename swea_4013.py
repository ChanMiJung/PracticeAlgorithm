
# 시계방향 : 1 / 반시계방향 : -1
# N극 : 0 / S극 : 1

def check_turn(wheels, num, dr):
    rotation = [0, 0, 0, 0]
    rotation[num-1] = dr
    right_index = num
    while right_index < 4:
        if wheels[right_index-1][2] == wheels[right_index][-2]:
            break

        if rotation[right_index-1] == 1:
            rotation[right_index] = -1
        elif rotation[right_index-1] == -1:
            rotation[right_index] = 1
        right_index+= 1

    left_index = num-1
    while left_index > 0:
        if wheels[left_index-1][2] == wheels[left_index][-2]:
            break
        
        if rotation[left_index] == 1:
            rotation[left_index-1] = -1
        elif rotation[left_index] == -1:
            rotation[left_index-1] = 1
        left_index -= 1
    return rotation

    

def turn(wheel, dr):
    if dr == 1:
        temp = wheel.pop()
        wheel = [temp] + wheel
    elif dr == -1:
        temp = wheel.pop(0)
        wheel.append(temp)
    return wheel


for t in range(int(input())):
    K = int(input())
    wheels = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        m, dr = map(int, input().split())
        rotation = check_turn(wheels, m, dr)
        wheels = [turn(wheels[i], rotation[i]) for i in range(4)]
    answer = 1 * wheels[0][0] + 2 * wheels[1][0] + 4 * wheels[2][0] + 8 * wheels[3][0]
    print(f"#{t+1} {answer}")
            




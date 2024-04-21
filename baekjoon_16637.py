from collections import deque


N = int(input())
math_list = list(input().strip())
max_value = -(2**31)
    
int_max = 2**31



def dfs(order_list):
    global max_value, N, int_max

    # 괄호추가
    express_list = []
    index = 0
    for value in order_list:
        for i in range(index, value-1):
            express_list.append(math_list[i])
        express_list.append(eval("".join(math_list[value-1:value+2])))
        index = value + 2
    if index < N:
        for i in range(index, N):
            express_list.append(math_list[i])
    result = int(express_list[0])
    for i in range(1, len(express_list), 2):
        if express_list[i] == '+':
            result += int(express_list[i+1])
        elif express_list[i] == '-':
            result -= int(express_list[i+1])
        elif express_list[i] == '*':
            result *= int(express_list[i+1])


    if max_value < result and result < int_max:
        max_value = result
    
    for j in range(order_list[-1]+4, N, 2):
        dfs(order_list+[j])


if N == 1:
    value = int(math_list[0])
    if max_value < value < int_max:
        max_value = value
elif N == 3:
    value = eval("".join(math_list))
    if max_value < value < int_max:
        max_value = value
else:
    for i in range(1, N, 2):
        dfs([i])

print(max_value)

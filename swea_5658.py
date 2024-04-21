



for T in range(int(input())):
    N, K = map(int, input().split())
    numbers = list(input().strip())
    passwords = set()
    rotate = N//4
    for _ in range(rotate):
        # check_number
        for i in range(0, N, rotate):
            passwords.add(int("0x" + "".join(numbers[i:i+rotate]), 16))
        # rotate
        temp = numbers.pop()
        numbers = [temp] + numbers[:]
    print(f"#{T+1} {sorted(list(passwords), reverse=True)[K-1]}")
def down_sort(blocks, W, H):
    for j in range(W):
        for i in range(H-1, -1, -1):
            if blocks[i][j] == 0:
                move = False
                for k in range(i-1, -1, -1):
                    if blocks[k][j] > 0:
                        blocks[i][j] = blocks[k][j]
                        blocks[k][j] = 0
                        move = True
                        break
                if not move:
                    break
    return blocks

def remove_block(blocks, (x, y), cnt, N, W, H):
    remove_list = [(x, y)]
    idx = 0
    while idx < len(remove_list):
        x, y = remove_list[idx]
        value = blocks[x][y]
        blocks[x][y] = 1

        k = 1
        while k < value:
            if -1 < x-k and blocks[x-k][y] > 0:
                if (x-k, y) not in remove_list:
                    remove_list.append((x-k, y))
            if x+k < W and blocks[x+k][y] > 0:
                if (x+k, y) not in remove_list:
                    remove_list.append((x+k, y))
            if -1 < y-k and blocks[x][y-k] > 0:
                if (x, y-k) not in remove_list:
                    remove_list.append((x, y-k))
            if y+k < H and blocks[x][y+k] > 0:
                if (x, y+k) not in remove_list:
                    remove_list.append((x, y+k))
            k += 1

        idx += 1
    for (a, b) in remove_list:
        blocks[a][b] = 0

    blocks = down_sort(blocks, W, H)
    
    return 

    




for i in range(int(input())):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]


    for l in range(W):
        for k in range(H):
            if blocks[k][l] != 0:
                remove_block(blocks, (k, l), 1, N, W, H)
                break

    print("#" + (i+1) + " " + answer)
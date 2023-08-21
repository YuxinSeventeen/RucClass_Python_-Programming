# -*- coding: utf-8 -*-

def DiamondPrint(Char, N, Dir='X'):
    # 创建菱形模板
    diamond = [[' ' for i in range(7)] for j in range(7)]
    for i in range(4):
        diamond[i][3-i:4+i] = [Char]*(2*i+1)
        diamond[6-i][3-i:4+i] = [Char]*(2*i+1)
    
    # 纵向打印
    if Dir == 'Y':
        for i in range(N):
            # 打印上半部分
            for j in range(1, 8, 2):
                print(" " * ((7 - j) // 2) + Char * j)
            # 打印下半部分
            for j in range(5, 1, -2):
                print(" " * ((7 - j) // 2) + Char * j)
        print("   {}".format(Char))
    
    # 横向打印
    elif Dir == 'X':
        for row in diamond:
            for i in range(N):
                print(''.join(row), end='')
            print()

DiamondPrint("$", 7,Dir=("Y"))
print("\n")
DiamondPrint("%", 7,Dir=("X"))
""" transpose of a matrix"""

def t(a):
    ''' regardless of what elements be in matrix, it just transposes'''
    # x = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    x = [[0] * len(a) for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            x[j][i] = a[i][j]
    return x

# f =[['0x54', '0x77', '0x6f', '0x20','0'], ['0x4f', '0x6e', '0x65', '0x20','f'], ['0x4e', '0x69', '0x6e', '0x65','e'], ['0x20', '0x54', '0x77', '0x6f','j']]
# print(t(f))
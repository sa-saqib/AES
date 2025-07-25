''' does the exor operation element wise '''
# def addroundkey(a,b) -> list:
#     ''' considering the (input)matrices given are of same dimensions'''
#     res = [[int(a[i][j],16) ^ int(b[i][j],16) for j in range(len(a[0]))] for i in range(len(a))]
#     return res

# def addroundkey(a,b) -> list:
#     m =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#     for i in range(4):
#         for j in range(4):
#             (m[i][j]) ^= int(a[i][j],16) ^ int(b[i][j],16)
#     return m


def addroundkey(a, b) -> list:
    ''' element wise exor operation between two matrices '''
    result = []
    for row_a, row_b in zip(a, b):
        xor_row = [f'0x{(int(i, 16) ^ int(j, 16)):02x}' for i, j in zip(row_a, row_b)]
        result.append(xor_row)
    return result


# a =  [['0x54', '0x68', '0x61', '0x74'],
#     ['0x73', '0x20', '0x6d', '0x79'],
#     ['0x20', '0x4b', '0x75', '0x6e'],
#     ['0x67', '0x20', '0x46', '0x75']]

# b = [['0x20', '0xa3', '0x7f', '0xa8'],
#     ['0x9d', '0xb7', '0xf5', '0x45'],
#     ['0xaa', '0x9f', '0x4d', '0xf9'],
#     ['0xb7', '0xb7', '0xfb', '0x40']]
# print(addroundkey(a,b))
# End-of-file (EOF)

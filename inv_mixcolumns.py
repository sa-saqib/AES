'''in AES, the step mixcolumns just multiplies two matrices but intsead of adding does xor'''
from mixmul import mixmul
def invmixcolumns(a):
    '''a,b are expected to be 4*4, 4*1 matrices respectively '''
    m = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    b= [[14,11,13,9],
        [9,14,11,13],
        [13,9,14,11],
        [11,13,9,14]]
    for i in range(4):
        for j in range(4):# col of  a
            for k in range(4):#col of b
                m[i][j] ^= (mixmul((a[k][j]),b[i][k]))
                # (((a[i][k]))*b[k][j])
            # m[i][j] += (gmul((a[i][j]),b[j][i]))
    for i in range(4):
        for j in range(4):
            m[i][j] = f'0x{m[i][j]:02x}'
    return m

# f= [['0x47','0x40','0xa3','0x4c'],
#     ['0x37','0xd4','0x70','0x9f'],
#     ['0x94','0xe4','0x3a','0x42'],
#     ['0xed','0xa5','0xa6','0xbc']]
# print(invmixcolumns(f))
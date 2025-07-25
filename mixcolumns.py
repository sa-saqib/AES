'''in AES, the step mixcolumns just multiplies two matrices but intsead of adding does xor'''
from mixmul import mixmul
def mixcolumns(a):
    '''a,b are expected to be 4*4, 4*1 matrices respectively '''
    m = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    b= [[2,3,1,1],
    [1,2,3,1],
    [1,1,2,3],
    [3,1,1,2]]
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

# f= [['0x20','0xa3','0x7f','0xa8'],
#     ['0x9d','0xb7','0xf5','0x45'],
#     ['0xaa','0x9f','0x4d','0xf9'],
#     ['0xb7','0xb7','0xfb','0x40']]
# print(mixcolumns(f))
# a= [[2,3,1,1],
#     [1,2,3,1],
#     [1,1,2,3],
#     [3,1,1,2]]
# g= [[2,3,1,1],
#     [1,2,3,1],
#     [1,1,2,3],
#     [3,1,1,2]]
# output = [[30,70,110,150]]

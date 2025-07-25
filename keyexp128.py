""" round keys generation for AES 128 """
from gmul import gmul
from addrow import addrow


def keyexp128(a):
    ''' input "a" is key in hex'''
    fres = [a]
    for i in range(10):
        newkey = fres[-1]
        #roundconsts = 01, 02, 04, 08, 10, 20, 40, 80, 1B, 36, 6C, D8, AB, 4D,
#               9A, 2F, 5E, BC, 63, C6, 97, 35, 6A, D4, B3, 7D, FA, EF, C5
        x = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
        b = gmul(newkey[3], x[i])
        # res = []
        # res.append(addrow(newkey[0], b))
        # res.append(addrow(res[0], newkey[1]))
        # res.append(addrow(res[1], newkey[2]))
        # res.append(addrow(res[2], newkey[3]))
        res = [addrow(newkey[0], b)]
        for j in range(1, 4):
            res.append(addrow(res[j-1], newkey[j]))
        fres.append(res)
    return fres

# f = [['0x54', '0x68', '0x61', '0x74'],
#      ['0x73', '0x20', '0x6D', '0x79'],
#      ['0x20', '0x4B', '0x75', '0x6E'],
#      ['0x67', '0x20', '0x46', '0x75']]


# result = keyexp128(f)
# for n in range(11):
#     print(result[n])
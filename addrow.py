''' element wise exor between two rows '''


def addrow(a,b):
    ''' a and b are respective rows of matrix'''
    e =[]
    for i, j in zip(a,b):
        d = hex(int(i,16) ^ int(j,16))
        # e.append(d) #this line is replaced bcoz, in some situations we get only one digit hex no.
# which is not correct for the code written to replace it(that particular element ) from the s- box
        e.append(f'0x{int(d, 16):02x}')
    return e


# f=  ['0xb6', '0x5a', '0x9d', '0x85']
# g = ['0x54', '0x68', '0x61', '0x74']
# print(addrow(f,g))
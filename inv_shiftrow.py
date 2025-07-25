'''In AES decryption, There is shift row same is being implemented'''

def invshiftleft(a) -> list:
    '''Reverse of shiftleft - shifts each row right by its index'''
    for i in range(4):
        a[i] = a[i][-i:] + a[i][:-i]
    return a


# output  =  [[1 ,2 ,3 , 4],
#           [6 ,7 ,8 , 5],
#           [11,12,9 ,10],
#           [16,13,14,15]]

# print(invshiftleft(output))
# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
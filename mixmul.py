'''XTIMES(b) = {b6 b5 b4 b3 b2 b1 b0 0} ⊕ {0 0 0 1 1 0 1 1} if b7 = 1. 
             = ({b6 b5 b4 b3 b2 b1 b0 0}                     if b7 = 0'''


def mixmul(a, m) -> int | None:
    ''' just like matrix mul but add is replaced by exor '''
    
    if m == 1:
        a = int(a, 16)
        return a
    if m == 2:
        a = int(a, 16)
        if a < 0x80:
            return a << 1
        # if a > 0x7f:
        return (a << 1 & 0xff) ^ 0x1b
        # return None
    if m == 3:
        return (mixmul(a, 1) ^ mixmul(a, 2))
    if m == 4:
        if mixmul(a,2) < 0x80:
            return mixmul(a,2)<<1
        return ((mixmul(a,2)<<1) & 0xff) ^ 0x1b
    if m == 8:
        if mixmul(a,4) < 0x80:
            return mixmul(a,4)<<1
        return ((mixmul(a,4)<<1) & 0xff) ^ 0x1b
    if m == 9:
        return (mixmul(a, 1) ^ mixmul(a, 8))
    if m == 11:
        return (mixmul(a, 1) ^ mixmul(a,2) ^ mixmul(a, 8)  )
    if m == 13:
        return (mixmul(a, 1) ^ mixmul(a,4) ^ mixmul(a, 8)  )
    if m == 14:
        return (mixmul(a, 2) ^ mixmul(a,4) ^ mixmul(a, 8)  )
    return None

# X = '0x80'
# print(hex(mixmul(X, 2)))

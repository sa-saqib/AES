
""" taking plain key as input """
from toascii import text2num
from transpose import t
from keyexp128 import keyexp128
from addroundkey import addroundkey
from sub_byte_mat import sub_byte
from shiftrow import shiftleft
from mixcolumns import mixcolumns

def aes128(a, b):
    """ a is text and b is key """ 
    state_matrix = t(text2num(a))
    # print("state", state_matrix)
    roundkeys = keyexp128(text2num(b))
    # print('roubd', roundkeys[0])
    newstate = addroundkey(state_matrix, t(roundkeys[0]))
    # print(newstate)

    for i in range(1, 10):
        u = sub_byte(newstate)
        v = shiftleft(u)
        w = mixcolumns(v)
        newstate = addroundkey(w, t(roundkeys[i]))
        # print(f"After Add Round Key (Round {i}):")
        # print(newstate)

    p = sub_byte(newstate)
    q = shiftleft(p)
    r = addroundkey(q, t(roundkeys[10]))
    cipher = t(r)
    return (cipher)



f = "Two One Nine Two"
g = "Thats my Kung Fu"
output = aes128(f, g)
print(output)

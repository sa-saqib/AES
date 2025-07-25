'''AES 128 decryption give the cipher text in matrix form and get the actual plain text '''
from toascii import text2num
from num2text import num2text
from transpose import t
from keyexp128 import keyexp128
from addroundkey import addroundkey
from inv_sub_byte_mat import invsub_byte
from inv_shiftrow import invshiftleft
from inv_mixcolumns import invmixcolumns

def aes128de(a, b):
    """ a is cipher text in matrix and b is key """ 
    state_matrix = t(a)
    roundkeys = keyexp128(text2num(b))
    k = addroundkey(state_matrix, t(roundkeys[10]))
    l = invshiftleft(k)
    newstate = invsub_byte(l)

    for i in range(9,0,-1):
        u = addroundkey(newstate, t(roundkeys[i]))
        v = invmixcolumns(u)
        w = invshiftleft(v)
        newstate = invsub_byte(w)

    r = addroundkey(newstate, t(roundkeys[0]))
    decipher = t(r)
    plaintext = num2text(decipher)
    return plaintext


f = [['0x29', '0xc3', '0x50', '0x5f'], ['0x57', '0x14', '0x20', '0xf6'], ['0x40', '0x22', '0x99', '0xb3'], ['0x1a', '0x2', '0xd7', '0x3a']]
g = "Thats my Kung Fu"
output = aes128de(f, g)
print(output)

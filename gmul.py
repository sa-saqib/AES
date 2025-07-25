"""in key expansion we require gfunction to generate round keys
key in english : "Thats my Kung Fu"
• w[0] = (54, 68, 61, 74),w[1] = (73, 20, 6D, 79),w[2] = (20, 4B, 75, 6E),w[3] = (67, 20, 46, 75)
• g(w[3]):
• circular byte left shift of w[3]: (20, 46, 75, 67)
• Byte Substitution (S-Box): (B7, 5A, 9D, 85)
• Adding round constant (01, 00, 00, 00) gives: g(w[3]) = (B6, 5A, 9D, 85)
• w[4] = w[0] ⊕ g(w[3]) = (E2, 32, FC, F1):
Key in Hex (128 bits): 54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75
• w[0] = (54, 68, 61, 74),w[1] = (73, 20, 6D, 79),w[2] = (20, 4B, 75, 6E),w[3] = (67, 20, 46, 75)
• g(w[3]):
•          circular byte left shift of w[3]: (20, 46, 75, 67)
•          Byte Substitution (S-Box): (B7, 5A, 9D, 85)
•          Adding round constant (01, 00, 00, 00) gives: g(w[3]) = (B6, 5A, 9D, 85)
•          w[4] = w[0] ⊕ g(w[3]) = (E2, 32, FC, F1):  """

from sub_byte_mat import sub_byte_row


def gmul(a, i):
    """ a is last column forming a word
        i is number which represents round (ith round) """
    a = a[1:] + a[:1]
    b = sub_byte_row(a)
    b[0] = hex(int(b[0], 16) ^ i)
    return b

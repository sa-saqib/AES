
def text2num(a):
    l = []
    res = []
    x = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in a:
        l.append((hex(ord(i))))
    for i in range(1, 5):
        res.append(l[4*(i-1):(4*(i))])
    # for i in range(4):
    #     for j in range(4):
    #         x[i][j] = res[j][i]
    return res


# print(text2num("Thats my Kung Fu"))
# print(text2num("Two One Nine Two"))

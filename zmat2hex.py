''' not a neccessary step '''
def hexstring(matrix):
    '''converts matrix with hex values into hexstring by concatenating all the elements row wise'''
    result = []
    for row in matrix:
        formatted_hex = [h[2:].zfill(2) for h in row]
        result.extend(formatted_hex)
    return ''.join(result)

hex_matrix = [['0x29', '0xc3', '0x50', '0x5f'],
              ['0x7', '0x14', '0x20', '0xf6'],
              ['0x40', '0x2', '0x99', '0xb3'],
              ['0x1a', '0x2',  '0xd7', '0xa']]

hex_string = hexstring(hex_matrix)
print(hex_string)  # Output:29c3505f071420f6400299b31a02d70a
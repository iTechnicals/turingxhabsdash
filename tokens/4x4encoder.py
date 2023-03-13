def encode(num):
    binary = str(bin(num))[2:]
    while len(binary) < 12:
        binary = "0" + binary
    data = [["0", "0", "0", "0"],
            ["0", "0", "1", "0"],
            ["0", "1", "1", "0"],
            ["0", "0", "0", "0"]]
    for i, j in enumerate(binary[8:]):
        data[3][i] = j
    for i, j in enumerate(binary[:3]):
        data[0][i] = j
    data[1][0] = binary[4]; data[1][3] = binary[5]
    data[2][0] = binary[6]; data[2][3] = binary[7]
    
    return data

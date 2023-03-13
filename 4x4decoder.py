import cv2

def readimg(filename):
    img = cv2.imread("token.png", 0)
    data = [["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"]] 
    xsize, ysize = img.shape[0] // 4, img.shape[1] // 4
    for i in range(4):
        for j in range(4):
            totalcolor = 0
            for x in range(i*xsize, (i+1)*xsize):
                for y in range(j*ysize, (j+1)*ysize):
                    totalcolor += image[y][x][0]
            avgcolor = totalcolor / (xsize * ysize)
            if avgcolor <= 128:
                data[i][j] = "0"
            else:
                data[i][j] = "1"
    return data

def align(data):
    while data[1][1] != "0":
        data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0])-1,-1,-1)]
    return data

def decode(data):
    lindata = []
    value = 0
    for i in data:
        for j in i:
            lindata.append(j)
    lindata = lindata[:5] + lindata[7:9] + lindata[11:]
    for i, j in enumerate(lindata):
        value += int(j)*2**(11-i)
    return value
    

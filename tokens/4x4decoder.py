import cv2

def readimg(filename):
    # NB image loaded in grayscale
    img = cv2.imread(filename, 0)
    data = [["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"]]
    # Calculates size of each 'pixel'
    xsize, ysize = img.shape[0] // 4, img.shape[1] // 4
    # Iterates through all pixels
    for i in range(4):
        for j in range(4):
            # Calculates the average brightness value for each pixel
            totalcolor = 0
            for x in range(i*xsize, (i+1)*xsize):
                for y in range(j*ysize, (j+1)*ysize):
                    totalcolor += img[x][y]
            avgcolor = totalcolor / (xsize * ysize)
            # Decides whether the pixel was white or black
            if avgcolor >= 100:
                data[i][j] = "0"
            else:
                data[i][j] = "1"
    return data

# Rotates the data until the central L is correctly oriented
def align(data):
    while data[1][1] != "0":
        data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0])-1,-1,-1)]
    return data

# Removes the central L and calculates the corresponding value for the pixel
def decode(data):
    value = 0
    lindata = data[0] + data[1] + data[2] + data[3]
    if not (lindata[6] == "1" and lindata[9] == "1" and lindata[10] == "1"):
        return None
    lindata = lindata[:5] + lindata[7:9] + lindata[11:]
    for i, j in enumerate(lindata):
        value += int(j)*2**(11-i)
    return value

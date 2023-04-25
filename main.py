from PIL import Image
import numpy as np
import random
import math

if __name__ == '__main__':
    im = Image.open("cat.jpg")
    p = np.array(im)
    watermark = "Halo"
    ascii_string = ""

    for c in watermark:
        char_water_mark = str(bin(ord(c)))[2:]
        if len(char_water_mark) < 8:
            char_water_mark = (8 - len(char_water_mark)) * "0" + char_water_mark
        ascii_string += char_water_mark

    p2 = p.ravel().copy()
    x = random.choice(range(len(p2)-len(ascii_string)))

    for i in range(len(ascii_string)):
        p2[x+i] = int(str(bin(p2[x+i]))[:-1] + ascii_string[i], 2)

    p2 = p2.reshape(len(p), len(p[0]), len(p[0][0]))

    sum_wm = 0
    x_position = 0
    y_position = 0
    for i in range(len(p)):
        for j in range(len(p[0])):
            for k in range(len(p[0][0])):
                if p[i][j][k] != p2[i][j][k]:
                    x_position = i
                    y_position = j
                    sum_wm += 1

    print("Different rgb values:", sum_wm)
    print("Max changed pixels:", math.ceil(len(ascii_string)/3))
    print("String ends at position: X", x_position, "| Y", y_position)
    print("Max length of string (using ASCII):", math.floor((len(p)*len(p[0])*len(p[0][0]))/8))

    p2 = Image.fromarray(p2.astype('uint8'))
    p2.save('cat_result.jpg', quality=100, subsampling=0)

import numpy as np
import cv2
import sys

image = cv2.imread(sys.argv[1])

h = image.shape[0]
w = image.shape[1]

print ('width: %d pixels'% (w))
print ('height: %d pixels'% (h))

file_ascii = open(sys.argv[2],'w')
table_convert = ['', '.', ',' ,';', '-', '"','*', 'l', 'n', 's', 'a', 'k', 'm', 'g', 'O', 'X', 'A', 'K', 'G', 'M', '@', '@']

for i in range(h):
    str = ''
    for j in range(w):
        average_point = (int(image[i][j][0]) + int(image[i][j][1]) + int(image[i][j][2]) ) // 3
        str += '  ' + table_convert[average_point//12]
    file_ascii.write(str + '\n')

file_ascii.close()

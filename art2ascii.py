import cv2
import numpy as np

img = cv2.imread("./externals/audiR8.jpeg")
#img = cv2.imread("./externals/Sebastian-Vettel.jpg")
#img = cv2.imread("./externals/Golden-Gate-Bridge.png")
img = cv2.resize(img, (150,150), interpolation = cv2.INTER_AREA)

dimensions = img.shape
intensity = np.empty((dimensions[0], dimensions[1]))
imgASCII = []

#Calculating the intensity of each pixel without loading a greyscale image
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        RGBval = img[x][y]
        avg = (int(RGBval[0]) + int(RGBval[1]) + int(RGBval[2])) // 3
        intensity[x][y] = avg

#Intensity to Ascii Values
#Larger intensity values correspond to a 'larger' ASCII character.
mapASCII = ['`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
        '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
        'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
        'a','o','*','#','M','W','&','8','%','B','@','$']

#Using a dictionary to map intensity values to ASCII values
intensityMapping = {}
lower = 0
increment = 255 // len(mapASCII)
upper = lower + increment

for char in mapASCII:
    intensityMapping[(lower, upper)] = char
    lower += increment + 1
    upper += increment + 1

#To view the mapping of intensity values to ASCII characters
#for key, val in intensityMapping.items():
#    print(f'{val}: {key}')

for x in range(dimensions[0]):
    row = []
    for y in range(dimensions[1]):
        key = intensity[x][y]
        for low,high in intensityMapping.keys():
        #Gets the lower and upper bound for each of the keys from the intensityMapping dictionary
            if key >= low and key <= high:
                row.append(intensityMapping[(low, high)])
                break
    imgASCII.append(row)

for row in imgASCII:
    line = [x + x + x for x in row]
    #For a sharper image, each ASCII character is printed out thrice instead of once.
    print("".join(line))

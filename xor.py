########################################################
# Name: Devon Knudsen
# Assignment: XOR ROX
# Date: 5 May 2020
# Writen in Python 3
########################################################

from PIL import Image
from random import randint

# the images
INPUT_IMAGE = "input.png"
AND_IMAGE = "and.png"
OR_IMAGE = "or.png"
XOR_IMAGE = "xor.png"

# bitwise operation flags
AND_OP = True
OR_OP = True
XOR_OP = True

# generate and return a list of random rgb tuples as a keys for every pixel within the input image
def generateKeys():
    img = Image.open(INPUT_IMAGE)
    rows, cols = img.size
    imgSize = rows * cols
    
    keys = []
    for i in range(imgSize):
        
        # generate random rgb tuple
        currKey = (randint(0,255),randint(0,255), randint(0,255))
        
        # print the rgb values of the current key
        print("{},{},{}".format(currKey[0], currKey[1], currKey[2]))
        
        keys.append(currKey)
    
    return keys
    
# mutate the input image using and, or and/or xor bitwise operations using the provided key list
def mutateImg(keys):
    
    # loading images and their pixels for each type of bitwise operation based on which flags are set to true
    if(AND_OP):
        aImg = Image.open(INPUT_IMAGE)
        aPixels = aImg.load()
    if(OR_OP):
        oImg = Image.open(INPUT_IMAGE)
        oPixels = oImg.load()
    if(XOR_OP):
        xImg = Image.open(INPUT_IMAGE)
        xPixels = xImg.load()
    
    img = Image.open(INPUT_IMAGE)
    pixels = img.load()
    rows, cols = img.size
    
    currKeyPos = 0
    for i in range(rows):
        row = i
        for j in range(cols):
            col = j
            
            r, g, b = pixels[row, col]
            key = keys[currKeyPos]
            
            if(AND_OP):
                # add operation on current pixel with random key
                aPixels[row, col] = (key[0] & r, key[1] & g, key[2] & b)
            
            if(OR_OP):
                # or operation on current pixel with random key
                oPixels[row, col] = (key[0] | r, key[1] | g, key[2] | b)
            
            if(XOR_OP):
                # xor operation on current pixel with random key
                xPixels[row, col] = (key[0] ^ r, key[1] ^ g, key[2] ^ b)
                
            currKeyPos += 1
    
    # write the new image
    if(AND_OP):
        aImg.save(AND_IMAGE)
    if(OR_OP):
        oImg.save(OR_IMAGE)
    if(XOR_OP):
        xImg.save(XOR_IMAGE)
    
# MAIN
keys = generateKeys()
mutateImg(keys)

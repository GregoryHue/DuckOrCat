# Quick script to resize images that are too large. Also slighty degrades the quality in order to save on storage and memory.
# Usage : source env/bin/activate && cd app/tools/ && python3 resize.py 

from PIL import Image
import os, sys

MIN_SIZE = 1024
PATH = "../images/"

dirs = os.listdir( PATH )

i = 0
j  = len(dirs)

resized = 0

for item in dirs:
    if os.path.isfile(PATH+item):
        im = Image.open(PATH+item)
        f, e = os.path.splitext(PATH+item)
        print(str(i + 1) + ' images out of ' + str(j) + ' \t| ', end='')
        
        if im.width > MIN_SIZE:
            new_height = round(im.height / (im.width / MIN_SIZE))
            print('name: ', item, '\t| width: ', im.width, '\t| height: ', im.height, ' \t| new width: ', MIN_SIZE, '\t| new height: ', new_height)
            imResize = im.resize((MIN_SIZE, new_height), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)
            resized = resized + 1
        elif im.height > MIN_SIZE:
            new_width = round(im.width / (im.height / MIN_SIZE))
            print('name: ', item, '\t| width: ', im.width, '\t| height: ', im.height, ' \t| new width: ', new_width, '\t| new height: ', MIN_SIZE)
            imResize = im.resize((new_width, MIN_SIZE), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)
            resized = resized + 1
        else:
            imResize = im.resize((im.width, im.height), Image.ANTIALIAS)
            print('name: ', item, '\t| width: ', im.width, '\t| height: ', im.height, ' \t| new width: ', '*', '\t| new height: ', '*')
            imResize.save(f + '.jpg', 'JPEG', quality=90)
        i = i +1

    

print('\nResized ' +str(resized) + ' pictures.')
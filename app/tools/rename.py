# Quick script to rename images.
# Usage : source env/bin/activate && cd app/tools/ && python3 rename.py 

from PIL import Image
import os, sys

RENAME = 'Duck_'
EXTENSION = '.jpg'
PATH = "../images/"

dirs = os.listdir( PATH )

i = 0
j  = len(dirs)

# Renaming them al first to a temporary name, to avoid overwriting files.
for item in dirs:
    if os.path.isfile(PATH+item):
        f, e = os.path.splitext(PATH+item)
        print(str(i + 1) + ' images out of ' + str(j) + ' \t| ', end='')
        if os.path.isfile(PATH + RENAME + str(i) + EXTENSION):
            j = i
            while os.path.isfile(PATH + RENAME + str(j) + EXTENSION):
                j = j + 1
            os.rename(PATH+item, PATH + RENAME + str(j) + EXTENSION)
        else:
            os.rename(PATH+item, PATH + RENAME + str(i) + EXTENSION)
            
        print('original name: ', item, '\t| new name: ', RENAME + str(i) + EXTENSION)
        i = i +1

    

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

renamed = 0

for item in dirs:
    if os.path.isfile(PATH+item):
        f, e = os.path.splitext(PATH+item)
        print(str(i + 1) + ' images out of ' + str(j) + ' \t| ', end='')
        if os.path.isfile(PATH + RENAME + str(i) + EXTENSION):
            # To avoid overwriting pictures, this will search for a another file name available.
            temp_i = 0
            while os.path.isfile(PATH + RENAME + str(temp_i) + EXTENSION):
                temp_i = temp_i + 1
            os.rename(PATH+item, PATH + RENAME + str(temp_i) + EXTENSION)
            renamed = renamed + 1
        else:
            os.rename(PATH+item, PATH + RENAME + str(i) + EXTENSION)
            renamed = renamed + 1
            
        print('original name: ', item, '\t| new name: ', RENAME + str(i) + EXTENSION)
        i = i +1

    
print('\nRenamed ' +str(renamed) + ' files.')
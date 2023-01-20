# Quick script to delete duplicate images.
# Usage : source env/bin/activate && cd app/tools/ && python3 delete_duplicate.py 

from PIL import Image
import os, sys
import hashlib


def file_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

PATH = "../images/"

dirs = os.listdir( PATH )

i = 0
j  = len(dirs)

hash_codes = []

removed = 0

for item in dirs:
    if os.path.isfile(PATH+item):
        print(str(i + 1) + ' images out of ' + str(j) + ' \t| ', end='')
        hash = file_hash(PATH+item)
        print(hash, '\t| name: ', item, end='')
        if hash in hash_codes:
            os.remove(PATH+item)
            removed = removed + 1
            print('\t| removed')
        else:
            hash_codes.append(hash)
            print('\t| stayed')
        i = i +1

print('\nRemoved ' +str(removed) + ' duplicates.')
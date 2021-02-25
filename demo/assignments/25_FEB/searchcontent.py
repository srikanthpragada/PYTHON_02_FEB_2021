# searchcontent.py string start_dir

import os
import sys


def file_contains(filename, search_string):
    try:
        with open(filename, "r") as f:
            if search_string in f.read():
                return True
            else:
                return False
    except:
        pass


if len(sys.argv) < 2:
    print("Usage : python searchcontent.py string start_dir")
    exit()

search_string = sys.argv[1]

if len(sys.argv) == 2:
    start_dir = os.getcwd()
else:
    start_dir = sys.argv[2]

allfiles = os.walk(start_dir)

for dirname, folders, files in allfiles:
    for file in files:
        filename = dirname + "\\" + file
        if file_contains(filename, search_string):
            print(filename)

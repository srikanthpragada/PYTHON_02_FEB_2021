import os

stdir = r"d:\classroom\feb2\demo"
allfiles = os.walk(stdir)

for dirname, folders, files in allfiles:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)

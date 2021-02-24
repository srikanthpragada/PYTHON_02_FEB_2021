import os

stdir = r"d:\classroom\feb2\demo"
allfiles = os.walk(stdir)

for name,folders,files in allfiles:
    print(f"{name:50} {len(files):3}")



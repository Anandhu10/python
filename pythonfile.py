import os

# List all files in a directory using scandir()
basepath = 'F:\pendrive backup'
fsize=os.path.getsize(basepath)
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
            print(f"the file {basepath} is: {fsize}Bytes.")

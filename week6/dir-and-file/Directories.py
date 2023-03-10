import os
def listDirs(p):
    print([x.name for x in os.scandir(path = p) if x.is_dir()])

def listFiles(p):
    print([x.name for x in os.scandir(path = p) if x.is_file()])

def listDirsAndFiles(p):
    print([x.name for x in os.scandir(path = p)])

path = '..'
listDirs(path)
listFiles(path)
listDirsAndFiles(path)
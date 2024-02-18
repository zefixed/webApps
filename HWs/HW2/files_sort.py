from os import listdir
from os.path import isfile
from sys import argv

def files_sort(path: str) -> list[str]:
    lstdir = []
    for file in listdir(path):
        if isfile(path + "/" + file):
            lstdir.append(file)
    lstdir.sort(key=lambda x: x.split(".")[-1])
    
    return lstdir

if __name__ == "__main__":
    print("\n".join(files_sort(argv[1])))
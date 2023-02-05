from zipfile import ZipFile
import os

def human_format(size):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ']
    index = 0
    for i in range(len(sizes)):
        if size / (1024 ** i) < 1:
            break
        index = i
    return f'{round(size / (1024 ** index))}{sizes[index]}'



with ZipFile('mongosh-1.6.2-win32-x64.zip') as zf:
    for name in zf.namelist():
        size = zf.getinfo(name).file_size
        items = name.rstrip("/").split("/")    

        print("|  "*(len(items)-1) + items[-1]+ '  '+human_format(size) )
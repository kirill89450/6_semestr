import shutil
import time

def make_reserve_arc(source, dest):
    archive_name = f"{dest}/{time.strftime('%d-%m-%Y-%H-%M-%S')}.zip"
    shutil.make_archive(archive_name.strip('.zip'), 'zip', source)
    
    
make_reserve_arc(r'C:\Users\kirih\OneDrive\Рабочий стол\lab1\test5',r'C:\Users\kirih\OneDrive\Рабочий стол\lab1')
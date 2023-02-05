import os

def get_dir_info(path):
    size = 0
    file_count = 0
    dir_count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        size += sum(os.path.getsize(os.path.join(dirpath, f)) for f in filenames)
        file_count += len(filenames)
        dir_count += len(dirnames)

    return size, file_count, dir_count

def top_dirs_by_count(path):
    dirs = {}
    for dirpath, dirnames, filenames in os.walk(path):
        dir_size, file_count, subdir_count = get_dir_info(dirpath)
        total_count = file_count + subdir_count
        dirs[dirpath] = (total_count, dir_size)

    top_dirs = sorted(dirs.items(), key=lambda x: x[1][0], reverse=True)[:10]
    for dirpath, (file_count, dir_size) in top_dirs:
        size_str = ''
        if dir_size < 1024:
            size_str = f"{dir_size} B"
        elif dir_size < 1024**2:
            size_str = f"{dir_size / 1024:.2f} KB"
        elif dir_size < 1024**3:
            size_str = f"{dir_size / 1024**2:.2f} MB"
        else:
            size_str = f"{dir_size / 1024**3:.2f} GB"
        print(f"{dirpath} - {file_count} файлов и каталогов| {size_str}")
        
        
top_dirs_by_count(r'C:\Users\kirih\OneDrive\Рабочий стол\test4')
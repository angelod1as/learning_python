from pathlib import Path
import os


def dir_size(filepath, depth=1, line_size=0):
    for directory in filepath.glob('*'):
        if directory.is_dir() and not directory.name.startswith('.'):
            size = 0
            for file in directory.glob('**/*'):
                if file.is_file():
                    size += os.path.getsize(file)
            print('--' * line_size, directory.name,
                  round(size / 1024 / 1024, 2), 'mb')
            if (depth > 1):
                dir_size(directory, depth-1, line_size+1)


dir_size(Path.home() / 'Music', 3)

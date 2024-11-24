from pathlib import Path
import shutil
import os

# Copying file with copyfile
# Doesn't copy permissions
curr_folder = Path(__file__).parent
curr_path = curr_folder / "sample.txt"
dest_path = curr_folder / 'dest1' / "sample.txt"  # File, not folder

shutil.copyfile(curr_path, dest_path)

# Copying with copy
# Copies permissions
curr_folder = Path(__file__).parent
curr_path = curr_folder / "sample.txt"
dest_folder = curr_folder / 'dest2'

shutil.copy(curr_path, dest_folder)

# Copying with copy2
# Copies metadatas
curr_folder = Path(__file__).parent
curr_path = curr_folder / "sample.txt"
dest_folder = curr_folder / 'dest3'

shutil.copy2(curr_path, dest_folder)

# Moving files
curr_folder = Path(__file__).parent
curr_path = curr_folder / "sample.txt"
dest_folder = curr_folder / 'dest1'  # Folder or file

shutil.move(curr_path, dest_folder)

# Deleting files
curr_folder = Path(__file__).parent
curr_path = curr_folder / "sample.txt"
dest_file = curr_folder / 'dest1' / 'file.txt'

print('Creating')
shutil.copyfile(curr_path, dest_file)

if dest_file.exists():
    print('Removing')
    os.remove(dest_file)

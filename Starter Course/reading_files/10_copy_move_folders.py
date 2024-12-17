from pathlib import Path
import shutil

# Creating folders
curr_folder = Path(__file__).parent
dest_folder = curr_folder / "dest4"
dest_folder.mkdir(exist_ok=True)

# Creating folders within folders
curr_folder = Path(__file__).parent
dest_folder = curr_folder / "dest5" / "inner"
dest_folder.mkdir(exist_ok=True, parents=True)

# Copying folders (with content)
curr_folder = Path(__file__).parent
shutil.copytree(curr_folder / "dest5", curr_folder / "dest1" / "dest5")

# Deleting empty folders
curr_folder = Path(__file__).parent
remove_folder = curr_folder / "dest5" / "inner"
if remove_folder.exists():
    remove_folder.rmdir()

# Deleting full folders
curr_folder = Path(__file__).parent
remove_folder = curr_folder / "dest1" / "dest5"
if remove_folder.exists():
    shutil.rmtree(remove_folder)

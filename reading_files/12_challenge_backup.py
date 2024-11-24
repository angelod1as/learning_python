# Organize files by format
from pathlib import Path
import shutil
import datetime

curr_dir = Path(__file__).parent
folder_to_organize = curr_dir / "challenge_files"
organized_folder = curr_dir / "organized"
backup_folder = curr_dir / "backup"

if organized_folder.exists():
    shutil.rmtree(organized_folder)

organized_folder.mkdir()

if not backup_folder.exists():
    backup_folder.mkdir()

for file in folder_to_organize.glob('**/*'):
    if file.is_file():
        suffix_folder = organized_folder / file.suffix.replace('.', '')
        if not suffix_folder.exists():
            suffix_folder.mkdir()
        shutil.copy(file, suffix_folder)

backup_name = datetime.datetime.now().strftime('%Y_%m_%d')
shutil.make_archive(backup_folder / backup_name, 'zip', organized_folder)

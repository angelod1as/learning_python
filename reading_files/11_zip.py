from pathlib import Path
import shutil

# Zipping
curr_folder = Path(__file__).parent
zip_name = curr_folder / "zipped"
shutil.make_archive(zip_name, 'zip', curr_folder)

# Unzipping
curr_folder = Path(__file__).parent
zippend_file = curr_folder / "zipped.zip"
unzipped_folder = curr_folder / "unzipped"
shutil.unpack_archive(zippend_file, unzipped_folder)

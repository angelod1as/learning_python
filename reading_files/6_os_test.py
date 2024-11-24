from pathlib import Path
import os

# Listing paths of files on folder
print('\nAll files')
print(list(Path.cwd().glob('*')))

# Filtering paths
print('\nPython files')
print(list(Path.cwd().glob('*.py')))

# Filtering subfiles
print('\nSubfiles files')
print(list(Path.cwd().glob('**/*')))

# Validating paths with exists()
print('\nExists?')
print(Path.home().exists())

# Checking if file or folder
print('\nIs __file__ file?')
print(Path(__file__).is_file())
print('\nIs __file__ parent file?')
print(Path(__file__).parent.is_file())
print('\nIs __file__ parent dir?')
print(Path(__file__).parent.is_dir())

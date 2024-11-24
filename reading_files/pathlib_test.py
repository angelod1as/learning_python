from pathlib import Path
import os

caminho = Path('primeira_pasta/segunda_pasta')

for nome in ['arch1.txt', 'arch2.txt', 'arch2.txt']:
    caminho_arquivo = caminho / nome
    # print(caminho_arquivo)

###### Testing Path ###########
# Home dir
print(Path.home())
# Working dir
print(Path.cwd())
# Is it absolute?
print(Path.cwd().is_absolute())  # true
# A relative folder
print(Path('test_folder'))
# Is it absolute?
print(Path('test_folder').is_absolute())  # false
# Turning to absolute
print(Path.cwd() / 'test_folder')
print((Path.cwd() / 'test_folder').exists())  # true
# What if we change the folder?
os.chdir(Path.home())
print((Path.cwd() / 'test_folder').exists())  # false

###### Testing __file__ ###########
print(__file__)
print(Path(__file__))
print(Path(__file__).is_absolute())  # true
print(Path(__file__).parent)  # navigating
print((Path(__file__).parent / 'test_folder').exists())  # true

###### Testing partial files ###########
caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print(caminho_arquivo.anchor)
print(caminho_arquivo.parent)
print(caminho_arquivo.name)
print(caminho_arquivo.stem)
print(caminho_arquivo.suffix)
print(caminho_arquivo.drive)  # windows driver
print(caminho_arquivo.parents[2])  # navigate multiple parents

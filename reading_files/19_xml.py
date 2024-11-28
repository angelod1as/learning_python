import xml.dom.minidom
from pathlib import Path

# Reading xml
curr_dir = Path(__file__).parent
dom_tree = xml.dom.minidom.parse(str(curr_dir / 'xmls' / 'livros.xml'))

group = dom_tree.documentElement
livros = group.getElementsByTagName('livro')


# Looping
for livro in livros:
    title = livro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
    author = livro.getElementsByTagName('autor')[0].childNodes[0].nodeValue
    print('Titulo', title, '| Autor', author)

# Saving
livros[0].getElementsByTagName(
    'autor')[0].childNodes[0].nodeValue = 'Soares, Adriano'

with open(curr_dir / 'xmls' / 'livros_copia.xml', 'w', encoding='utf-8') as file:
    dom_tree.writexml(file)

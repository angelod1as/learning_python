from pathlib import Path


def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob('**/*'):
        if arquivo.is_file():
            if arquivo.stem == nome_do_arquivo:
                print(arquivo)
                break


encontra_arquivo(Path.cwd(), '7_exercise')

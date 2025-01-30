import pypdf
from pathlib import Path
from collections import Counter

caminho_pdf = Path("materiais de aula") / "documentos" / "vpt_minecraft.pdf"
leitor_pdf = pypdf.PdfReader(caminho_pdf)

texto_por_pagina = [pagina.extract_text() for pagina in leitor_pdf.pages]

palavras = []
for texto in texto_por_pagina:
    palavras_da_pagina = (
        texto.lower().replace("\n", " ").replace(",", "").replace(".", "").split(" ")
    )
    palavras.extend(palavras_da_pagina)

contagem = Counter(palavras)
print(f"\n\n:DEV {contagem.most_common(20)}\n\n")

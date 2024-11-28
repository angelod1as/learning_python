from pathlib import Path
import pandas as pd

current_dir = Path(__file__).parent
sheet_dir = Path(current_dir / 'planilhas')
sheet_name = 'clientes.xlsx'
sheet_dict = pd.read_excel(Path(sheet_dir / sheet_name), sheet_name=None)

for tab, sheet in sheet_dict.items():
    sheet.to_excel(Path(sheet_dir / 'split' / f'{tab}.xlsx'), index=False)

with pd.ExcelWriter(Path(sheet_dir / 'joined' / sheet_name)) as joined:
    for file in Path(sheet_dir / 'split').glob('*.xlsx'):
        sheet = pd.read_excel(file)
        sheet.to_excel(joined, sheet_name=file.stem, index=False)

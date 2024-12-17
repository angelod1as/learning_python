from pathlib import Path
import pandas as pd
# import openpyxl

current_dir = Path(__file__).parent

client_sheet_rs = pd.read_excel(
    current_dir / 'planilhas' / 'clientes.xlsx',
    sheet_name='RS',
    # header=0,
    # index_col=0,
    # decimal='.'
)

client_sheet_sc = pd.read_excel(
    current_dir / 'planilhas' / 'clientes.xlsx',
    sheet_name='SC',
)

with pd.ExcelWriter(current_dir / 'planilhas' / 'copia_clientes.xlsx') as new_sheet:
    client_sheet_rs.to_excel(new_sheet, sheet_name='RS', index=False)
    client_sheet_sc.to_excel(new_sheet, sheet_name='SC', index=False)

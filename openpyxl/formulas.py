from openpyxl import Workbook
from openpyxl.formula.translate import Translator

wb = Workbook()

sheet = wb.active

sheet["A1"] = 100
sheet["A2"] = 200

formula = "=SUM(A1:A2)"
sheet["A3"] = formula

sheet["B1"] = 300
sheet["B2"] = 250

sheet["B3"] = Translator(formula, origin="A3").translate_formula("B3")

wb.save("formula.xlsx")

# Saber fórmulas
from openpyxl.utils import FORMULAE

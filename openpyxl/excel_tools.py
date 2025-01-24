from openpyxl import load_workbook

# load
wb = load_workbook("exemplo.xlsx")

sheet = wb["Sheet1"]

# locate values
sheet["B2"].value
sheet.cell(row=2, column=2).value

# max rows and columns
sheet.max_row
sheet.max_column

for i in range(0, sheet.max_row):
    print(sheet.cell(row=i + 1, column=2).value)

# change value
sheet.cell(row=2, column=3).value = 75
sheet.cell(row=2, column=3).value

# save
wb.save("exemplo.xlsx")

# merging
sheet.merge_cells("A1:D1")
sheet.unmerge_cells("A1:D1")  # the values were lost!!

# delete rows & cols
sheet.insert_rows(4)
sheet.delete_rows(4)
sheet.insert_cols(2, 5)
sheet.delete_cols(2, 5)

# images
from openpyxl.drawing.image import Image

img = Image("catlogo.png")
sheet.add_image(img, "A1")

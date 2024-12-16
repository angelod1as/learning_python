# Convert to list comprehention

valores = [30, 50, 100, 120]

triplos = []
for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)

print(triplos)

# Answer
triplos = [valor * 3 for valor in valores]
print(triplos)

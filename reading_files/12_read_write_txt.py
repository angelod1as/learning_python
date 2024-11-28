from pathlib import Path

# # READING
# Not recommended way to read files
curr_folder = Path(__file__).parent

shopping_list = open(curr_folder/'shopping_list.txt')

print(shopping_list.read())

shopping_list.close()

# Recommended way to read files — "with" auto closes files
curr_folder = Path(__file__).parent

with open(curr_folder/'shopping_list.txt') as shopping_list:
    print(shopping_list.read())

# Line by line
curr_folder = Path(__file__).parent

with open(curr_folder/'shopping_list.txt') as shopping_list:
    line = shopping_list.readline()
    while line != "":
        print(line, end='')
        line = shopping_list.readline()

# All lines
curr_folder = Path(__file__).parent

with open(curr_folder/'shopping_list.txt') as shopping_list:
    print(shopping_list.readlines())


# # WRITING
# Writing files
bought = ["farinha", "fermento", "agua"]
curr_folder = Path(__file__).parent

with open(curr_folder/'shopping_list.txt') as shopping_list:
    list_items = shopping_list.readlines()

with open(curr_folder/'shopping_list_updated.txt', mode="w") as shopping_list_updated:
    for item in list_items:
        if not item.replace('\n', '') in bought:
            shopping_list_updated.write(item)

# Writing line by line
curr_folder = Path(__file__).parent
bought = ["farinha", "fermento", "agua"]

with open(curr_folder/'shopping_list.txt') as shopping_list:
    list_items = shopping_list.readlines()

updated_list = []
for item in list_items:
    if not item.replace('\n', '') in bought:
        updated_list.append(item)

with open('shopping_list_updated.txt', mode="w") as updated_file:
    updated_file.writelines(updated_list)

# Adding new files
curr_folder = Path(__file__).parent
new_items = ["sabao", "acucar"]
new_items_with_return = []

for item in new_items:
    new_items_with_return.append(f'\n{item}')

with open('shopping_list.txt', mode="a") as updated_list:
    updated_list.writelines(new_items_with_return)

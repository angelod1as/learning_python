from pathlib import Path

REMOVED_ITEM = 'Passear com cachorro'

curr_folder = Path(__file__).parent

with open(curr_folder / 'view_list.html') as html:
    html_lines = html.readlines()

new_html_lines = []
WRITELINE = True


for i, line in enumerate(html_lines):
    if i < len(html_lines) - 3 and REMOVED_ITEM in html_lines[i + 2]:
        WRITELINE = False
    if WRITELINE:
        new_html_lines.append(line)
    if '</li>' in line:
        WRITELINE = True


with open(curr_folder / 'view_list_updated.html', mode="w") as html:
    html_lines = html.writelines(new_html_lines)

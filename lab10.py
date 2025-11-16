import re
file_path = r'C:\Users\User\Desktop\moyalki.py\lab.py\lab10\mockdata.txt'
with open(file_path, "r", encoding="utf-8") as file:
    text = file.readlines()

name_pattern = r'^([A-Za-z]+)\s'
surname_pattern = r'^[A-Za-z]+\s([A-Za-z]+)'
filetype_pattern = r'\.([A-Za-z0-9]+)\b'

names = []
surnames = []
filetypes = []

for line in text:
    name = re.search(name_pattern, line)
    surname = re.search(surname_pattern, line)
    filetype = re.search(filetype_pattern, line)

    if name:
        names.append(name.group(1))
    if surname:
        surnames.append(surname.group(1))
    if filetype:
        filetypes.append(filetype.group(1))

with open("name.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(names))

with open("surname.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(surnames))

with open("typeFile.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(filetypes))

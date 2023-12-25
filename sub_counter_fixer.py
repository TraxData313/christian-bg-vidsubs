import re

file_name = str(input("File name: ")) #'your_file.txt'
encoding = int(input("Encoding (0 for windows-1251 / 1 for utf-8): "))
encoding = ['windows-1251', 'utf-8'][encoding]

# Read content from a file
with open(file_name, 'r', encoding=encoding) as file:
    file_content = file.read()

# Regular expression to match lines with a single number
pattern = re.compile(r'^\d+(\.\d+)?$')

# Replace numbers with the increasing counter
counter = 1
new_lines = []
for line in file_content.split('\n'):
    if pattern.match(line):
        new_lines.append(str(counter))
        counter += 1
    else:
        new_lines.append(line)
new_content = '\n'.join(new_lines)

# Save the modified content back to the file
with open(file_name, 'w', encoding=encoding) as output_file:
    output_file.write(new_content)
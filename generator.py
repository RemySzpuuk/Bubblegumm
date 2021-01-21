from git.manager import Manager # Used to read .gitignore
from git.scanner import Scanner # Used to scan for files/directories

template = "<html><body>%</body></html>" # % sign is a marker for where content should go
FILE_TYPES_TO_IGNORE = []
FILES_TO_IGNORE = []

# Read .gitignore
# Analyse .gitignore
odin = Manager()
odin.add_file("/git/*")
if not odin.empty:
    for item in odin.contents:
        if '*' in item:
            FILE_TYPES_TO_IGNORE.append(item.replace('*', ''))
        else:
            FILES_TO_IGNORE.append(item)

thor = Scanner()
for file in thor.find_type(".py"):
    print(file)

print(odin.contents)

# Read directories and files
# Remove any .gitignore files or file types

# Generate a basic html sitemap
            



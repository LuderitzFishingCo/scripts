import os, re, pyperclip, send2trash, shutil
fileRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+
    .
    (\d{4})
''',re.VERBOSE)
#Function to change the name of films
def change_name(name):
    name = name.replace('.',' ')
    mo = fileRegex.search(name)
    if(mo):
        name = name.split(mo.group(1), 1)
        name = name[0]
        name =  name[:-1]
    return name


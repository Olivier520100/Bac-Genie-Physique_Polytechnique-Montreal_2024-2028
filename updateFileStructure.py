import re
import os
import string

class File():
    def __init__(self,name,directory):
        self.name = name
        self.level = 0
        self.directory = directory

class Folder():
    def __init__(self,name,directory):
        self.name = name
        self.directory = directory
        self.subfolders = []
        self.files = []
        self.level = 0
        print(directory)
        print(os.listdir(directory))
        for sobjects in os.listdir(directory):
            if "."  not in objects:
                self.subfolders.append(Folder(objects,self.directory+name+"/"))

["│","├","─","└"]
f = open("README.md","r")
readme = f.read()
f.close()
file_structure_string = "test"
pattern = r"## Structure de fichier\s*```\n[\s\S]*?\n```"
a = re.search(pattern,readme)
print(a.group(0))

root = Folder("","../")

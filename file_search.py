import json
import os
from zipfile import ZipFile

message = ("""\
Incorrect Usage:
    clean.py [directory] [jsonfile]

parameters:
    directory - where the sweep will be done
    jsonfile - the file used for all the config
        look at the github example for the jsonfile format
""")

class FileSweeper:

    compress_extensions = []
    root = ""
    json_file = ""

    def __init__(self, root, file):
        self.setRoot(root)
        self.set_JSON(file)
    
    def check_dir(self):
        if not os.path.isdir(self.root):
            print("This path is invalid try again")
            exit(0)

    def getRoot(self):
        return self.root
    
    def setRoot(self, root):
        self.root = root
        self.check_dir()
    
    def set_JSON(self, file):
        self.json_file = file
        self.load_JSON()

    def load_JSON(self):
        """ load the file extensions used from json file """
        try:
            with open(self.json_file) as file:
                data = json.load(file)
                if not len(data['extensions']):
                    print("No extensions defined in the json file")
                    exit(0)
                for ext in data['extensions']: 
                    self.compress_extensions.append(ext)
        except FileNotFoundError:
            print("File is not found aborting...")
            exit(0)
        except json.decoder.JSONDecodeError:
            print("Incorrect JSON format check github pages for more information")
            exit(0)

    def get_tree_size(self, path):
        """ gets the transerve size of the tree """
        try:
            total = 0
            for entry in os.scandir(path):
                if not entry.name.startswith('.') and entry.is_dir():
                    total += self.get_tree_size(entry.path)
                else: 
                    total += entry.stat(follow_symlinks=False).st_size
        except OSError:
            pass
        return total

    def check_file_ext(self, path, file):
        """ if specific file ext zips and remove old file """
        ext = os.path.splitext(file)
        if ext[1] in self.compress_extensions and len(ext) < 3: 
            self.zip_file(path, file)

    def zip_file(self, path, file):
        """ zips the file """
        filepath = os.path.join(path, file)
        os.chdir(filepath.rsplit('/',1)[0]) # so it doesn't zip parent directories

        with ZipFile(filepath + '.zip', 'w') as zip: zip.write(file)
        os.remove(filepath)

    def search_file_tree(self):
        """ Finds the file paths directories """
        for dirName, dirs, files in os.walk(self.root, topdown=False):
            print("Found directory ", dirName)

            for f in files: self.check_file_ext(dirName, f)
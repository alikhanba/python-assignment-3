import os


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_files(self):
        if os.path.exists(self.filename):
            print("File found")
            return True
        else:
            print("File does not exist")
            return False

    def create_output_folder(self, folder='output'):
        if os.path.exists(folder):
            print("Folder found")
        else:
            os.makedirs(folder)
            print("Folder created")
        return True

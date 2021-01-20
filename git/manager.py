"""
    manager.py
    - Created by Remy Szpuk

    *To manage .gitignore files ~ this could be edited to manage other file types as well.

    Objects:
        Manager:
            empty :: Variable indicating whether gitignore is empty or not
            __init__ :: Constructor
                loki :: Scanner object
                gitignore_path :: path to project gitignore
                contents :: gitignore file contents
            add_file :: adds a file to the gitignore contents (memory)
            add_list :: adds a list of files to the gitignore contents (memory)
            unload :: moves gitignore contents (memory) into gitignore file (drive)
            load :: moves gitignore contents (drive) into gitignore contents (memory)
            dump_file :: adds a file to gitignore contents (drive)
            dump_list :: adds a list of files to gitignore contents (drive)




"""
# imports scanner class which will be used to find the project .gitignore file
from scanner import Scanner

class Manager:
    # Class variable empty will become true if their is nothing in the .gitignore file
    # Otherwise, empty will remain false.
    empty: bool = False

    def __init__(self) -> None:

        # Creates a Scanner object
        self.loki = Scanner()

        # Trying to find the .gitignore file's path
        # If the Scanner cannot find the .gitignore file's path it returns a empty string.
        self.gitignore_path: str = self.loki.find(".gitignore")

        # Checking if Scanner returned empty string
        if self.gitignore_path == "":

            # Manager creates new .gitignore in the project's directory
            f = open(f"{self.loki.project_directory}/.gitignore", 'w')
            f.close()

            # Tries to find the .gitignore path again
            # This time it should not return an empty string because
            # we just created the .gitignore file in the project's directory
            self.gitignore_path = self.loki.find(".gitignore")

        # reads .gitignore file and checks if file is empty
        with open(self.gitignore_path, 'r') as self.contents:
            if self.contents.read().replace(' ', '').replace('\n', '') == "":
                Manager.empty = True
            else:
                # If file is not empty replace file object with the file's contents
                self.contents: list = self.contents.readlines()

    # Adds file to list of file addresses (which is stored in memory)
    def add_file(self, file) -> None:
        self.contents.append(file)

    # Adds a many files to the list of file addresses (which is stored in memory)
    def add_list(self, files: list) -> None:
        for file in files:
            self.contents.append(file)

    # Unloads the list of file addresses into the .gitignore file
    def unload(self) -> None:
        with open(self.gitignore_path, 'w') as f:
            f.writelines(self.contents)
        # Clear list because file addresses are now stored in a file
        self.contents.clear()

    # Reads file and adds each line to a list of contents
    def load(self) -> None:
        with open(self.gitignore_path, 'r') as f:
            self.contents = f.readlines()

    # Dumps a file address into the .gitignore file
    def dump_file(self, file: str) -> None:
        with open(self.gitignore_path, 'a') as f:
            f.write(file)

    # Dump a list of file addresses into the .gitignore file
    def dump_list(self, files: list) -> None:
        with open(self.gitignore_path, 'a') as f:
            f.writelines(files)


if __name__ == "__main__":
    raise Exception


















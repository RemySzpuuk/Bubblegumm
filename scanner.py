"""
    Scanner.py
    - Created by Remy Szpuk

    *For finding specific files like .gitignore

    Objects:
        Scanner:
            __init__ :: Constructor
            find :: returns first match
            find_all :: returns a list of all matches
            find_type :: returns a list of files with target extension

"""
import os


class Scanner:

    # By default the project directory is assumed to be the current working directory
    # The project directory can be manually specified when a Scanner object is created
    # example:   test = Scanner("C:\project_directory")
    def __init__(self, project_directory: str = os.getcwd()) -> None:
        self.project_directory: str = project_directory

    # Attempts to find the target file using os.walk()
    # Returns the first match if an adequate file is found
    # Returns an empty string if nothing is found
    def find(self, target: str) -> str:
        for root, dirs, files in os.walk(self.project_directory):
            if target in files:
                return os.path.join(root, target)
        return ""

    # Same as find() but returns a list of all matching results
    def find_all(self, target: str) -> list:
        results: list = []
        for root, dirs, files in os.walk(self.project_directory):
            for target in files:
                results.append(os.path.join(root, target))

        return results

    # Same as find_all() but returns all files with the same extension
    def find_type(self, target: str) -> list:
        results: list = []
        for root, dirs, files in os.walk(self.project_directory):
            for file in files:
                if file.endswith(target):
                    results.append(os.path.join(root, file))
        return results


if __name__ == "__main__":
    raise Exception

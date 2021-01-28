"""
    Create by Remy Szpuk

    reader.py reads. i know it might sound dull but that's what it does and what it does best.
    It reads .gitignore, config.bubble, config_example.txt, and of course the project's directory.

    Contents:


"""
import os
from pathlib import Path
from __init__ import INIT
from distutils.util import strtobool
import json


class DirectoryAnalyser:
    def __init__(self):
        self.map = {}

    def scan_project_directory(self, file_type: str = ".html"):
        i = 0
        for root, folder, file in os.walk(os.getcwd()):
            for f in file:
                if f.endswith(file_type):
                    self.map[f"{i}"] = {"FILENAME": str(f), "PATH": str(Path(f).resolve())}
                    i += 1

    def export_map(self):
        with open("map.json", 'w') as outfile:
            outfile.write(str(self.map))

    @staticmethod
    def refactor(char, new_char):
        with open("map.json", 'r') as file:
            string = file.read()
        string = string.replace(char, new_char)
        with open("map.json", 'w') as file:
            file.write(string)


class ConfigAnalyser(INIT):
    def __init__(self):
        super().__init__()
        self.contents = []
        self.almost_tokens = []
        self.tokens = {}

    def read_config_to_contents(self):
        with open(self.config_file_directory, 'r') as config:
            self.contents = config.readlines()

        for line in self.contents:
            if line == '\n':
                self.contents.remove(line)
            if line == '' or line == ' ':
                self.contents.remove(line)

    def read_contents_to_almost_tokens(self):
        for line in self.contents:
            if '#' in line:
                self.contents.remove(line)
            if line.upper() == "USE_GIT_IGNORE":
                self.almost_tokens.append(f"{line.upper()}")
            if line.upper() == "PROJECT_DIRECTORY":
                self.almost_tokens.append(f"{line.upper()}")
            if line.upper() == "LOG_FILE_DIRECTORY":
                self.almost_tokens.append(f"{line.upper()}")
            if line.upper() == "CONFIG_FILE_DIRECTORY":
                self.almost_tokens.append(f"{line.upper()}")
            if line.upper() == "CSS_FILE_PATH":
                self.almost_tokens.append(f"{line.upper()}")
            if line.upper() == "USE_CSS_FILE":
                self.almost_tokens.append(f"{line.upper()}")
            if line.upper() == "SHOW_CONSOLE_LOG":
                self.almost_tokens.append(f"{line.upper()}")
            if line.upper() == "SHOW_FILE_LOG":
                self.almost_tokens.append(f"{line.upper()}")
            if line.upper() == "USE_HTML":
                self.almost_tokens.append(f"{line.upper()}")

    def read_almost_tokens_to_tokens(self):
        for line in self.almost_tokens:
            if ':' in line.replace(' ', '').replace('\n', ''):
                line = line.split(':')
                self.tokens[line[0]] = line[1]

        self.contents.clear()
        self.almost_tokens.clear()
        del self.contents
        del self.almost_tokens

    def read_tokens_to_class_attributes(self):
        self.use_html = bool(strtobool(self.tokens["USE_HTML"].lower()))
        self.use_css_file = bool(strtobool(self.tokens["USE_CSS_FILE"].lower()))
        self.show_console_log = bool(strtobool(self.tokens["SHOW_CONSOLE_LOG"].lower()))
        self.use_git_ignore = bool(strtobool(self.tokens["USE_GIT_IGNORE"].lower()))
        self.show_file_log = bool(strtobool(self.tokens["SHOW_FILE_LOG"].lower()))
        self.css_file_path = self.tokens["CSS_FILE_PATH"].lower()
        self.project_directory = self.tokens["PROJECT_DIRECTORY"].lower()
        self.config_file_directory = self.tokens["CONFIG_FILE_DIRECTORY"].lower()
        self.log_file_directory = self.tokens["LOG_FILE_DIRECTORY"].lower()

        self.tokens.clear()
        del self.tokens

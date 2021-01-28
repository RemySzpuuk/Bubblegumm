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

class DirectoryAnalyser(INIT):
    def __init__(self):
        super().__init__()
        self.map = []

    def scan_project_directory(self, file_type: str = ".html"):
        i = 0
        for root, folder, file in os.walk(self.project_directory):
            for f in file:
                if f.endswith(file_type):
                    self.map[i] = {str(f), str(Path(f).resolve())}
                    i += 1


class ConfigAnalyser(INIT):
    def __init__(self):
        super().__init__()
        self.contents = []
        self.almost_tokens = []
        self.tokens = {}

        with open(self.config_file_directory, 'r') as config:
            self.contents = config.readlines()

        for line in self.contents:
            if line == '\n':
                self.contents.remove(line)
            if line == '' or line == ' ':
                self.contents.remove(line)

        with self.contents as cfg:
            for line in cfg:
                if '#' in line:
                    cfg.remove(line)
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

        with self.almost_tokens as alt:
            for line in alt:
                if ':' in line:
                    line = line.split(':').replace(' ', '').replace('\n' '')
                    self.tokens[line[0]] = line[1]

        self.contents.clear()
        self.almost_tokens.clear()
        del self.contents
        del self.almost_tokens

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






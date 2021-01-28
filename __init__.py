import os
#import time

class INIT:
    def __init__(self, project_directory = os.getcwd(), config_file_directory = os.getcwd() ):
        self.project_directory = project_directory
        self.config_file_directory = config_file_directory + "/bubblegum.config"
        self.log_file_directory = config_file_directory + "/bubblegum.log"
        self.message: str  # none config method
        self.show_console_log: bool = False
        self.show_file_log: bool = False
        self.use_git_ignore: bool = False
        self.use_css_file: bool = False
        self.css_file_path: bool = False
        self.use_html: bool = True

        file = open(self.project_directory, 'w').close()
        file = open(self.config_file_directory, 'w').close()
        file = open(self.log_file_directory, 'w').close()


    # THIS IS NOT HOW YOU WRITE DECORATORS WTF
    # WHY IS THERE IN HERE? THEY SHOULD BE SEPARATE FROM THE CLASS!!!!!
    # WAS I HIGH WHEN I WRITE THIS?
    # def log_to_console(self, function, message: str = "Default message, none was provided"):
    #     if not self.show_console_log:
    #         return None
    #
    #     def logger():
    #         print(f"@{function.__name__}: {message} ~{time.time_ns()}")
    #         return function()
    #     return logger()
    #
    # def log_to_file(self, function, message: str):
    #     if not self.show_file_log:
    #         return None
    #
    #     def logger():
    #         f = open(self.log_file_directory, 'a')
    #         f.write(f"@{function.__name__}: {message} ~{time.time_ns()}")
    #         return function()
    #     return logger()

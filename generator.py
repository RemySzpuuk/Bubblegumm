"""
    Create by Remy Szpuk

    generator.py generates HTML and XML (depending upon the config file).
    This will also generate a default config file, and an example config file in
    the project's directory.

"""
from reader import INIT

class Generator(INIT):
    def __init__(self):
        super(Generator, self).__init__()

class GenerateHTML:
    def __init__(self):
        pass

class GenerateXML:
    def __init__(self):
        pass

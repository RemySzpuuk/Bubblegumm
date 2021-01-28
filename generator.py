"""
    Create by Remy Szpuk

    generator.py generates HTML and XML (depending upon the config file).
    This will also generate a default config file, and an example config file in
    the project's directory.

"""
from __init__ import INIT
import xml.etree.cElementTree as ET



class Generator(INIT):
    def __init__(self):
        super(Generator, self).__init__()

class GenerateHTML(Generator):
    def __init__(self):
        super().__init__()

        # We have the Value, now it's time to generate some nice HTML

class GenerateXML(Generator):
    def __init__(self):
        super().__init__()
        self.header = ET.Element("sitemap")
        self.sub_header = {}
        self.content = {}

    # def GenerateXMLSitemap(self):




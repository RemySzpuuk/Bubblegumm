"""
    Create by Remy Szpuk

    generator.py generates HTML and XML (depending upon the config file).
    This will also generate a default config file, and an example config file in
    the project's directory.

"""
from __init__ import INIT
import xml.etree.cElementTree as ET
import json, os


class Generator(INIT):
    def __init__(self):
        super(Generator, self).__init__()
        self.map = {}

    def import_map(self):
        try:
            with open("map.json", 'r') as _file:
                self.map = json.load(_file)
        except FileExistsError:
            print("File does not exist, error.")
            return 0
        except FileNotFoundError:
            print("File could not be found, error.")
            return 0


class GenerateHTML(Generator):
    def __init__(self):
        super().__init__()

        # TODO: Finish this HTML Generator later.


class XMLGenerator(Generator):
    def __init__(self):
        super().__init__()
        self.header = ET.Element("sitemap")

        # Each value will be linked across the dictionaries.
        # Example: id = 1, id = 1, these dictionaries will be linked when creating the sitemap.
        self.sub_headers = []
        self.links = []
        self.description = []

    def analyse_map(self):
        i = 0
        for key, value in self.map.items():
            if key == str(i):
                self.sub_headers.append(value["FILENAME"].split('.')[0])

                self.links.append(value["PATH"])
            i += 1

    def generate_xml_sitemap(self):
        for element in self.sub_headers:
            value = self.links[self.sub_headers.index(element)]
            ET.SubElement(self.header, element).text = value
        tree = ET.ElementTree(self.header)
        tree.write("sitemap.xml")
        if os.path.exists("map.json"):
            os.remove("map.json")


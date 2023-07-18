import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from argparse import ArgumentParser


class Human:
    """Class Human"""

    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        """Method to convert object to json format"""
        converted_json = json.dumps(self.__dict__, indent=4)
        self.__write_to_file(converted_json, 'json')
        # print(converted_json) # for simple print

    def convert_to_xml(self):
        """Method to convert object to xml format"""
        human_sample = vars(self)
        converted_xml = dicttoxml(human_sample, attr_type=False, custom_root='Human')
        formatted_xml = parseString(converted_xml)
        # print(formatted_xml.toprettyxml()) # for simple print
        self.__write_to_file(formatted_xml.toprettyxml(), 'xml')

    def __write_to_file(self, lines, extension):
        """
        Method to write to file
        :param lines: string to write to file
        :param extension: requested format of file
        """
        file_name = f'Human_Object.{extension}'
        with open(file_name, 'w') as file:
            file.writelines(lines)
        print(f'Human Object was written to {file_name}')


human_object = Human('Jane', 23, 'female', 2000)

parser = ArgumentParser(description='CLI parser')
parser.add_argument('--format', help='Format to convert object: json or xml')
arguments = parser.parse_args()

if arguments.format.lower() == 'json':
    human_object.convert_to_json()
elif arguments.format.lower() == 'xml':
    human_object.convert_to_xml()

from flask import Flask
from flask_restful import reqparse

class get_parameters():
    def __init___(self):
        self.__area = parser.parse_args().get("area", "None")
        self.__postalCode = parser.parse_args().get("postalCode", "None")

    def get(self):
        
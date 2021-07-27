from flask import Flask, jsonify
from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument("area", float, required = True, help = "Not all required data are given")
parser.add_argument("postalCode", int, required = True, help = "Not all required data are given")
response = {}

class get_parameters():
    def area(self):
        self.__area = parser.parse_args().get("area", "None")
        if self.__area:
            response["area"] = jsonify(self.__area)
        
    def postal_code(self):
        self.__postalCode = parser.parse_args().get("postalCode", "None")
        if len(self.__postalCode) == 4:
            response["postalCode"] = jsonify(self.__postalCode)
        else:
            return jsonify({"Warning": "Postal code exists of 4 characters"})
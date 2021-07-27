from flask import Flask, request, jsonify


response = {}

class get_parameters():
    def area(self):
        self.__area = request.args().get("area", "None")
        if self.__area:
            response["area"] = self.__area
        
    def postal_code(self):
        self.__postalCode = request.args().get("postalCode", "None")
        if len(self.__postalCode) == 4:
            response["postalCode"] = self.__postalCode
        else:
            return jsonify({"Warning": "Postal code should exist of 4 characters"})
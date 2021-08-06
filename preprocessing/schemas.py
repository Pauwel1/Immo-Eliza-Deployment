### Immmo Eliza Deployment ###
### BeCode BXL - Bouman 3.31 ###
### Pauwel De Wilde ###

# schemas to get the parameters seperately
from flask import abort

class Get_parameters:
    def __init__(self, request):
        self.request = request

    def area(self):
        area = self.request.args.get("area", None)
        if (area == None):
            abort(400, description = "Area not given (only numbers separated by a '.' are allowed)")
        else:
            return area

    def postal_code(self):
        postalCode = self.request.args.get("postalCode", None)
        if len(postalCode) == 4:
            return postalCode
        else:
            abort(400, description = "Postal code should exist of 4 intigers, without space")
    
    def subtype_property(self):
        subtypeProperty = self.request.args.get("subtypeProperty", None)
        # There should be a limited list to select from, that will be transformed to dummies with values 1 - 22
        lst = [
            "APARTMENT", "HOUSE", "MANSION", 
            "VILLA", "STUDIO", "HOUSE_GROUP", 
            "EXCEPTIONAL_PROPERTY", "MIXED_USE_BUILDING", "APARTMENT_BLOCK",
            "BUNGALOW", "CASTLE", "COUNTRY_HOUSE", 
            "TOWN_HOUSE", "MANOR_HOUSE", "GROUND_FLOOR",
            "PENTHOUSE", "KOT", "CHALET",
            "FARMHOUSE", "PAVILION", "DUPLEX",
            "LOFT", "SERVICE_FLAT", "TRIPLEX"
            ]
        if subtypeProperty in lst:
            return subtypeProperty
        else:
            abort(400, description = "Choose one of the property type options")

    def building_condition(self):
        buildingCondition = self.request.args.get("buildingCondition", None)
        # There should be a limited list to select from, that will be transformed to dummies with values 1 - 6
        lst2 = ["GOOD", "TO_RESTORE", "TO_BE_DONE_UP", "AS_NEW", "JUST_RENOVATED", "TO_RENOVATE"]
        if buildingCondition in lst2:
            return buildingCondition
        else:
            abort(400, description = "Choose one of the building condition options")
    
    def bedrooms_count(self):
        BedroomsCount = self.request.args.get("BedroomsCount", None)
        if BedroomsCount:
            return BedroomsCount
        else:
            return 0

    def facade_count(self):
        facadeCount = self.request.args.get("facadeCount", None)
        if facadeCount:
            return facadeCount
        else:
            abort(400, description = "Specify the number of facades")

    def outside_space(self):
        outsideSpace = self.request.args.get("outsideSpace", None)
        if outsideSpace:
            return outsideSpace
        else:
            abort(400, description = "Please enter the available space outside the house (terrace + garden)")

    def land_surface(self):
        landSurface = self.request.args.get("landSurface", None)
        if landSurface:
            return landSurface
        else:
            abort(400, description = "Please give the surface of the lot")

    def fireplace_exists(self):
        fireplaceExists = self.request.args.get("fireplaceExists")
        if fireplaceExists == "yes":
            return 1
        else:
            return 0
    
    def has_swimming_pool(self):
        hasSwimmingPool = self.request.args.get("hasSwimmingPool")
        if hasSwimmingPool == "yes":
            return 1
        else:
            return 0
    
    def has_garden(self):
        hasGarden = self.request.args.get("hasGarden")
        if hasGarden == "yes":
            return 1
        else:
            return 0
    
    def has_terrace(self):
        hasTerrace = self.request.args.get("hasTerrace")
        if hasTerrace == "yes":
            return 1
        else:
            return 0
    
    def has_fully_equipped_kitchen(self):
        hasFullyEquippedKitchen = self.request.args.get("hasFullyEquippedKitchen")
        if hasFullyEquippedKitchen == "yes":
            return 1
        else:
            return 0
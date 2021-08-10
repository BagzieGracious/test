"""
Module to return validations values
"""
from flask import jsonify

class DataValidation:
    @staticmethod
    def check_empty_data(data, lst):
        """
        Method tests if the params are empty
        """
        if not isinstance(DataValidation.check_data_fields(data, lst), bool):
            return DataValidation.check_data_fields(data, lst)
        
        for key in data:
            if data[key] == "":
                return jsonify({
                    "success":False,
                    "error": {
                        "code": 400,
                        "message": "No field should be empty"
                    }
                }), 400
        return True


    @staticmethod
    def check_data_fields(data, lst):
        """
        Method tests if required fields were sent
        """

        if set(list(data.keys())) == set(lst):
            return True
        return jsonify({
            "success":False,
            "error": {
                "code": 400,
                "message": ', '.join(list(set(lst) - set(list(data.keys())))) + " field(s) is/are missing"
            }
        }), 400


    @staticmethod
    def check_for_strings(data):
        """
        Method tests if the params are all strings
        """
        for key in data:
            if not isinstance(data[key], str):
                return False
        return True

    
    @staticmethod
    def check_for_integers(data):
        """
        Method tests if the params are all integers
        """
        for key in data:
            if not isinstance(data[key], int):
                return False
        return True


    @staticmethod
    def validate_user_info(data, lst=None):
        """
        Method returns the validate user information
        """
        if isinstance(DataValidation.check_empty_data(data, lst), bool):
            if DataValidation.check_for_strings(data):
                return True
            return jsonify({
                "success":False,
                "error": {
                    "code": 400,
                    "message": "Fields should be a string"
                }
            }), 400
        return DataValidation.check_empty_data(data, lst)

    
    @staticmethod
    def validate_transactions(data, lst=None):
        """
        Method returns the validate transaction information
        """
        if isinstance(DataValidation.check_empty_data(data, lst), bool):
            if DataValidation.check_for_integers(data):
                return True
            return jsonify({
                "success":False,
                "error": {
                    "code": 400,
                    "message": "Fields should be an integer"
                }
            }), 400
        return DataValidation.check_empty_data(data, lst)

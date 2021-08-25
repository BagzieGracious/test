"""
Module to handle users requests via endpoints
"""

from flask import json, request
from flask.views import MethodView
from api.models.model import Model
from api.data.data import Data
from api.config.data_validation import DataValidation

class UserController(MethodView):
    """
    Users controller that inherits the method view
    """
    users = Model(Data.users())


    @staticmethod
    def get(user_id=None):
        """
        Method that handles view of users
        """
        if user_id is None:
            return UserController.users.get_item()
        return UserController.users.get_item(user_id, 'user_id')


    @staticmethod
    def post():
        """
        Method that handles create users
        """
        post_data = request.get_json()
        post_values = DataValidation.validate_user_info(post_data, ['username', 'email', 'password'])

        if isinstance(post_values, bool):
            data_object = {
                "user_id": len(UserController.users.get_list()) + 1,
                "username": post_data['username'],
                "email": post_data['email'],
                "password": post_data['password'],
                "amount": 0.0,
                "currency": "USD"
            }
            return UserController.users.create_item(data_object)
        return post_values

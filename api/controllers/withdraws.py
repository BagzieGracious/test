"""
Module to handle deposits requests via endpoints
"""

from flask import jsonify, request
from flask.views import MethodView
from api.models.model import Model
from api.data.data import Data
from api.config.data_validation import DataValidation
from api.controllers.users import UserController

class WithdrawController(MethodView):
    """
    Withdraw controller that inherits the method view
    """
    withdraws = Model(Data.withdraws())


    @staticmethod
    def get(user_id=None):
        """
        Method that handles view of withdraw
        """
        user_data = UserController.users.get_item(user_id, 'user_id')
        if not user_data[0].get_json()['success']:
           return jsonify({"success": False, "message": "User not found"}), 404

        if user_id is None:
            return WithdrawController.withdraws.get_item()
        return WithdrawController.withdraws.get_item(user_id, 'user_id')


    @staticmethod
    def post(user_id):
        """
        Method that handles create withdraws
        """
        user_data = UserController.users.get_item(user_id, 'user_id')
        user_response = user_data[0].get_json()
        if not user_response['success']:
           return jsonify({"success": False, "message": "User not found"}), 404

        post_data = request.get_json()
        post_values = DataValidation.validate_transactions(post_data, ['amount'])

        if isinstance(post_values, bool):
            data_object = {
                "withdraw_id": len(WithdrawController.withdraws.get_list()) + 1,
                "user_id": user_id,
                "amount": post_data['amount']
            }
            user_amount = user_response['payload'][0]['amount']

            if user_amount < post_data['amount']:
                return jsonify({"success": False, "message": "Insuffient balance"}), 404
            UserController.users.update_item(user_id, 'user_id', 'amount', (user_amount - post_data['amount']))
            return WithdrawController.withdraws.create_item(data_object)
        return post_values

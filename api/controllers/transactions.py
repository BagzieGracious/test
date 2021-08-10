"""
Module to handle transactions requests via endpoints
"""

from flask import jsonify, request
from flask.views import MethodView
from api.models.model import Model
from api.data.data import Data
from api.config.data_validation import DataValidation
from api.controllers.users import UserController

class TransactionController(MethodView):
    """
    transactions controller that inherits the method view
    """
    transactions = Model(Data.transactions())


    @staticmethod
    def get(user_id=None):
        """
        Method that handles view of transactions
        """
        user_data = UserController.users.get_item(user_id, 'user_id')
        if not user_data[0].get_json()['success']:
           return jsonify({"success": False, "message": "User not found"}), 404

        if user_id is None:
            return TransactionController.transactions.get_item()
        return TransactionController.transactions.get_item(user_id, 'user_id')


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
        post_values = DataValidation.validate_transactions(post_data, ['amount', 'receiver_id'])

        if isinstance(post_values, bool):
            data_object = {
                "transaction_id": len(TransactionController.transactions.get_list()) + 1,
                "user_id": user_id,
                "amount": post_data['amount']
            }
            user_amount = user_response['payload'][0]['amount']

            if user_amount < post_data['amount']:
                return jsonify({"success": False, "message": "Insuffient balance"}), 404

            receiver_data = UserController.users.get_item(post_data['receiver_id'], 'user_id')
            receiver_response = receiver_data[0].get_json()
            if not receiver_response['success']:
                return jsonify({"success": False, "message": "Receiver not found"}), 404

            receiver_amount = receiver_response['payload'][0]['amount']
            UserController.users.update_item(post_data['receiver_id'], 'user_id', 'amount', (post_data['amount'] + receiver_amount))
            UserController.users.update_item(user_id, 'user_id', 'amount', (user_amount - post_data['amount']))
            return TransactionController.transactions.create_item(data_object)
        return post_values

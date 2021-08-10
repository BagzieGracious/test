"""
Module for rendering routes
"""
from api.controllers.users import UserController
from api.controllers.deposits import DepositController
from api.controllers.withdraws import WithdrawController
from api.controllers.transactions import TransactionController

class Routes:
    """
    Create a Routes class
    """

    @staticmethod
    def fetch_routes(app):
        """
        static method for fetching all routes
        """

        #default route
        @app.route('/')
        def index():
            return "Welcome to this Home Page"

        
        #users endpoints
        app.add_url_rule(
            '/api/v1/users/',
            view_func=UserController.as_view('createUser'),
            methods=['POST'],
            strict_slashes=False
        )

        app.add_url_rule(
            '/api/v1/users/',
            view_func=UserController.as_view('getUsers'),
            methods=['GET'],
            strict_slashes=False
        )

        app.add_url_rule(
            '/api/v1/users/<int:user_id>',
            view_func=UserController.as_view('getSingleUser'),
            methods=['GET'],
            strict_slashes=False
        )

        # depoists endpoint
        app.add_url_rule(
            '/api/v1/deposits/<int:user_id>',
            view_func=DepositController.as_view('createDeposit'),
            methods=['POST'],
            strict_slashes=False
        )

        app.add_url_rule(
            '/api/v1/deposits/<int:user_id>',
            view_func=DepositController.as_view('getUserDeposits'),
            methods=['GET'],
            strict_slashes=False
        )

        # withdraws endpoint
        app.add_url_rule(
            '/api/v1/withdraws/<int:user_id>',
            view_func=WithdrawController.as_view('createWithdraw'),
            methods=['POST'],
            strict_slashes=False
        )

        app.add_url_rule(
            '/api/v1/withdraws/<int:user_id>',
            view_func=WithdrawController.as_view('getUserWithdraw'),
            methods=['GET'],
            strict_slashes=False
        )

        # transactions endpoint
        app.add_url_rule(
            '/api/v1/transactions/<int:user_id>',
            view_func=TransactionController.as_view('createTransactions'),
            methods=['POST'],
            strict_slashes=False
        )

        app.add_url_rule(
            '/api/v1/transactions/<int:user_id>',
            view_func=TransactionController.as_view('getUserTransactions'),
            methods=['GET'],
            strict_slashes=False
        )
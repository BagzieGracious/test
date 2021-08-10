from flask import json
from run import APP

class CreateItem:

    def __init__(self):
        self.app = APP
        self.client = self.app.test_client

    def create_user(self, username, email, password):
        post = self.client().post(
            '/api/v1/users/',
            data=json.dumps(dict(
                username=username,
                email=email,
                password=password,
            )),
            content_type='application/json'
        )
        return post

    def create_deposit(self, product, quantity, price):
        post = self.client().post(
            '/api/v1/sales/',
            data=json.dumps(dict(
                product=product,
                quantity=quantity,
                price=price
            )),
            content_type='application/json'
        )
        return post
"""
Module for testing user
"""
from unittest import TestCase
from flask import json
from api.tests.create_item import CreateItem

class TestCreateUser(TestCase):
    """
    Class that inherits TestCase for testing TDD
    """

    def test_create_user(self):
        """
        Method returns create users results
        """
        post = CreateItem().create_user('Bagenda Deogratius', "bagenda@gmail.com", 'password')

        resp = json.loads(post.data.decode())
        self.assertTrue(resp['success'], True)
        self.assertTrue(resp['payload'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)

    def test_create_user(self):
        """
        Method returns create users results
        """
        post = CreateItem().create_user('Bagenda Deogratius', "", 'password')

        resp = json.loads(post.data.decode())
        self.assertTrue(resp['error']['message'], 'No field should be empty')
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)
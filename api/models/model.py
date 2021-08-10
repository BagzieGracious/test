"""
Module that acts a model, for handling data manipulation
"""
from flask import jsonify

class Model:
    """
    model class that add data to data structures
    """
    def __init__(self, lst):
        """
        constructor method that initializes a list
        """
        self.lst = lst

    def get_list(self):
        """
        method for returning actual list
        """
        return self.lst

    def get_item(self, item_id=None, item_var=None):
        """
        method for get data from data structures
        """
        items = []
        if item_id is None and item_var is None:
            return jsonify({"success":True, "payload":self.lst}), 200
        for item in self.lst:
            if item.get(item_var) == item_id:
                items.append(item)
        return jsonify({"success":True, "payload":items}), 200

    def create_item(self, item):
        """
        method for add an item in the data structure
        """
        self.lst.append(item)
        return jsonify({"success":True, "payload":item}), 201

    def update_item(self, item_id, item_var, key, value):
        """
        method for update an item in the data structure
        """
        for item in self.lst:
            if item.get(item_var) == item_id:
                item[key] = value
        return jsonify({"success":True, "payload":item}), 201

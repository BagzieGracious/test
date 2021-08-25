"""
Module that returns dummy data
"""

class Data:
    """
    class that returns data stored in data structures
    """
    @staticmethod
    def users():
        """
        Method that returns all available users
        """
        return []

    @staticmethod
    def transactions():
        """
        Method that returns all available transactions
        """
        return []

    @staticmethod
    def withdraws():
        """
        Method that returns all available withdraws
        """
        return []

    @staticmethod
    def deposits():
        """
        Method that returns all available deposists
        """
        return []

    @staticmethod
    def currencies():
        """
        Method that returns all currencies
        """
        return {
            'USD':  1,
            'Naira': 411.57,
            'Yen': 109.47,
            'Yuan': 6.46
        }

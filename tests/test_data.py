""" A module to test database """

import json
import sys
import unittest


class TestDB(unittest.TestCase):
    """ A class to test the databse files """

    def setUp(self):
        """ A method loads whatever needs before every test """
        sys.path.append('..')

    def tearDown(self):
        """ A method loads whatever needs after every test """
        pass

    def test_database(self):
        """ A method that checks databses files availability """
        db_path = './catsleep/data.json'
        with open(db_path, 'r') as rf:
            data = json.load(rf)

        print(data['audio'])
        print(data['beep'])


if __name__ == '__main__':
    test_db = TestDB()
    test_db.test_database()
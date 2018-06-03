""" Validate coastal.py functionality. """
import unittest

from mango.coastal import (coastal_data)

class TestCoastal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.example = 'foo'
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_classvar_example(self):
        assert self.example == 'foo'

    def test_coastal_data(self):
        """ Validating an example function """
        output = coastal_data()

        assert output
        assert output == True

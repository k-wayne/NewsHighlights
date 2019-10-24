import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source(
            "id", "name", "description", "url", "category", "language", "country")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

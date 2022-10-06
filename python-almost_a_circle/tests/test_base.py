import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    def test_2(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_json_to_string(self):
        r = Base.Rectangle(1,2,3,4)
        dictionary = r.todictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary), str)

    # def test_from_json_string(self):

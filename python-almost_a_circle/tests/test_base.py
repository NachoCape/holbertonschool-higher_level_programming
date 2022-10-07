import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    def test_2(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_json_to_string(self):
        r = Rectangle(1, 2, 3, 4)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary), str)

    def test_save_to_file_rectangle(self):
        Rectangle.save_to_file(None)
        Rectangle.save_to_file([])
        Rectangle.save_to_file([Rectangle(1, 2, 3, 4), Rectangle(1, 2)])

    def test_save_to_file_square(self):
        Square.save_to_file(None)
        Square.save_to_file([])
        Square.save_to_file([Square(1, 2, 3, 4), Rectangle(1, 2)])

    def test_from_json_string_rectangle(self):
        list = Rectangle.to_json_string([{'id': 89, 'width': 10}])
        dict = Rectangle.from_json_string(list)

    def test_from_json_string_Square(self):
        list = Square.to_json_string([{'id': 89, 'width': 10}])
        dict = Square.from_json_string(list)

    def test_create_rectangle(self):
        Rectangle.create(**{'width': 2, 'height': 3})

    def test_create_square(self):
        Square.create(**{'width': 2, 'height': 3})

    def test_load_from_file_rectangle(self):
        Rectangle.load_from_file()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

    def test_load_from_file_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

    # def test_from_json_string(self):

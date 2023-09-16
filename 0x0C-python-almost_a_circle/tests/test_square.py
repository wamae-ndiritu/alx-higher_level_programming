#!/usr/bin/python3
"""
Test module for class Square that inherits
from Rectangle
"""
import unittest
import io
from unittest.mock import patch
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """
    Unit Test for class Square
    """

    def test_init(self):
        """
        Test valid initialization
        """
        square = Square(5, 1, 2, 100)
        self.assertEqual(square.id, 100)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

        # Test None id
        square2 = Square(1, 3, 2, None)
        self.assertEqual(square2.size, 1)
        self.assertEqual(square2.x, 3)
        self.assertEqual(square2.y, 2)

        # Test invalid initialization
        with self.assertRaises(TypeError):
            Square("invalid")
        with self.assertRaises(ValueError):
            Square(-5)
            Square(0)
            Square(5, -1, 2)
            Square(5, 1, -2)

    def test_area(self):
        """
        Test finding area of the square
        """
        square = Square(5)
        self.assertEqual(square.area(), 25)

        square = Square(2)
        self.assertEqual(square.area(), 4)

        square = Square(13)
        self.assertEqual(square.area(), 169)

    def test_display(self):
        """
        Test display square method
        """
        # Without considering x,y dimensions
        square = Square(3)
        expected_output = "###\n###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        # Considering x,y dimensions
        square = Square(3, 1, 1)
        expected_output = "\n ###\n ###\n ###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """
        Test string representation of the Square instance
        """
        square = Square(5, 1, 2, 100)
        expected_str = "[Square] (100) 1/2 - 5"
        self.assertEqual(str(square), expected_str)

        square = Square(4, 2, 1, 12)
        expected_str = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(square), expected_str)

    def test_update(self):
        """
        Test updating public instance attributes
        """

        # Test with non-keyworded arguments
        square = Square(5, 1, 2, 100)
        square.update(200, 6, 3, 4)
        self.assertEqual(square.id, 200)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)

        s1.update(89, 2)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)

        s1.update(89, 2, 3)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 10)

        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        # Test with keyworded arguments
        s1 = Square(10, 10, 10, 10)
        s1.update(height=1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)

        s1.update(size=1, x=2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 10)

        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 1)

        s1.update(x=1, y=2, size=3)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)

    def test_to_dictionary(self):
        """
        Test for getting the instance representation
        of an object with all its attributes
        """
        square = Square(5, 1, 2, 100)
        expected_dict = {
                "id": 100,
                "size": 5,
                "x": 1,
                "y": 2
                }
        self.assertEqual(square.to_dictionary(), expected_dict)

    # Test inherited methods from Rectangle class

    def test_base_to_json_string(self):
        """
        Test the to_json_string method inherited from Rectangle
        """
        square = Square(5, 1, 2, 100)
        json_str = square.to_json_string([square.to_dictionary()])
        new_str = '[{"id": 100, "size": 5, "x": 1, "y": 2}]'
        self.assertEqual(json_str, new_str)

    def test_base_save_to_file(self):
        """
        Test the save_to_file method inherited from Rectangle
        """
        square1 = Square(5, 1, 2, 100)
        square2 = Square(3, 0, 0, 200)
        Square.save_to_file([square1, square2])

        with open("Square.json", "r") as file:
            data = file.read()
            file_data = [
                    {"id": 100, "size": 5, "x": 1, "y": 2},
                    {"id": 200, "size": 3, "x": 0, "y": 0}
                    ]
            self.assertEqual(data, Square.to_json_string(file_data))
        # Test with empty list of objects saved
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, '[]')

    def test_base_from_json_string(self):
        """
        Test the from_json_string method inherited from Rectangle
        """
        json_str = '[{"id": 100, "size": 5, "x": 1, "y": 2}]'
        data = Square.from_json_string(json_str)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 100)
        self.assertEqual(data[0]['size'], 5)
        self.assertEqual(data[0]['x'], 1)
        self.assertEqual(data[0]['y'], 2)

        json_str = None
        data = Square.from_json_string(json_str)
        self.assertEqual(data, [])

    def test_base_create(self):
        """
        Test the create method inherited from Rectangle
        """
        obj_dict = {'id': 5, 'size': 10, 'x': 3, 'y': 4}
        obj = Square.create(**obj_dict)
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.size, 10)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1 is s2, False)
        self.assertEqual(s1 == s2, False)
        s1_str = "[Square] (27) 5/1 - 3"
        s2_str = "[Square] (27) 5/1 - 3"
        self.assertEqual(str(s1), s1_str)
        self.assertEqual(str(s2), s2_str)

    def test_base_load_from_file(self):
        """
        Test the load_from_file method inherited from Rectangle
        """
        square1 = Square(5, 1, 2, 100)
        square2 = Square(3, 0, 0, 200)
        Square.save_to_file([square1, square2])

        loaded_objs = Square.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 100)
        self.assertEqual(loaded_objs[0].size, 5)
        self.assertEqual(loaded_objs[0].x, 1)
        self.assertEqual(loaded_objs[0].y, 2)
        self.assertEqual(loaded_objs[1].id, 200)
        self.assertEqual(loaded_objs[1].size, 3)
        self.assertEqual(loaded_objs[1].x, 0)
        self.assertEqual(loaded_objs[1].y, 0)

    def test_base_save_to_file_csv(self):
        """
        Test the save_to_file_csv method inherited from Rectangle
        """
        square1 = Square(5, 1, 2, 100)
        square2 = Square(3, 0, 0, 200)
        Square.save_to_file_csv([square1, square2])

        with open("Square.csv", "r") as file:
            data = file.read()
            self.assertIn("id,size,x,y", data)
            self.assertIn("100,5,1,2", data)
            self.assertIn("200,3,0,0", data)

        # Test with None list objects
        Square.save_to_file_csv(None)

        with open("Square.csv", "r") as file:
            data = file.read()
            self.assertIn("id,size,x,y", data)
            self.assertIn("", data)

    def test_base_load_from_file_csv(self):
        """
        Test the load_from_file_csv method inherited from Rectangle
        """
        square1 = Square(5, 1, 2, 100)
        square2 = Square(3, 0, 0, 200)
        Square.save_to_file_csv([square1, square2])

        loaded_objs = Square.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 100)
        self.assertEqual(loaded_objs[0].size, 5)
        self.assertEqual(loaded_objs[0].x, 1)
        self.assertEqual(loaded_objs[0].y, 2)
        self.assertEqual(loaded_objs[1].id, 200)
        self.assertEqual(loaded_objs[1].size, 3)
        self.assertEqual(loaded_objs[1].x, 0)
        self.assertEqual(loaded_objs[1].y, 0)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Test module for testing class Rectangle with all
its methods including the methods being inherited
from the parent class Base
"""
import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """
    Unit Test for class Rectangle
    """
    def test_init(self):
        """
        Test valid initialization
        """
        rect = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rect.id, 100)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

        # Test None id
        rect2 = Rectangle(1, 3, 1, 2, None)
        self.assertEqual(rect2.width, 1)
        self.assertEqual(rect2.height, 3)
        self.assertEqual(rect2.x, 1)
        self.assertEqual(rect2.y, 2)

        rect3 = Rectangle(10, 7, 6, 8, None)
        self.assertEqual(rect3.width, 10)
        self.assertEqual(rect3.height, 7)
        self.assertEqual(rect3.x, 6)
        self.assertEqual(rect3.y, 8)

        # Test invalid initialization
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 1, 2)
            Rectangle(1, 'height', 1, 1)
            Rectangle(1, 2, 'x', 1)
            Rectangle(1, 2, 4, '6')
            Rectangle('width', 'height', 'x', 'y')
            Rectangle(0.4, 3.2, 2.0, 1.0)

        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 1, 2)
            Rectangle(5, 0, 1, 2)
            Rectangle(5, 10, -1, 2)
            Rectangle(5, 10, 1, -2)

    def test_area(self):
        """
        Test finding area of the rectangle
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

        rect = Rectangle(2, 4)
        self.assertEqual(rect.area(), 8)

        rect = Rectangle(13, 7)
        self.assertEqual(rect.area(), 91)

    def test_display(self):
        rect = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """
        Test string representation of the Rectangle instance
        """
        rect = Rectangle(5, 10, 1, 2, 100)
        expected_str = "[Rectangle] (100) 1/2 - 5/10"
        self.assertEqual(str(rect), expected_str)

        rect = Rectangle(4, 6, 2, 1, 12)
        expected_str = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(rect), expected_str)

        rect = Rectangle(5, 5, 1)
        expected_str = "[Rectangle] (20) 1/0 - 5/5"
        self.assertEqual(str(rect), expected_str)

    def test_update(self):
        """
        Test updating public instance attributes
        """

        # Test with non-keyworded arguments
        rect = Rectangle(5, 10, 1, 2, 100)
        rect.update(200, 6, 12, 3, 4)
        self.assertEqual(rect.id, 200)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        # Test with keyworded arguments
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 10)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)

    def test_to_dictionary(self):
        """
        Test for getting the instance representation
        of an object with all it's attribute
        """
        rect = Rectangle(5, 10, 1, 2, 100)
        expected_dict = {
                "id": 100,
                "width": 5,
                "height": 10,
                "x": 1,
                "y": 2
                }
        self.assertEqual(rect.to_dictionary(), expected_dict)

    # Test inherited methods from Base class

    def test_base_to_json_string(self):
        """
        Test the to_json_string method inherited from Base
        """
        rect = Rectangle(5, 10, 1, 2, 100)
        json_str = rect.to_json_string([rect.to_dictionary()])
        new_str = '[{"id": 100, "width": 5, "height": 10, "x": 1, "y": 2}]'
        self.assertEqual(json_str, new_str)

    def test_base_save_to_file(self):
        """
        Test the save_to_file method inherited from Base
        """
        rect1 = Rectangle(5, 10, 1, 2, 100)
        rect2 = Rectangle(3, 7, 0, 0, 200)
        Rectangle.save_to_file([rect1, rect2])

        with open("Rectangle.json", "r") as file:
            data = file.read()
            file_data = [
                    {"id": 100, "width": 5, "height": 10, "x": 1, "y": 2},
                    {"id": 200, "width": 3, "height": 7, "x": 0, "y": 0}
                    ]
            self.assertEqual(data, Rectangle.to_json_string(file_data))
        # Test with empty list objects saved
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertEqual(data, '[]')

    def test_base_from_json_string(self):
        """
        Test the from_json_string method inherited from Base
        """
        json_str = '[{"id": 100, "width": 5, "height": 10, "x": 1, "y": 2}]'
        data = Rectangle.from_json_string(json_str)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 100)
        self.assertEqual(data[0]['width'], 5)
        self.assertEqual(data[0]['height'], 10)
        self.assertEqual(data[0]['x'], 1)
        self.assertEqual(data[0]['y'], 2)

        json_str = None
        data = Rectangle.from_json_string(json_str)
        self.assertEqual(data, [])

    def test_base_create(self):
        """
        Test the create method inherited from Base
        """
        obj_dict = {'id': 5, 'width': 10, 'height': 20, 'x': 3, 'y': 4}
        obj = Rectangle.create(**obj_dict)
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)
        r1_str = "[Rectangle] (8) 1/0 - 3/5"
        r2_str = "[Rectangle] (8) 1/0 - 3/5"
        self.assertEqual(str(r1), r1_str)
        self.assertEqual(str(r2), r2_str)

    def test_base_load_from_file(self):
        """
        Test the load_from_file method inherited from Base
        """
        rect1 = Rectangle(5, 10, 1, 2, 100)
        rect2 = Rectangle(3, 7, 0, 0, 200)
        Rectangle.save_to_file([rect1, rect2])

        loaded_objs = Rectangle.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 100)
        self.assertEqual(loaded_objs[0].width, 5)
        self.assertEqual(loaded_objs[0].height, 10)
        self.assertEqual(loaded_objs[0].x, 1)
        self.assertEqual(loaded_objs[0].y, 2)
        self.assertEqual(loaded_objs[1].id, 200)
        self.assertEqual(loaded_objs[1].width, 3)
        self.assertEqual(loaded_objs[1].height, 7)
        self.assertEqual(loaded_objs[1].x, 0)
        self.assertEqual(loaded_objs[1].y, 0)

    def test_base_save_to_file_csv(self):
        """
        Test the save_to_file_csv method inherited from Base
        """
        rect1 = Rectangle(5, 10, 1, 2, 100)
        rect2 = Rectangle(3, 7, 0, 0, 200)
        Rectangle.save_to_file_csv([rect1, rect2])

        with open("Rectangle.csv", "r") as file:
            data = file.read()
            self.assertIn("id,width,height,x,y", data)
            self.assertIn("100,5,10,1,2", data)
            self.assertIn("200,3,7,0,0", data)

        # Test with None list objects
        Rectangle.save_to_file_csv(None)

        with open("Rectangle.csv", "r") as file:
            data = file.read()
            self.assertIn("id,width,height,x,y", data)
            self.assertIn("", data)

    def test_base_load_from_file_csv(self):
        """
        Test the load_from_file_csv method inherited from Base
        """
        rect1 = Rectangle(5, 10, 1, 2, 100)
        rect2 = Rectangle(3, 7, 0, 0, 200)
        Rectangle.save_to_file_csv([rect1, rect2])

        loaded_objs = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 100)
        self.assertEqual(loaded_objs[0].width, 5)
        self.assertEqual(loaded_objs[0].height, 10)
        self.assertEqual(loaded_objs[0].x, 1)
        self.assertEqual(loaded_objs[0].y, 2)
        self.assertEqual(loaded_objs[1].id, 200)
        self.assertEqual(loaded_objs[1].width, 3)
        self.assertEqual(loaded_objs[1].height, 7)
        self.assertEqual(loaded_objs[1].x, 0)
        self.assertEqual(loaded_objs[1].y, 0)


if __name__ == '__main__':
    unittest.main()

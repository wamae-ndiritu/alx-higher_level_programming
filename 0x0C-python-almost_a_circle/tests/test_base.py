#!/usr/bin/python3
"""
Test module for class base and
its methods
"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """
    Tests class Base and all it's method
    """
    def test_init(self):
        """
        Test initialization of the class attribute id
        """
        obj = Base()
        self.assertEqual(obj.id, 1)

        obj2 = Base(10)
        self.assertEqual(obj2.id, 10)

        obj3 = Base()
        self.assertEqual(obj3.id, 2)

    def test_to_json_string(self):
        """
        Test conversion to JSON string representation
        """
        with self.assertRaises(AttributeError):
            obj = Base()
            json_str = Base.to_json_string([obj.to_dictionary()])

    def test_save_to_file(self):
        """
        Test saving objects to a file
        """
        with self.assertRaises(AttributeError):
            obj1 = Base(1)
            obj2 = Base(2)
            Base.save_to_file([obj1, obj2])

    def test_from_json_string(self):
        """
        Test for converting from JSON string
        """
        json_str = '[{"id": 1}, {"id": 2}]'
        data = Base.from_json_string(json_str)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[1]['id'], 2)

    def test_create(self):
        """
        Test for method create that creates an instance of
        it's class
        """
        # Attempt to use create method directly in the Base class
        with self.assertRaises(TypeError):
            obj_dict = {'id': 5, 'width': 10, 'height': 20}
            obj = Base.create(**obj_dict)

    def test_load_from_file(self):
        """
        Test loading JSON from a file
        """
        with self.assertRaises(AttributeError):
            obj1 = Base(1)
            obj2 = Base(2)
            Base.save_to_file([obj1, obj2])
            loaded_objs = Base.load_from_file()

    def test_save_to_file_csv(self):
        """
        Test saving to a csv file
        """
        with self.assertRaises(AttributeError):
            obj1 = Base(1)
            obj2 = Base(2)
            Base.save_to_file_csv([obj1, obj2])

    def test_load_from_file_csv(self):
        """
        Test loading data from a csv file
        """
        with self.assertRaises(AttributeError):
            obj1 = Base(1)
            obj2 = Base(2)
            Base.save_to_file_csv([obj1, obj2])
            loaded_objs = Base.load_from_file_csv()


if __name__ == '__main__':
    unittest.main()

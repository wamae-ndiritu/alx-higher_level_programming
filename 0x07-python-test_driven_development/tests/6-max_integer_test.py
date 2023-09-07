#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test case for function max_integer
    """

    def test_max_integer(self):
        """Test with a list of integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_empty_list(self):
        """Test with an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_dupliacate_max(self):
        """Test with duplicate maximun values
        """
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    def test_negative_values(self):
        """Test with negative values
        """
        self.assertEqual(max_integer([-5, -3, -10, -1]), -1)

    def test_non_int_list_value(self):
        """
        Test with non-integer list values
        """
        
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, '4', 5])

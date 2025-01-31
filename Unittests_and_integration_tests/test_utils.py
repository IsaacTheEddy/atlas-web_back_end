#!/usr/bin/env python3
"""This is my test module for Utils.py"""
from utils import access_nested_map
from parameterized import parameterized
import unittest
from unittest import mock

class TestAccessNestedMap(unittest.TestCase):
    """This class is used for Utils.py Test Cases"""


    @parameterized.expand([
        ({'a': 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, param1, param2, expectedResult):
        """This will test access.tested_maps methodfrom utils.py"""
        self.assertEqual(access_nested_map(nested_map=param1, path=param2), expectedResult)


#!/usr/bin/env python3
"""This is my test module for Utils.py"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from parameterized import parameterized
import json


import requests

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


    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, {"a", "b"})
        ])
    def test_access_nested_map_exception(self, param1, param2,):
        """This will test for and Report Key Errors for the
        access method Class"""
        with self.assertRaises(expected_exception=KeyError):
            access_nested_map(nested_map=param1, path=param2)

class TestGetJson(unittest.TestCase):
    """Test class is used for Utils.py GetJson Cases"""

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, param, expectedResult):
        '''This should mock requests. get and assert if
        the call is made once'''
        mock = Mock()
        mock.json.return_value = expectedResult
        with patch('requests.get') as mock_get:
            mock_get.return_value = mock
            self.assertEqual(get_json(param), expectedResult)
            mock_get.assert_called_once_with(param)

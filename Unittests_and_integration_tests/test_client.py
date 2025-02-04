#!/usr/bin/env python3
"""This module is for testing the clients modules"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """This class is for the testing of the
    GitHubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, param, mock_get):
        """Tests the get_json of call"""
        test = GithubOrgClient(param)
        test.org
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{param}")

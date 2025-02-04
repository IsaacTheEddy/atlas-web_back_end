#!/usr/bin/env python3
"""This module is for testing the clients modules"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
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

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_get):
        """Mocks the property method"""
        mock_get.return_value = {'repos_url': 'https://api.github.com/orgs/google/repos'}
        test = GithubOrgClient('google')
        test.org
        results = test._public_repos_url
        self.assertEqual(results, 'https://api.github.com/orgs/google/repos')


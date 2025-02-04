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

    @patch('client.get_json')
    def test_public_repos(self, mock_jock):
        """Mocks clients get_json and _public_repose
        to check that its the mocked value"""
        mock_jock.return_value =[ {'name': "money, money"}, {'name': "moneeye"}]
        test = GithubOrgClient('google')
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)\
        as mock_prop:
            mock_prop.return_value = 'https://api.github.com/orgs/google/repos'
            results = test.public_repos()
            self.assertEqual(results, ["money, money", "moneeye"])

    @parameterized.expand([({"license": {"key": "my_license"}},"my_license", True),
                           ({"license": {"key": "other_license"}},"my_license", False)])
    def test_has_license(self, param1, param2, expectedResult):
        """Test if user has license"""
        test = GithubOrgClient("google")
        result = test.has_license(param1, param2)
        self.assertEqual(result, expectedResult)

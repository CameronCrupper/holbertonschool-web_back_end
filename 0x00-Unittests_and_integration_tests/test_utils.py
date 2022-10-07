#!/usr/bin/env python3
"""
Test Utils
"""
import unittest
import math
from utils import access_nested_map, memoize, get_json
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
import requests


class TestAccessNestedMap(unittest.TestCase):
    """
    Access Nested Map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path_map, result_expec):
        """
        test access nested map
        """
        self.assertEqual(access_nested_map(nested_map, path_map), result_expec)
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path_map):
        """
        test access nested map acception
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path_map)
        self.assertEqual(
            f'KeyError({str(error.exception)})', repr(error.exception))


class TestGetJson(unittest.TestCase):
    """
    test get json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test get json
        """
        with patch('request.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    test memoize
    """
    def test_memoize(self):
        """
        test memoize
        """
        class TestClass:
            """
            test class
            """

            def a_method(self):
                """
                a method
                """
                return 42
            @memoize
            def a_property(self):
                """
                a property
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class =TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()

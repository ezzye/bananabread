#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock
from get_page_structure import get_webpage_content, get_element_dict


class TestWebpageContent(unittest.TestCase):

    def test_get_webpage_content(self):
        # Set up mock HTML element
        mock_session = MagicMock()
        mock_element = MagicMock()
        mock_response = MagicMock()

        mock_element.attrs = {"class": "test", "id": "long_attribute_value"}
        mock_element.text = "Test text"
        mock_element.tag = "div"
        mock_element.element.iterchildren.return_value = []

        mock_session.get.return_value = mock_response

        mock_response.html.find.return_value = mock_element

        result = get_webpage_content("https://www.example.com", mock_session)

        # Validate the result
        expected_result = {
            "tag": "div",
            "attributes": {"class": "test"},
            "text": "Test text",
            "children": []
        }
        self.assertEqual(result, expected_result)

    def test_get_element_dict(self):
        # Set up mock HTML element
        mock_element = MagicMock()
        mock_element.attrs = {"class": "test", "id": "long_attribute_value"}
        mock_element.text = "Test text"
        mock_element.tag = "div"
        mock_element.element.iterchildren.return_value = []

        result = get_element_dict(mock_element)

        # Validate the result
        expected_result = {
            "tag": "div",
            "attributes": {"class": "test"},
            "text": "Test text",
            "children": []
        }
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

"""Test script for titlecase.py file"""

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from titlecase.titlecase import title_case


class TestTitleCase:
    """Module for Unit test"""

    def test_lower_text_is_uppercased(self):
        """To test the units"""
        initial_text = "this should be capitalized"
        expected_text = "This Should Be Capitalized"
        returned_text = title_case(initial_text)
        assert expected_text == returned_text

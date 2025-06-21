# python imports
import unittest

# application imports
from functions.get_files_info import get_files_info

"""
# Create tests for the get_files_info func:
# get_files_info("calculator", ".") and print the result to the console.
# get_files_info("calculator", "pkg") and print the result to the console.
# get_files_info("calculator", "/bin") and print the result to the console
    # (this should return an error string)
# get_files_info("calculator", "../") and print the result to the console
    # (this should return an error string)
"""


class TestGetFilesInfo(unittest.TestCase):
    def test_valid_dir(self):
        result = get_files_info("calculator", ".")
        print("\nResult for '.':\n", result)
        self.assertIn("-", result)  # basic sanity check

    def test_subdir(self):
        result = get_files_info("calculator", "pkg")
        print("\nResult for 'pkg':\n", result)
        self.assertIn("is_dir=", result)

    def test_invalid_dir(self):
        result = get_files_info("calculator", "/bin")
        print("\nResult for '/bin':\n", result)
        self.assertTrue(result.startswith("Error:"))

    def test_outside_working_dir(self):
        result = get_files_info("calculator", "../")
        print("\nResult for '../':\n", result)
        self.assertTrue(result.startswith("Error:"))

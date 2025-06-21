# python imports

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

def main():
    test_valid_dir()
    test_invalid_dir()
    test_subdir()
    test_outside_working_dir()

def test_valid_dir():
    result = get_files_info("calculator", ".")
    print("\nResult for '.':\n", result)

def test_subdir():
    result = get_files_info("calculator", "pkg")
    print("\nResult for 'pkg':\n", result)

def test_invalid_dir():
    result = get_files_info("calculator", "/bin")
    print("\nResult for '/bin':\n", result)

def test_outside_working_dir():
    result = get_files_info("calculator", "../")
    print("\nResult for '../':\n", result)

if __name__ == "__main__":
    main()
import unittest
from Password_checker.password_checker import Verification

#password_is_valid will check if the password meets a few different conditions.
#If one of the below conditions is not met then the relevant
#error/exception should be thrown/raised.
#Your error/exception message should match one of the following conditions exactly (word-for-word).

#    password should exist
#    password should be longer than than 8 characters
#    password should have at least one lowercase letter
#    password should have at least one uppercase letter
#    password should at least have one digit
#    password should have at least one special character

#Creat an instance of the password checker class
#verification = Verification()


#Testing if the password returns True on at least 3 conditions
import unittest

validate = Verification()

# class Test_Password_Checker(unittest.TestCase):

# Test if password has less than 8 characters
def test_pass_length():
    assert validate.Verification() == True


# Test if password has atleast one special character
def test_pass_characters():
    pass


# Test if password has atleast one numeric value
def test_pass_numbers():
    pass


# Test if password has atleast one lowercase letter
def test_pass_lowercase():
    pass


# Test if password has atleast one uppercase letter
def test_pass_uppercase():
    pass


if __name__ == '__main__':
    unittest.main()
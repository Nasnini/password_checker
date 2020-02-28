from Password_checker.password_checker import Verification
import unittest

# If the given password meets at least three of the conditions listed above then
# this function should return true, otherwise it should return false.
# Add a feature: the password is never OK if conditions 1 and 2 are not met.

# Instance of the Verification class
# verification = Verification()

# Testing if the password exist in password_checker

class Test_Password_Checker(unittest.TestCase):

    #Test if password has less than 8 characters
    def test_pass_length(self):
        pass

    #Test if password has atleast one special character
    def test_pass_characters(self):
        pass

    #Test if password has atleast one numeric value
    def test_pass_numbers(self):
        pass

    #Test if password has atleast one lowercase letter
    def test_pass_lowercase(self):
        pass

    #Test if password has atleast one uppercase letter
    def test_pass_uppercase(self):
        pass

if __name__ == '__main__':
    unittest.main()

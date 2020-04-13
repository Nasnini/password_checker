from Password_checker.password_checker import Verification
import unittest

# If the given password meets at least three of the conditions listed above then
# this function should return true, otherwise it should return false.
# Add a feature: the password is never OK if conditions 1 and 2 are not met.

# Instance of the Verification class
# verification = Verification()

# Testing if the password exist in password_checker

class Test_Password_Checker(unittest.TestCase):

    password = "UmuziCohort2020#"
    password_checker = Password_Checker(password)

    def test_password_is_ok():
        assert password_checker.password_is_ok(password)==True
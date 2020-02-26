import unittest
from password_checker.password_checker import Verification

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
verification = Verification()


#Testing if the password returns True on at least 3 conditions
def test_password_is_okay():
    assert Verification == 'thk', "Password must be at least 8 letters"
    assert Verification == '[0-9]', "Password must contain one number"
    assert Verification == '@%$^@', "Password must contain one special character"


    #Test is True if it passes the 3 conditions

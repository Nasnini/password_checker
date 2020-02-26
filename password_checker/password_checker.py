import re


class Verification():
    def __init__(self):
        pass

    password = 'UmuziCohort$20'

    x = True
    while x:
        if len(password) < 8:
            print("Password should be longer than 8 characters.")
            break
        elif not re.search("[a-z]", password):
            print("Password should have at least one lowercase letter.")
            break
        elif not re.search("[0-9]", password):
            print("Password should have at lease one digit.")
            break
        elif not re.search("[A-Z]", password):
            print("Password should have at least one uppercase letter.")
            break
        elif not re.search("[$#@!%^?<>&*()_+]", password):
            print("Password should have at least one special character")
            break
        elif not re.search("[$s]", password):
            print("Password does not exist.")
            break
        else:
            print("Valid password")
            x = False

    if x:
        print("Not a Valid Password")

import re


class Verification():
    def __init__(self):
        pass

    password = 'QWEYTRY4546as@'

    x = True
    while x:
        if len(password) < 8:
            raise Exception("Password should be longer than 8 characters.")
            break
        elif not re.search("[a-z]", password):
            raise Exception("Password should have at least one lowercase letter.")
            break
        elif not re.search("[0-9]", password):
            raise Exception("Password should have at lease one digit.")
            break
        elif not re.search("[A-Z]", password):
            raise Exception("Password should have at least one uppercase letter.")
            break
        elif not re.search("[$#@!%^?<>&*()_+]", password):
            raise Exception("Password should have at least one special character")
            break
        elif not re.search("[$s]", password):
            raise Exception("Password does not exist.")
            break
        else:
            print("Valid password")
            x = False

    if x:
        raise Exception("Not a Valid Password")

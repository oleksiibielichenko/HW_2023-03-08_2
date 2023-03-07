# Register
# 1) Get user name
# 2) Email
# 3) Password
# 4) Confirm password
#
# Check -> True / False
# get value to check and statement for requirements

user_name = input('Enter your name: ')
user_email = input('Enter your email: ')
user_password = input('Enter your password: ')
is_valid = None


def name_validation():
    global user_name
    if len(user_name) < 2:
        return False
    else:
        return True


def email_validation():
    global user_email
    if '@' in user_email and '.' in user_email:
        return True
    else:
        return False


def password_validation():
    global user_password
    if len(user_password) > 6:
        return True
    else:
        return False


def registration():
    global is_valid

    is_valid_name = name_validation()
    is_valid_email = email_validation()
    is_valid_password = password_validation()

    if is_valid_name and is_valid_email and is_valid_password:
        is_valid = True
        print('It is valid data')
    else:
        is_valid = False
        print('It is invalid data')


print(is_valid)
registration()
print(is_valid)

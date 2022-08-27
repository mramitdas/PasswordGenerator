import string
import random


# Compact Version
print(''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*()_-:;"<>.,?/') for i in range(int(input()))]))


# Extended Version
def password(x):
    capital_letters = string.ascii_uppercase
    small_letters = string.ascii_lowercase
    number = string.digits
    special = '!@#$%^&*()_-:;"<>.,?/'

    combined = capital_letters + small_letters + number + special

    return ''.join([random.choice(combined) for i in range(x)])


if __name__ == "__main__":
    print(password(int(input())))

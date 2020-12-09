import random
import string


LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = "_+-!"


def generate_id(length=10):
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 8
        if nothing is specified.
    :returns string <class 'str'>
    '''

    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'


    printable = list(printable)
    random.shuffle(printable)


    user_id = random.choices(printable, k=length)
    user_id = ''.join(user_id)
    return user_id

#def generate_id(number_of_small_letters=4,
#                number_of_capital_letters=2,
#                number_of_digits=2,
#                number_of_special_chars=2,
#                allowed_special_chars=r"_+-!"):
#
    #return user_id

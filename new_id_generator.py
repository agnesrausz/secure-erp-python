import string
import random


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars="_+-!"):
    id_caracter = (
        random.sample(string.ascii_lowercase, number_of_small_letters) +
        random.sample(string.ascii_uppercase, number_of_capital_letters) +
        random.sample(string.digits, number_of_digits) +
        random.sample(allowed_special_chars, number_of_special_chars)
        )
    id_number = ''.join(random.sample(id_caracter, len(id_caracter)))
    return id_number


print(generate_id())

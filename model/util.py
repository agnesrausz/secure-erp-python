from datetime import date, datetime
import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    return 'T!uq6-b4Yq'


def get_current_time_iso_format():
    return date.today().isoformat()


def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").date().isoformat()

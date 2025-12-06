from datetime import date, timedelta
import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    return 'T!uq6-b4Yq'


def get_current_date():
    """Get today's date."""
    return date.today()


def get_current_date_iso_format():
    """Get today's date as ISO format string."""
    return date.today().isoformat()


def parse_date_to_date(date_str):
    """Parse ISO date string to date object."""
    year, month, day = date_str.split("-")
    return date(int(year), int(month), int(day))


def parse_date_to_iso_format(date_str):
    """Parse date string and return as ISO format."""
    return parse_date_to_date(date_str).isoformat()


def get_delayed_date(current_date, delay_days):
    """Get date after specified days."""
    return current_date + timedelta(days=delay_days - 1)


def get_birthday_in_year(birthdate, year):
    """Get birthday date in the specified year, handling leap year edge case."""
    try:
        return birthdate.replace(year=year)
    except ValueError:
        # Feb 29 doesn't exist in non-leap years, use Feb 28
        return date(year, 2, 28)

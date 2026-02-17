from datetime import datetime
from operator import ge
from webbrowser import get


def get_days_from_today(date: str) -> int:
    """Return the number of days between a given date and today.

    The input date must be in 'YYYY-MM-DD' format.
    Positive value means the date is in the past,
    negative value means the date is in the future.
    """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as error:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.") from error

    today = datetime.today().date()
    return (today - given_date).days


# if __name__ == "__main__":
#     print(get_days_from_today("2027-10-09"))


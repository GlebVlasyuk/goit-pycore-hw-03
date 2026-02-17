from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """Get users with birthdays in next 7 days (including today).

    Receives: list of dicts like {"name": str, "birthday": "YYYY.MM.DD"}.
    Logic: checks upcoming birthdays and moves weekend congratulations to Monday.
    Returns: list of dicts like {"name": str, "congratulation_date": "YYYY.MM.DD"}.
    """
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        if "name" not in user or "birthday" not in user:
            continue

        try:
            born_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            continue

        current_year_birthday = born_date.replace(year=today.year)
        if current_year_birthday < today:
            current_year_birthday = current_year_birthday.replace(year=today.year + 1)

        if current_year_birthday < today or current_year_birthday > end_date:
            continue

        congratulation_date = current_year_birthday
        weekday = congratulation_date.weekday()

        if weekday == 5:
            congratulation_date = congratulation_date + timedelta(days=2)
        elif weekday == 6:
            congratulation_date = congratulation_date + timedelta(days=1)

        result.append(
            {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            }
        )

    return result


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.02.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Bob", "birthday": "1990.02.22"},
    ]

    print("Привітати:", get_upcoming_birthdays(users))

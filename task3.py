import re


def normalize_phone_number(phone_number: str) -> str:
    """Normalize phone number to +380XXXXXXXXX style."""
    # Keep only digits and "+".
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    # Remove "+" from everywhere except possible first symbol.
    if cleaned.startswith("+"):
        digits = re.sub(r"\D", "", cleaned[1:])
    else:
        digits = re.sub(r"\D", "", cleaned)

    if digits.startswith("380"):
        return f"+{digits}"

    return f"+38{digits}"


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone_number(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

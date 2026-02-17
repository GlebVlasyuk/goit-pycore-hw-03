import random


def get_numbers_ticket(min, max, quantity):
    """Generate sorted unique random numbers for a lottery ticket."""
    # All inputs must be integers.
    if not isinstance(min, int):
        return []
    if not isinstance(max, int):
        return []
    if not isinstance(quantity, int):
        return []

    # Validate lottery limits from the task.
    if min < 1:
        return []
    if max > 1000:
        return []
    if min > max:
        return []

    count_of_numbers_in_range = max - min + 1
    if quantity < 1:
        return []
    if quantity > count_of_numbers_in_range:
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers


if __name__ == "__main__":
    result = get_numbers_ticket(1, 49, 4)
    print(result)

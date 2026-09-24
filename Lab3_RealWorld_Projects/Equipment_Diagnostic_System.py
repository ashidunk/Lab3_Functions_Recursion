# CODE 1

LAST_NAME = "SABARIAGA"
SEED_NUM = 2
FAVORITE_ARTIST = "MICO"


def generate_readings():
    readings = [
        SEED_NUM * 10,
        len(LAST_NAME) * 5,
        len(FAVORITE_ARTIST) * 10
    ]
    return readings


def validate_reading(value):
    try:
        if value >= 0 and value <= 100:
            return True
        else:
            return False
    except TypeError:
        return False


def calculate_average(readings):
    return sum(readings) / len(readings)


def classify_equipment(average):
    if average >= 75:
        return "NORMAL"
    elif average >= 50:
        return "WARNING"
    else:
        return "CRITICAL"


def logger(func):
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@logger
def diagnostic():
    readings = generate_readings()

    valid = []
    invalid = []

    for reading in readings:
        if validate_reading(reading):
            valid.append(reading)
        else:
            invalid.append(reading)

    if len(valid) > 0:
        average = calculate_average(valid)
        condition = classify_equipment(average)
    else:
        average = 0
        condition = "NO VALID DATA"

    print("Generated Equipment Data:", readings)
    print("Valid Readings:", valid)
    print("Invalid Readings:", invalid)
    print("Average:", round(average, 2))
    print("Equipment Condition:", condition)

    return condition


result = diagnostic()

print("Final Output:", result)
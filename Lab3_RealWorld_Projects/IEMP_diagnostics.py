def validate(value):
    try:
        if value >= 0 and value <= 100:
            return True
        else:
            return False
    except TypeError:
        return False


def analyze_fault(value):
    if value <= 75:
        return 0

    return analyze_fault(value - 10) + 1


def logger(func):
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@logger
def diagnostic(readings):
    valid = []
    invalid = []
    abnormal = []

    for value in readings:
        if validate(value):
            valid.append(value)

            if value > 75:
                abnormal.append(value)
        else:
            invalid.append(value)

    return valid, invalid, abnormal
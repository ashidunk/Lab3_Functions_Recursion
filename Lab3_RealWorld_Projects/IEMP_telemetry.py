def generate_telemetry(last_name, seed_num, artist):
    values = [
        seed_num * 10,
        len(last_name) * 5,
        len(artist) * 10,
        seed_num * 20,
        len(last_name) * 10
    ]

    for value in values:
        yield value


def process_data(data):
    return list(map(lambda x: x + 5, data))
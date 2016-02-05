import time


def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.time
        delta = current_time - (last_time or current_time)
        last_time = time.time
        yield delta, item

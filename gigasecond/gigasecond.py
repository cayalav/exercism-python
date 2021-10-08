from datetime import timedelta


def add(moment):
    gigasecond = 1000000000
    future = moment + timedelta(seconds=gigasecond)
    return future
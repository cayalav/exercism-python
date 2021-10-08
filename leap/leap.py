def leap_year(year):
    mod = divider(year)
    return mod(4) and not mod(100) or mod(400)

def divider(year):
    return lambda d: year % d == 0
                
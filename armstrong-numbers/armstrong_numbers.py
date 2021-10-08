def is_armstrong_number(number):
    digits = str(number)
    power = len(str(number))
    for digit in digits:
        digit_raised = int(digit)**power
        number -= digit_raised
    if number:
        return False
    else:
        return True
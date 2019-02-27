def IsValidChannel(num):
    if num >= 0 or num <= 15:
        return True
    else: 
        return False

def EnsureInteger(input):
    if isinstance(input, int):
        return input
    elif isinstance(input, str):
        if input.isnumeric(): 
            return int(input)
        else:
            raise Exception("EnsureInteger cannot parse string to valid Int")
    else:
        raise Exception("EnsureInteger was not able to parse a Str or Int")


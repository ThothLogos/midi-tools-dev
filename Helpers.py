def IsValidChannel(num):
    if num >= 0 and num <= 15:
        return True
    else: 
        return False

def EnsureInteger(input):
    if isinstance(input, int):
        return int(str(input).lstrip("0") or "0")
    elif isinstance(input, str) and input.isnumeric():
        return int(input.lstrip("0") or "0")
    else:
        raise Exception("EnsureInteger unable to parse valid Int, passed \"{}\"".format(input))

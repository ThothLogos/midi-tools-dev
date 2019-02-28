def IsValidChannel(num):
    if num >= 0 and num <= 15:
        return True
    else: 
        return False

def EnsureInteger(input):
    if isinstance(input, int):
        return int(str(input).lstrip("0") or "0")
    elif isinstance(input, str):
        if input.isnumeric(): 
            return int(input.lstrip("0") or "0")
        else:
            #raise Exception("EnsureInteger parse failed string \"{}\" to valid Int".format(input))
            print("EnsureInteger parse failed string \"{}\" to valid Int".format(input))
    else:
        #raise Exception("EnsureInteger unable to parse a Str or Int, passed \"{}\"".format(input))
        print("EnsureInteger unable to parse a Str or Int, passed \"{}\"".format(input))

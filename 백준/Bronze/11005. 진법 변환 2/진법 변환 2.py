import string

CHAR_LOOKUP = list(string.digits + string.ascii_uppercase)

def numeral(num):
    global CHAR_LOOKUP
    return CHAR_LOOKUP[num]

def convert_base(number, base):
    if base < 2 or base > 36:
        return False
    mods = []
    while number > 0:
        mods.append(numeral(number % base))
        number //= base
    mods.reverse()
    return ''.join(mods)

number_input, base_input = map(int, input().split())

print(convert_base(number_input, base_input))
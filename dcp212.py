import math

def num_to_alphabet_id(num):
    """ Basically just convert num to base 26
    1 -> A
    27 -> AA
    28 -> AB
    """
    # mine goes the opposite way.
    # exp = math.floor(math.log(num, 26))
    # ans = ""
    # while exp >= 0:
    #     x = 26**exp
    #     ans += chr(ord('A')-1 + (num//x))
    #     num = num%x
    #     exp -= 1
    # return ans

    # here is a simpler way:
    ans = ""
    while num > 0:
        num, digit = divmod(num, 26)
        ans = chr(64 + digit) + ans
    return ans

print(num_to_alphabet_id(1))
print(num_to_alphabet_id(27))
print(num_to_alphabet_id(28))
print(num_to_alphabet_id(16)) # -> P

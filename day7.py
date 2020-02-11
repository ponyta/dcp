# to note, a 1 char string is always ok
def isValidMapping(substr):
    if 1 <= int(substr) <= 26:
        return True
    return False

# O(n) time
def numEncodings(string):
    if len(string) == 1:
        return 1
    # DP
    numEncodings = [0]*(len(string) + 2)
    numEncodings[-2] = 1
    numEncodings[-3] = 1

    for i in range(len(string)-2, -1, -1):
        num = 0
        if isValidMapping(string[i:i+2]):
            num += numEncodings[i+2]
        num += numEncodings[i+1]
        numEncodings[i] = num

    return numEncodings[0]

print numEncodings("111")


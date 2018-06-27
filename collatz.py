# Daily Coding Problem #210

found = {1: 0} # assume it's a hash set

def next(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return 3*n + 1

def collatz(n):
    global found
    if n in found:
        return found[n]
    found[n] = collatz(next(n)) + 1
    return found[n]

def main():
    global found
    max_n = 1
    for i in range(1, 1000001):
        if collatz(i) > found[max_n]:
            max_n = i
    print (max_n)

main()

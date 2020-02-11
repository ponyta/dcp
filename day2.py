def main():
    arr = [1,2,3,4,5, 6, 7, 8, 9]
    print prod(arr)

def prod(arr):
    prefix_prods = [1]*len(arr)
    suffix_prods = [1]*len(arr)
    for i in range(1, len(prefix_prods)):
        prefix_prods[i] = prefix_prods[i-1]*arr[i-1]
    for i in range(len(suffix_prods)-2,-1,-1):
        suffix_prods[i] = suffix_prods[i+1]*arr[i+1]
    for i in range(len(arr)):
        arr[i] = prefix_prods[i]*suffix_prods[i]
    return arr

main()

def first_missing_natural(arr):
    for i in range(len(arr)):
        # if arr[i] is within bounds swap it with it's proper position
        while 0 <= arr[i] < len(arr) and arr[i] != i:
            tmp = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = tmp
    for i in range(1, len(arr)):
        if arr[i] != i:
            return i
    return len(arr)

if __name__ == '__main__':
    test = [1, 2, 0]
    print(first_missing_natural(test))

def main():
    arr = [3,4,-1,1]
    arr = [1, 2, 0]
    print find_missing_pos(arr)

def find_missing_pos(arr):
    pos_sum = 0
    max_n = arr[0]
    for i in arr:
        if i > 0:
            pos_sum += i
        if i > max_n:
            max_n = i
    total_sum = max_n*(max_n+1)/2
    if total_sum == pos_sum:
        return max_n + 1
    return total_sum - pos_sum
main()

from collections import deque
import math

def main():
    stack = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    queue = deque([])
    interflip(stack, queue)
    print stack

def interflip(stack, queue):
    big_len = int(math.ceil(len(stack)/2.0))
    small_len = int(math.floor(len(stack)/2.0))
    for i in range(len(stack)):
        queue.append(stack.pop())
    # rotate
    for i in range(small_len):
        queue.append(queue.popleft())
    for i in range(big_len):
        stack.append(queue.popleft())
    # pair
    for i in range(small_len):
        queue.append(stack.pop())
        queue.append(queue.popleft())
    if len(stack) != 0:
        queue.append(stack.pop())
    for i in range(len(queue)):
        stack.append(queue.popleft())
main()

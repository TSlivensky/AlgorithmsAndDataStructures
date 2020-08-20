# Uses python3
import sys
import math

def binary_search(a, low, high, x):
    if high < low:
        return -1

    mid = low + math.floor((high-low) / 2)

    if(a[mid] == x):
        return mid
    elif (x > a[mid]):
        return binary_search(a, mid + 1, high, x)
    elif(x < a[mid]):
        return binary_search(a, low, mid - 1, x)


    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    low = 0 
    high = len(a) - 1
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, low, high, x), end = ' ')

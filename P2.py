import random
import time
start_time = time.time()
def quickSelectMOM(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]  
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    pivot = quickSelectMOM(medians, len(medians) // 2)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    if k < len(left):
        return quickSelectMOM(left, k)
    elif k < len(left) + len(equal):
        return pivot
    else:
        return quickSelectMOM(right, k - len(left) - len(equal))
n = 800  # n
a = [random.randint(0, 2*n) for x in range(n)]
print(a)
print("Median:", quickSelectMOM(a,len(a) // 2))
end_time = time.time()
print("Run time (microsecond): ", (end_time - start_time) * 1000000)
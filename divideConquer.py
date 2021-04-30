from timeit import default_timer as timer #imports a timer to record the elapsed time it takes to return the entire code
from sys import maxsize
import sys
import tracemalloc
 
tracemalloc.start()
start = timer() 
def maxCrossingSum(A, l, m, h): # In this instance l represents the low point, m for mid point, h for high point
 
    # Include elements on left of mid.
    left_sum = -10000
    sm = 0
   
    for i in range(m, l-1, -1):
        sm = sm + A[i] 
        if (sm > left_sum):
            left_sum = sm
 
    # Include elements on right of mid
    right_sum = -10000
    sm = 0
    for i in range(m + 1, h + 1):
        sm = sm + A[i]
        if (sm > right_sum):
            right_sum = sm
 
    # Return sum of elements on left and right of mid, including the sum of both
    return max(left_sum + right_sum, left_sum, right_sum)
 
# Returns sum of maxium sum subarray in a[low..high]
def maxSubArraySum(A, l, h):
 
    # Base Case: Only one element, if low equals high, then it will return one single value
    if (l == h):
        return A[l]
 
    # Find middle point by simply dividing the low and high point
    m = (l + h) // 2
 
    return max(maxSubArraySum(A, l, m),
               maxSubArraySum(A, m+1, h),
               maxCrossingSum(A, l, m, h))
end = timer() 

current, peak = tracemalloc.get_traced_memory()

# Driver program to test maxSubArraySum, below is the array with 100 entires, you can find the rest in the data.csv file
A = [29,88,73,98,5,-60,-49,13,79,27,47,-24,20,-44,-65,23,75,32,-36,-27,-80,5,46,-19,72,-71,74,-55,-97,53,33,91,-88,26,80,-23,-66,55,18,77,-40,67,60,-97,-73,38,-99,-6,83,42,-32,92,91,6,-76,-41,-40,75,-41,99,-5,-57,79,-16,-86,-94,22,-49,-85,-70,81,-98,51,39,48,-38,87,84,-90,-22,-40,-36,68,10,80,5,59,68,-76,-13,66,-53,-73,18,-28,1,-38,20,-19,2]
n = len(A)
 
max_sum = maxSubArraySum(A, 0, n-1)

print("Maximum contiguous sum is ", max_sum)
print("Elapsed time:", end,"seconds")
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()


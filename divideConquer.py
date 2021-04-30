# Find the maximum possible sum in
# arr[] auch that arr[m] is part of it
from timeit import default_timer as timer

 
start = timer() 
def maxCrossingSum(arr, l, m, h): # In this instance l represents the low point, m for mid point, h for high point
 
    # Include elements on left of mid.
    left_sum = -10000
    sm = 0
  
 
    for i in range(m, l-1, -1):
        sm = sm + arr[i]
 
        if (sm > left_sum):
            left_sum = sm
 
    # Include elements on right of mid
    sm = 0
    right_sum = -10000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]
 
        if (sm > right_sum):
            right_sum = sm
 
    # Return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2, 1]
    return max(left_sum + right_sum, left_sum, right_sum)
  
 
 
# Returns sum of maxium sum subarray in a[l..h]
def maxSubArraySum(arr, l, h):
 
    # Base Case: Only one element
    if (l == h):
        return arr[l]
 
    # Find middle point
    m = (l + h) // 2
 
    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #     subarray crosses the midpoint
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m+1, h),
               maxCrossingSum(arr, l, m, h))
end = timer() 

run_time = ("{:.7f}".format(end - start))

# Driver Code
arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
n = len(arr)
 
max_sum = maxSubArraySum(arr, 0, n-1)



print("Maximum contiguous sum is ", max_sum)
print("Elapsed time:", run_time,"seconds")
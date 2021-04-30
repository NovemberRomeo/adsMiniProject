from sys import maxsize
from timeit import default_timer as timer
import tracemalloc

# Function to find the maximum contiguous subarray
def maxSubArraySum(A,size):
    tracemalloc.start()
    startTime = timer() 
    max_so_far = -maxsize - 1
    max_ending_here = 0
    
    for i in range(0,size):
        max_ending_here += A[i]
 
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
           
    endTime = timer()
   
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

    print ("Maximum contiguous sum is %d"%(max_so_far))
    print("Elapsed time:", f'{endTime:.8f}', 'seconds')

 
# Driver program to test maxSubArraySum, below is the array with 100 entires, you can find the rest in the data.csv file
A = [29,88,73,98,5,-60,-49,13,79,27,47,-24,20,-44,-65,23,75,32,-36,-27,-80,5,46,-19,72,-71,74,-55,-97,53,33,91,-88,26,80,-23,-66,55,18,77,-40,67,60,-97,-73,38,-99,-6,83,42,-32,92,91,6,-76,-41,-40,75,-41,99,-5,-57,79,-16,-86,-94,22,-49,-85,-70,81,-98,51,39,48,-38,87,84,-90,-22,-40,-36,68,10,80,5,59,68,-76,-13,66,-53,-73,18,-28,1,-38,20,-19,2]
maxSubArraySum(A,len(A))
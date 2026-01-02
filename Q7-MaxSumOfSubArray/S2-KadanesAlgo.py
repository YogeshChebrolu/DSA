"""
TC: O(n)
SC: O(1)
Question:
Approach: Have a counting sum when traversing array. If we found a better element or sum then restart the sub-array
"""

def MaxSumOfSubArray(arr):
    max_sum = curr_sum = arr[0]
    start = temp_start = end = 0
    
    n = len(arr)
    
    for i in range(1, n):
        if curr_sum + arr[i] < arr[i]:
            curr_sum = arr[i]
            temp_start = i
        else:
            curr_sum += arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
    return max_sum, start, end
        
         

def main():
    arr = [5, -1 , 5]
    print("Original Array: ", arr)
    largest_sub_array_sum, lp, rp = MaxSumOfSubArray(arr)
    print("Sum of largest sub array: ", largest_sub_array_sum, "start: ", lp, "end: ", rp)
    
main()
    
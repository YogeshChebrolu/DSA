"""
TC: O(n)
SC: O(1)
Approach: Iterate over the first half of the array and replace with corresponding element from second half
"""

def reverse_array(arr):
    n = len(arr)
    for i in range(n//2):
        temp = arr[i]
        arr[i], arr[n-i-1] = arr[n-i-1], temp
    
    return arr
        

def main():
    arr = [9,8,7,6,5,4,3,2]
    print("Original Array: ", arr)
    reverse_arr = reverse_array(arr)
    print("Reverse Array: ", reverse_arr)
    
main()

"""
Approach: Use Built-in reverse Method

arr.reverse()
"""
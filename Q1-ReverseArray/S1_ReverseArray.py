"""
TC: O(n)
SC: O(n)
Approach: Create a Temp Array and copy the array elements in reverse order
"""


def reverse_array(arr):
    n = len(arr)
    temp_array = [0] * n
    for i in range(n):
        temp_array[i] = arr[n-i-1]
    
    for i in range(n):
        arr[i] = temp_array[i]
    
    return arr

def main():
    arr = [9,8,7,6,5,4,3,2,1]
    print("Original Array: ", arr)
    reverse_arr = reverse_array(arr)
    print("Reverse Array: ", reverse_arr)
    
main()
    
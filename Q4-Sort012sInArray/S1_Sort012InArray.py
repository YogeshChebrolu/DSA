"""
Question: Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
Note: You need to solve this problem without utilizing the built-in sort function.
Solution: Loop through array push O's to 1st index and 2's to last index and leave 1's as it is

Failed Approach
"""
def sort012Array(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            arr.pop(i)
            arr = [0] + arr
        elif arr[i] == 2:
            arr.pop(i)
            arr = arr + [2]
    return arr

def main():
    arr = [2,1,2,0,1,1,2,0,0]
    print("Original Array: ", arr)
    sort_arr = sort012Array(arr)
    print("Sorted Array: ", sort_arr)
    
main()
    
"""
Approach: 3 pointer approach 
"""

def sort012Array(arr):
    n = len(arr)
    
    lo, mid = 0, 0
    hi = n - 1
    while mid<=hi:
        if arr[mid] == 0:
            arr[mid], arr[lo] = arr[lo], arr[mid]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr
            
        
def main():
    arr = [2,1,2,0,1,1,2,0,0]
    print("Original Array: ", arr)
    sort_arr = sort012Array(arr)
    print("Sorted Array: ", sort_arr)
    
main()
    
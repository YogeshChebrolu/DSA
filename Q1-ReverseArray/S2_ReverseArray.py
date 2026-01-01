"""
TC: O(n)
SC: O(1)
Approach: Swap elements using two pointer
"""

def reverse_array(arr):
    lp = 0
    rp = len(arr) - 1
    
    if lp == rp:
        return arr
    while True:
        if lp > rp:
            return arr
        temp_var = arr[lp]
        arr[lp] = arr[rp]
        arr[rp] = temp_var
        lp = lp + 1
        rp = rp - 1

def main():
    arr = [9,8,7,6,5,4,3,2]
    print("Original Array: ", arr)
    reverse_arr = reverse_array(arr)
    print("Reverse Array: ", reverse_arr)
    
main()
    
        
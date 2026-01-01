"""
URL: https://www.geeksforgeeks.org/dsa/move-negative-numbers-beginning-positive-end-constant-extra-space/
Question: Move all negative numbers to beginning and positive to end with constant extra space
Approach: Use two pointer approach where left pointer has negative num behind it and right pointer has positive number behind it
"""

def PushNegToBeginning(arr):
    n = len(arr)
    lp = 0
    rp = n -1 
    while lp <= rp:
        if arr[lp] > 0 and arr[rp] < 0:
            arr[lp], arr[rp] = arr[rp] , arr[lp]
        if arr[lp] > 0:
            while arr[rp] < 0:
                rp -= 1
            arr[lp], arr[rp] = arr[rp] , arr[lp]
        if arr[rp] < 0:
            while arr[lp] > 0:
                lp += 1
            arr[lp], arr[rp] = arr[rp] , arr[lp]
    return arr

def main():
    arr = [-5,-8,-7,6,15,42,3,-2,1]
    print("Original Array: ", arr)
    sort_arr = PushNegToBeginning(arr)
    print("Sorted Array: ", sort_arr)
    
main()
    
"""
Approach: Two pointer
"""

def PushNegToBeginning(arr):
    n = len(arr)
    lp = 0
    rp = n -1 
    while lp <= rp:
        if arr[lp] < 0:
            lp += 1
        elif arr[rp] >= 0:
            rp -= 1
        else:
            arr[lp], arr[rp] = arr[rp] , arr[lp]
            lp += 1
            rp -= 1
    return arr

def main():
    arr = [-5,-8,-7,6,15,42,3,-2,1]
    print("Original Array: ", arr)
    sort_arr = PushNegToBeginning(arr)
    print("Sorted Array: ", sort_arr)
    
main()
    
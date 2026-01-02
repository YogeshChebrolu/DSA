"""
Question: Given an array arr, rotate the array by one position in clockwise direction.
Approach: Remove the last element and append it as the first element
"""

def RotateArrayByOne(arr):
    temp = arr[-1]
    arr.pop(-1)
    arr = [temp] + arr
    return arr
def main():
    arr = [-5,-8,-7,6,15,42,3,-2,1]
    print("Original Array: ", arr)
    sort_arr = RotateArrayByOne(arr)
    print("Rotated Array: ", sort_arr)
    
main()
    
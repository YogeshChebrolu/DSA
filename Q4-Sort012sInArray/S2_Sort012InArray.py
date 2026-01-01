"""
TC: O(n)
SC: O(n)
Solution: Count no of 0's, 1's and 2's and creat an array
"""

def sort012Array(arr):
    c0 = c1 = c2 = 0
    for i in arr:
        if i == 0:
            c0 += 1
        elif i == 1:
            c1 += 1
        else:
            c2+= 1
    return c0 * [0] + c1 * [1] + c2 * [2]

def main():
    arr = [2,1,2,0,1,1,2,0,0]
    print("Original Array: ", arr)
    sort_arr = sort012Array(arr)
    print("Sorted Array: ", sort_arr)
    
main()
    
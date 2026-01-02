"""
TC:
SC:
Question: Given an array arr[] denoting heights of n towers and a positive integer k.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by k
Decrease the height of the tower by k
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Approach: Sort the array and add k to first half and subtract k from second half
Failure: You can't divide the with mid you should find optimal split
URL: https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1
"""

def MinimizeTheHeights(arr, k):
    arr = sorted(arr)
    mid = len(arr) // 2
    n = len(arr)
    for i in range(0, n):
        if i <= mid:
            arr[i] += k
        else:
            arr[i] -= k
    
    return arr[n-1] - arr[0], arr
         

def main():
    arr = [1, 5, 8, 10]
    k = 5
    print("Original Array: ", arr)
    min_diff , mod_arr= MinimizeTheHeights(arr, k)
    print("Min diff is: ", min_diff, "Modified arr: ", mod_arr)
    
main()
    
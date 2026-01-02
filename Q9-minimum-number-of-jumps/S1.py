"""
URL: https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
"""

def max_in_reach(arr:list, s, e):
    max_num = max(arr[s: e])
    max_num_index = arr[s:e].index(max_num)
    return max_num, max_num_index

def MinimumNumberofJumps(arr):
    no_of_jumps = 0
    i = 0
    while i < len(arr):
        current_element = arr[i]
        max_num_in_reach, max_num_index = max_in_reach(arr, i, i+current_element+1)
        if i+current_element >= i+(max_num_index-current_element)+ max_num_in_reach:
            no_of_jumps+=1
            i+=current_element
        else:
            no_of_jumps+=1
            i=max_num_index
            
    return no_of_jumps

def main():
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    k = 5
    print("Original Array: ", arr)
    min_of_jumps= MinimumNumberofJumps(arr)
    print("Min no of jumps: ", min_of_jumps)
    
main()
    
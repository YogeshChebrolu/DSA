"""
Tc: O(n)
SC: O(1)
Approach (Naive): Compare every element and find the min and max elements 
    Total comparisions are 2 * len(arr)
"""

def min_n_max(arr):
    min_element = 999999
    max_element = -999999
    n = len(arr)
    
    for i in range(n):
        current_element = arr[i]
        if current_element < min_element:
            min_element = current_element
        if current_element > max_element:
            max_element = current_element
    
    return min_element, max_element

def main():
    arr = [9,8,7,6,5,4,3,2,1]
    print("Original Array: ", arr)
    min_element, max_element = min_n_max(arr)
    print("Min and Max elements are: ", min_element, " ", max_element)
    
main()
    
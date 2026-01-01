"""
Approach: Recurssion diving the array into sub-arrays until 1 or 2 elements and find min and max elements recursively
        by comparing min and max elements of the divided arrays
"""

def get_min_n_max(arr, min_index, max_index):
    result = [0, 0]
    # Base Case (Single element in array)
    if min_index == max_index:
        return [arr[min_index], arr[min_index]]
    # two length array (Compare)
    if min_index + 1 == max_index:
        if arr[min_index] < arr[max_index]:
            result[0] = arr[min_index]
            result[1] = arr[max_index]
        else:
            result[0] = arr[max_index]
            result[1] = arr[min_index]
        return result

    mid = (min_index + max_index) // 2
    result1 = get_min_n_max(arr, min_index, mid)
    result2 = get_min_n_max(arr, mid+1, max_index)
    
    result[0] = min(result1[0], result2[0])
    result[1] = max(result1[1], result2[1])
    return result

def find_min_n_max(arr):
    return get_min_n_max(arr, 0, len(arr) - 1)

def main():
    arr = [-9,8,7,6,5,4,3,2,1]
    print("Original Array: ", arr)
    result = find_min_n_max(arr)
    print("Min and Max elements are: ", result[0], " ", result[1])
    
main()
    
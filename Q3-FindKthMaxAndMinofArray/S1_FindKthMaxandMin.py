"""
Question: Find Kth smallest and largest element of the array
TC: O(n^2)
SC: O(1)
Approach: Sort the array and index the element according to the kth index
"""

def findKthMinandMax(arr, k):
    # Sort the Array
    n = len(arr)
    for i in range(1, n):
        print("Chekcing Insersioin for index i: ", i)
        j = i - 1
        temp = arr[i]
        print("Saving as temp: ", temp)
        while True:
            if j >= 0 and temp < arr[j] :
                print("---- Shifting element from ", j+1, "index to ", j)
                arr[j+1] = arr[j]
                print("---- Array afrer shift: ", arr)
            else:
                break
            j = j - 1
        arr[j + 1] = temp 
    
    # kth min and max are
    min, max = arr[k-1], arr[-k]
    return min, max, arr
        


def main():
    arr = [-5,-8,-7,6,15,42,3,-2,1]
    print("Original Array: ", arr)
    result = findKthMinandMax(arr, 3)
    print("Sorted Array: ", result[2], "kth min ", result[0], "kth max ", result[1])
    
main()
    
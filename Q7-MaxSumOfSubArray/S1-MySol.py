"""
TC:
SC:
Question: You are given an integer array arr[]. You need to find the maximum sum of a subarray 
(containing at least one element) in the array arr[].
Approach: This has a lot of edge cases that aren't covered Negatives reduce the sum.
If a negative hurts more than the positives around it help, remove it.
"""
def HighestNegNumInBetween(arr: list, l, r):
    min = 999999
    for i in range(l, r):
        if arr[i] < min:
            min = arr[i]
            
    min_index = arr.index(min)
    
    has_neg = True if min < 0 else False
    
    return has_neg, min_index, min

def SumofArrayPart(arr: list, l, r):
    sum = 0
    for i in range(l, r):
        sum += arr[i]
    return sum

def MaxSumOfSubArray(arr):
    n = len(arr)
    lp = 0
    rp = n - 1
    s = sum(arr)
    prevLp = lp
    prevRp = rp
    while lp<=rp:
        has_neg, min_index, min = HighestNegNumInBetween(arr, lp, rp+1)
        print("Arr: ", arr[lp: rp+1], "Has Negative: ", has_neg, "LP: ", lp, "RP: ", rp)
        if has_neg:
            lp_to_neg_sum = SumofArrayPart(arr, lp, min_index)
            neg_to_rp_sum = SumofArrayPart(arr, min_index+1, rp+1)
            print("----LP_TP_NEG_SUM: ", lp_to_neg_sum, "NEG_TO_RP_SUM: ", neg_to_rp_sum)
            if lp_to_neg_sum < -1*min:
                prevLp = lp
                lp = min_index+1
                
            if neg_to_rp_sum < -1*min:
                prevRp = rp
                rp = min_index-1
        else:
            break
    s = SumofArrayPart(arr, lp, rp+1)
    return s, lp , rp
        
         

def main():
    arr = [5, -1 , 5]
    print("Original Array: ", arr)
    largest_sub_array_sum, lp, rp = MaxSumOfSubArray(arr)
    print("Sum of largest sub array: ", largest_sub_array_sum, "lp: ", lp, "rp: ", rp)
    
main()
    
"""
Great — this is exactly the right thing to ask.
This indexing looks magical until you see the invariant behind it. Let’s unpack it slowly and mechanically, using your way of thinking.

First, restate the two lines
max_height = max(arr[i] + k, arr[n-1] - k)
min_height = min(arr[0] + k, arr[i+1] - k)


These lines assume a very specific partition. Understanding that partition is the whole key.

What does index i represent?

After sorting arr:

arr[0] ≤ arr[1] ≤ ... ≤ arr[i] ≤ arr[i+1] ≤ ... ≤ arr[n-1]


We are testing a split at index i:

Elements 0 .. i → increase by k

Elements i+1 .. n-1 → decrease by k

This is the only structure we are considering.

Why? Because any optimal solution can be rearranged into this form after sorting.

Now let’s derive max_height
Candidates for maximum height after modification

From the two groups:

Left group (increased by k)
Largest element here is:

arr[i] + k


Right group (decreased by k)
Largest element here is:

arr[n-1] - k


So the overall maximum must be:

max(arr[i] + k, arr[n-1] - k)


Nothing else can be larger.

That explains:

max_height = max(arr[i] + k, arr[n-1] - k)

Now derive min_height
Candidates for minimum height after modification

Again from the two groups:

Left group (increased by k)
Smallest element here is:

arr[0] + k


Right group (decreased by k)
Smallest element here is:

arr[i+1] - k


So the overall minimum must be:

min(arr[0] + k, arr[i+1] - k)


That explains:

min_height = min(arr[0] + k, arr[i+1] - k)

Why these indices are enough (this is the crucial insight)

You might wonder:

“Why don’t we check all elements?”

Because after sorting:

The largest possible value in the left group is always arr[i]

The smallest possible value in the right group is always arr[i+1]

Everything else lies between these extremes and cannot define the min/max.

This is a boundary-only check.
"""
"""
TC: O(nlogn) - For sorting
SC: O(1)
"""
def MinimizeTheHeights(arr, k):
    arr.sort()
    n = len(arr)
    
    ans = arr[n-1] - arr[0]
    for i in range(n):
        max_height = max(arr[i]+k, arr[n-1]-k)
        min_height = min(arr[0]+k, arr[i+1]-k)
        
        if min_height<0:
            continue
        ans = min(ans, max_height-min_height)
    return ans, arr
def main():
    arr = [1, 5, 8, 10]
    k = 5
    print("Original Array: ", arr)
    min_diff , mod_arr= MinimizeTheHeights(arr, k)
    print("Min diff is: ", min_diff, "Modified arr: ", mod_arr)
    
main()
    
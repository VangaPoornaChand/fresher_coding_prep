

# Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

def findTwoElement(arr, n): 
    # code here
    ans = []
    num_map = {}
    for i in arr:
        if i not in num_map:
            num_map[i] = True
        else:
            ans.append(i)
        
    for i in range(1,n+1):
        if i not in num_map:
            ans.append(i)
            
    return ans

print(findTwoElement([1,3,3]))

def linearsearch(arr, n , k):
    
    for i in range(n):
        if arr[i] == k:
            return i
    
    return -1;

print(linearsearch([1,2,3,4,5],5,3))

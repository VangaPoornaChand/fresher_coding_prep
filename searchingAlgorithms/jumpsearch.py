import math


def jump_search(arr,n,k):
    index_ = 0
    step = int(math.sqrt(n))
    while index_<n:
        if arr[index_] == k:
            return index_
        elif arr[index_] > k:
            index_ = index_ - 1
        else:
            index_ = index_ + step
            if index_>n and index_!=n:
                index_=n-1
        
    return -1


print(jump_search([1,2,3,4,5,6,7,8,9,11,14,15,18,22],14,3))

def rec_linearsearch(arr,i,k):
    if arr[i]==k:
        return i
    return rec_linearsearch(arr,i+1,k)


print(rec_linearsearch([1,2,3,4,5],0,3))
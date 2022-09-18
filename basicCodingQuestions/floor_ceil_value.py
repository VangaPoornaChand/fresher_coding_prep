# Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing order. Write efficient functions to find floor and ceiling of x.


def sol(arr,x):
    n = len(arr)
    c = None
    f = None
    arr.sort()
    if x in arr:
        return x,x
    if max(arr) < x:
        c = "Ceil Doesn't Exist"
        f = max(arr)
    if min(arr) > x:
        f = "Floor Doesn't Exist"
        c = min(arr)
    for i in arr:
        if i > x:
            if c == None:
                c = i
            if f == None:
                f = arr[arr.index(i)-1]
            
    return f,c


print(sol([1, 2, 8, 10, 10, 12, 19],0))     # NA,1

print(sol([1, 2, 8, 10, 10, 12, 19],1))     # 1,1

print(sol([1, 2, 8, 10, 10, 12, 19],5))     # 2,8

print(sol([1, 2, 8, 10, 10, 12, 19],20))    # 19, NA


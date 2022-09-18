

def closestToZero (arr):
    n = len(arr)
    if n<2:
        return -1
    sum = 9999
    for i in range(n):
        for j in range(n-1,0,-1):
            if i == j: continue
            s = arr[i]+arr[j]
            if abs(sum) > abs(s):
                sum = s
    
    return sum

# print(closestToZero([1,2,3,4,5,-1]))

# print(closestToZero([-8 ,-66 ,-60]))

# print(closestToZero([-21 ,-67, -37, -18, 4, -65]))

print(closestToZero([-43 ,-37, 5, 4 ,-33, 17, -46 ,-27 ,-39 ,-13 ,-50 ,-45, 12, -34, -15 ,-12]))   # 0 is ans

print(closestToZero([18,-1]))

print(closestToZero([29, 13 ,-6 ,-32 ,-12]))
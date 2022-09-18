
def minAnd2ndMin( a):
    min1 = min(a)
    while min1 in a:
        a.remove(min1)
    if len(a)==0:
        return [-1,0]
    min2 = min(a)
    return min1,min2

print(minAnd2ndMin([1,2,3,4,5]))
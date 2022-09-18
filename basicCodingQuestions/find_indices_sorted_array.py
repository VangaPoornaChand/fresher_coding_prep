
# Input: arr = [1, 2, 5, 2, 3], val = 2
# Output: 1 2
# Explanation: After sorting, arr[] becomes [1, 2, 2, 3, 5]. The indices where arr[i] = 2 are 1 and 2. As the indices should be in increasing order, that’s why they are   (1, 2) and not (2, 1)

arr = [ 2, 5, 2, 3,2,2,2]
val = 2

res = []
arr.sort()
while True:
    if val not in arr:
        break
    index_ = arr.index(val)
    arr.remove(val)
    arr.insert(index_,'0')
    res.append(index_)

print(res)

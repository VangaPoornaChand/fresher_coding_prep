

def getMaximumGenerated(n: int):
    if n == 2: return 1
    if n < 2: return 0
    nums = [0] * (n+1)
    nums[0] = 0
    nums[1] = 1
    for i in range(1,(n//2)+1):
        # print(i*2,(i * 2) + 1)
        nums[ i * 2 ] = nums[i]
        nums[(i * 2) + 1] = nums[i] + nums[i+1]
        # print(nums[i*2],nums[(i * 2) + 1])
    # print(nums)
    return max(nums)
        
print(getMaximumGenerated(2))
print(getMaximumGenerated(3))
print(getMaximumGenerated(7))
print(getMaximumGenerated(17))
# class Solution:	
#     index_ = -1
#     def binarysearch(self, arr, n, k):
#         i = int(n/2)
#         if k==arr[i]:
#             return self.index_
#         elif k > arr[i]:
#             self.index_ = self.index_ + i
#             self.binarysearch(arr[i:],len(arr[i:]),k)
#         elif k < arr[i]:
#             self.binarysearch(arr[:i],len(arr[:i]),k)
#         else:
#             return self.index_


class Solution:
    def binarysearch(self, arr, n, k):
        begg = 0
        end = n
        while True:
            i = int(begg+((end-begg)/2))
            if arr[i] == k:
                return i
            elif k > arr[i]:
                begg = i+1
                end = n
            elif k < arr[i]:
                begg = 0
                end = i-1

        return -1

s = Solution()
print(s.binarysearch([1,2,3,4,5],5,3))
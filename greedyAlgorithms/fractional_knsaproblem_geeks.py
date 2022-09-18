#User function Template for python3

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # code here
        l = []
        result = []
        for i in Items:
            l.append((i.value,i.weight,i.value/i.weight))
        
        sorted_l = sorted(l,key=lambda a: a[-1],reverse=True)
        print(sorted_l)
        c = 0
        for i in sorted_l:
            if W > i[1]:
                c+=1
                W -= i[1]
                result.append(i[0])
                print(c)
            else:
                if W > 0:
                    print("CCC",c)
                    result.append(i[-1]*W)
                    W -= i[-1] * W              # This is important...!!!
                    
        print(result)
        return sum(result)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    # test_cases = int(input())
    # for cases in range(test_cases) :
    n,W = map(int,"84 87".strip().split())
    info = list(map(int,"78 16 94 36 87 43 50 22 63 28 91 10 64 27 41 27 73 37 12 19 68 30 83 31 63 24 68 36 30 3 23 9 70 18 94 7 12 43 30 24 22 20 85 38 99 25 16 21 14 27 92 31 57 24 63 21 97 32 6 26 85 28 37 6 47 30 14 8 25 46 83 46 15 18 35 15 44 1 88 9 77 29 89 35 4 2 55 50 33 11 77 19 40 13 27 37 95 40 96 21 35 29 68 2 98 3 18 43 53 7 2 31 87 42 66 40 45 20 41 30 32 18 98 22 82 26 10 28 68 7 98 4 87 16 7 34 20 25 29 22 33 30 4 20 71 19 9 16 41 50 97 24 19 46 47 2 22 6 80 39 65 29 42 1 94 1 35 15".strip().split()))
    Items = [Item(0,0) for i in range(n)]
    for i in range(n):
        Items[i].value = info[2*i]
        Items[i].weight = info[2*i+1]
        
    ob=Solution()
    print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends
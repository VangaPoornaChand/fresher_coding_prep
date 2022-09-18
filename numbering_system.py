# ANSWER NOT FOUND  AND CAN"T CODE !!!!!!!


M = 40

B = 2
def sol(M,B):
    while True:
        if B > M:
            return -1
        test_M = M
        r = []
        while test_M>=B:
            r.append(test_M % 2)
            test_M = test_M//2
            print(test_M)
        print(r)
        if r.count(r[0]) == len(r) and r[0] != 0:
            return B
        B+=1
print(sol(M,B))
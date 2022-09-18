


def sol(N,M,A,B):
    count = 0
    while sum(A)<sum(B):
        print(A,B)
        a_min = min(A)
        b_max = max(B)
        if a_min == b_max:
            return -1
        A.append(b_max)
        B.append(a_min)
        A.remove(a_min)
        B.remove(b_max)
        count += 1
    return count


T = 1
for i in range(T):
    N,M = map(int,input().strip().split())
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    res = sol(N,M,A,B)
    print(res)
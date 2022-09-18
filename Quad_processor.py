

from ast import Lambda


def sol(P, T):
    T.sort(reverse=True)
    P.sort()
    T_final = []
    k = 0
    for i in range(0,len(T),4):
        for j in T[i:i+4]:
            T_final.append(j+P[k])
        k+=1
    return max(T_final)


print(sol([8,10],[3,1,8,7,4,2,5,2]))

print(sol([5,11],[3,1,8,7,4,2,5,2]))
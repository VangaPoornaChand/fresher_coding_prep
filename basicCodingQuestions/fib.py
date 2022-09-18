
def fib(num):
    l = [0,1]
    for i in range(1,num-1):
        n = l[i]+l[i-1]
        l.append(n)
    print(l)
    return l[-1]

print(fib(15))
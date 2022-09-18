
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

def fact(num):
    res = 1
    while num>0:
        res = res * num
        num -= 1
    return res

print(factorial(5))
print(fact(5))
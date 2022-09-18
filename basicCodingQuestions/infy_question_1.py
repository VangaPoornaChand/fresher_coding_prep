

# You will be given a string s of size n you have to perform a perticulat type query multiples times on string,
# the query string T, find the lengh of a lexicographically smallest suffix string of S starts with T if there is no suffix return 0....

# Input Format:
# String S
# Q Query of Array....


def sol(S,T):
    if S.find(T) == -1:
        return 0
    return len(S[S.find(T):])



# Test Case 1
# S = "mazdpoghyykht"
# T = ["yk"]

# Test Case 2
# S = "ktmrgjswhwxu"
# T = ["z","w"]

# Test Case 3
S = "tvtrpudosnlydgi"
T = ["do"]

sum = 0
for i in T:
    sum = sum + sol(S,i)

print(sum)
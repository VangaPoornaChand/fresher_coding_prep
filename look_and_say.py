
def lookandsay(n):
    # code here
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"
    s = "11"
    for i in range(3, n + 1):       #i = 4
        s += '$'                    # s = 11$$
        l = len(s)                  # l = 4
        cnt = 1                     # cnt =1
        tmp = ""                    # ""
        for j in range(1 , l):      # j = 1
            if (s[j] != s[j - 1]):      # s[1] = 1, s[j-1]/s[0] = 1
                tmp += str(cnt + 0)         # tmp = 21
                tmp += s[j - 1]
                cnt = 1
            else:
                cnt += 1
        s = tmp
    return s


print(lookandsay(5))
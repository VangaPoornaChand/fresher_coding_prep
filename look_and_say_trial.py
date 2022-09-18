

# n = input()
n = 5
l = ["1","11","21","1211"]
for i in range(n-1):
    temp_ln = l[-1]
    i = 1
    while i <= len(l[-1]):
        final_out = ""
        j = 0
        # find str to read
        while temp_ln != "":
            j += 1
            print(j,len(l[-1]),len(temp_ln),temp_ln[j],temp_ln[j-1])
            if temp_ln[j] != temp_ln[j-1]:
                st = temp_ln[:j]
                temp_ln = temp_ln[j:]
        # read as count , number - append to final output
                final_out += str(st.count(st[0]))+st[0]
        # repeat above steps
        i+=1
    l.append(final_out)
    print(final_out,l)


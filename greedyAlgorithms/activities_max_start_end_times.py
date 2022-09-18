
def sol(actvities):
    res = 0
    res_l = []
    current_t = 0
    sorted_act = sorted(actvities, key= lambda a:a[-1])
    for i in sorted_act:
        if current_t <= i[0]:
            res += 1
            res_l.append(i)
            current_t = i[-1]

    return res,res_l

# print(sol([(4,6),(3,7),(5,8),(7,10),(13,15)]))
print(sol([(1,3),(2,3),(8,12),(5,8),(7,11)]))
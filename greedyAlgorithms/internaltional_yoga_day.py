

def sol(l,b,no_of_yoga_halls,rooms):
    # check at least one is possible or not else return 0
    ans = 0
    for i in range(no_of_yoga_halls):
        ans+= max(([(rooms[i][0]//l) * (rooms[i][1]//b), (rooms[i][0]//b) * (rooms[i][1]//l)]))
    print(rooms[i][0]//l , rooms[i][1]//b, rooms[i][0]//b ,rooms[i][1]//l)
    return ans


# print(sol(4,4,1,[(4,12)]))

print(sol(10,10,1,[(2,1000)]))

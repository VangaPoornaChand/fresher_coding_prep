

from cgitb import reset
from typing import final


def sol(prices,weights,bag_weight):             # P, W, P/W
    result = []
    price_by_weights = [float(i/j) for i,j in zip(prices,weights)]
    final_items = [(i,j,k) for i,j,k in zip(prices,weights,price_by_weights)]
    sorted_final_times = sorted(final_items, key=lambda x: x[-1],reverse=True)
    # print(sorted_final_times)
    
    for i in sorted_final_times:
        if bag_weight > i[1]:
            bag_weight -= i[1]
            result.append(i[0])
        else:
            result.append(i[-1]*bag_weight)
            # bag_weight-=i[]

    print(result)

    return sum(result)


print(sol([90,20,50,100],[9,1,25,2],15))

print(sol([60,100,120],[10,20,30],50))
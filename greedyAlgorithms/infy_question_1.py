
# input consists of fee amount
# output no of coins or notes

# coins/notes: 500, 100, 50, 10, 5, 1

def find_min_coins(fee,coins):
    ans_coins = 0
    while fee>0:
        for i in coins:
            if fee>i:
                selected_coin = i
                break
        fee -= selected_coin
        ans_coins+=1
    return ans_coins


fee = 682
coins=[500,100,50,10,5,1]

print(find_min_coins(fee,coins))
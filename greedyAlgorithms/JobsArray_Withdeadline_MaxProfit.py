
# Given an array of jobs,every job has deadline and profit. Every job takes 1 unit. Max profit jobs...

# Sort the given jobs as per the Profit desc...
# after Assign the jobs to ans array_ from last possible location...



# n = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}

n = 17
Jobs = {(1,56,288),(2, 27 ,435),( 3,67 ,401 ),(4 ,64 ,368 ),(5 ,94 ,248 ),(6 ,54 ,361 ),(7, 43 ,108 ),(8 ,96 ,167 ),(9 ,73 ,251 ),(10, 96, 170 ),(11, 14, 156 ),(12 ,78, 184 ),(13 ,61 ,370 ),(14, 77, 424 ),(15 ,68, 397 ),(16 ,40, 375 ),(17, 36, 218)}

def ans(Jobs,n):
    profit = 0
    Jobs_sorted = sorted(Jobs,key=lambda i: i[2],reverse=True)
    ans_list = [0]*1000                 # 1000 time is max it can accept, so we can chage this if we have more time in the inputs......
    for i in Jobs_sorted:
        print(i)
        for j in range(i[1],0,-1):
            if ans_list[j-1] == 0:
                ans_list[j-1] = 1
                profit += i[2]
                break
    return [sum(ans_list),profit]

print(ans(Jobs,n))

        
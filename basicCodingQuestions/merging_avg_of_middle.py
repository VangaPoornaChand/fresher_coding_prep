

def sol(arr1,arr2):
    arr1.extend(arr2)
    arr1.sort()
    mid = (len(arr1)//2)-1
    print(arr1)
    return sum([arr1[mid],arr1[mid+1]])//2


# def sol(arr1, arr2):
#     temp_arr = []
#     for i in arr1:
#         for j in arr2:
#             temp_arr.extend([min(i,j),max(i,j)])
#             arr2.remove(j)
#             break
#     print(temp_arr)
#     mid = (len(temp_arr)//2)-1
#     return (temp_arr[mid]+temp_arr[mid+1])//2

# print(sol([1,2,3,4,5],[2,3,4,5,6]))

# print(sol([1,12,15,26,38],[2,13,17,30,45]))

print(sol([1,2,3,6],[4,6,8,10]))
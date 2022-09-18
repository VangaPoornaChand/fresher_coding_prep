

from ast import While
from turtle import back, backward


def sol(input_list, start_index,find_color):        # ["red","blue","green","yellow"],1,"yellow"
    if input_list[start_index] == find_color:
        return 0
    found_at = input_list.index(find_color)
    # forward serach....
    forward = 0
    index_ = start_index
    while True:                         # First step, check index/set index correctly, and if found break, then increment index and forward....
        if index_ == len(input_list):
            index_ = 0
        if input_list[index_] == find_color:
            break
        forward+=1
        # print(forward)
        index_+=1

    index_ = start_index
    backward = 0
    while True:
        if index_ < 0:
            index_=len(input_list)-1
        if input_list[index_] == find_color:
            break
        backward += 1
        # print(backward,index_,len(input_list),input_list)
        index_-=1

    return min([backward,forward])



print(sol(["red","blue","green","yellow"],2,"yellow"))

print(sol(["black","gray","brown","red","pink"],0,"black"))
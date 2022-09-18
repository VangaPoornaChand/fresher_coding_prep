
# Question: Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.


def MissingNumber(array,n):

    sum_of_array = sum(array)
    sum_of_first_n_numbers = int((n + 1)*(n)/2)
    return sum_of_first_n_numbers-sum_of_array


print(MissingNumber([1,2,3,5],5))
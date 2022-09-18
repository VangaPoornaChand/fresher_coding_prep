

def kLargest(arr, n, k):
    arr.sort(reverse=True)
    return arr[:k]


def kLargest(arr, n, k):
    # code here
    output_arr = []
    for i in range(k):
        m = max(arr)
        output_arr.append(m)
        arr.remove(m)
    return output_arr


# print(kLargest())


num = int(input())

num_s = str(num)

num_r = num_s[::-1]

if num_s == num_r:
    print("Palindrome")
else:
    print("not a Palindrome....")
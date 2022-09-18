

# N = int(input())
# S = input()
# CASH = int(input())
# A_SWAP = int(input())
# B_FLIP = int(input())

def FLIPS(S,CASH,B_FLIP):
    OUTPUT_S = ""
    for i in range(len(S)):
        if S[i]== "1":
            if CASH>B_FLIP:
                CASH -= B_FLIP
                OUTPUT_S += "0"
            else:
                OUTPUT_S += S[i]
        else:
            OUTPUT_S += S[i]

    return OUTPUT_S

def SWAPS(S,CASH,A_SWAP):
    TEMP_S = ""
    zeros = S.count("0")
    ones = S.count("1")
    for i in range(min([zeros,ones])):
        if CASH>A_SWAP:
            CASH-=A_SWAP
            TEMP_S += "0"
        else:
            TEMP_S += "1"
    else:
        TEMP_S+="1"*(len(S) - len(TEMP_S))
    return TEMP_S


# N = 4
S = "111011"
CASH = 7
A_SWAP = 1
B_FLIP = 3
OUTPUT_S = ""
swap_possible = False
TEMP_S = ""

if '0' in S and '1' in S:
    swap_possible = True

if swap_possible:
    if A_SWAP > B_FLIP:
        TEMP_S = SWAPS(S,CASH,A_SWAP)
        OUTPUT_S = FLIPS(TEMP_S,CASH,B_FLIP)
        print("OUTPUT:",int(OUTPUT_S,2))
    else:
        OUTPUT_S = FLIPS(S,CASH,B_FLIP)
        TEMP_S = SWAPS(OUTPUT_S,CASH,A_SWAP)
        print("OUTPUT:",int(TEMP_S,2))

if not swap_possible:
    OUTPUT_S = FLIPS(S,CASH,B_FLIP)
    

print("S :",S)
print("TEMP_S :",TEMP_S)
print("OUTPUT_S:",OUTPUT_S)




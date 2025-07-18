##### Sort a list of random numbers without using .sort().
numlist = [4, 3 , 8 , 12 , 24 , 10 , 7, 9 , 1, 0]

for x in range(len(numlist) - 1, 0 , -1):
    for i in range(x):
        if numlist[i] > numlist[i + 1]:
            numlist[i], numlist[i + 1] = numlist[i + 1], numlist[i]
            

print(numlist)
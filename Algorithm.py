"""
Hacker rank solution for compare the triplets
"""
print("\t\t Solution to Compare the triplets")
alice = input("Enter a lists of numbers: ").split()
bob = input("Enter a lists of numbers: ").split()
x = []
res = 0
res1 = 0
res2 = res, res1
for i, j in zip(alice, bob):
    #print(i, j)
    if i > j:
        res += 1
    elif i < j:
        res1 += 1
    else:
        res += 0
x.append(res2)
    #print(res)
print(res, res1)
#print(res1)

######################################################

"""
    Jumping the clouds

n = int(input("Enter a num: "))
num_J = input("Enter a number of jump: ").split()
"""

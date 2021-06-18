import random


randomList = random.sample(range(5000), 11)

print(randomList)
print('\n')
print("=================printing top numbers====================")
print('\n')



randomList = sorted(randomList, reverse=True)


print(randomList[:10])

print('\n')


# Asymptotic analysis of this implementation would be

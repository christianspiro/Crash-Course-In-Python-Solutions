
list = []
for item in range(0,21):
    list.append(item)
    print(item)

print(list)

secondList = []
for item in range(0, 1000001):
    secondList.append(item)

print(secondList)

print(min(secondList))
print(max(secondList))
thirdList = secondList
fourthList = thirdList + secondList
print(fourthList)

cubeList = []
for item in range(0,11):
    cubeList.append(item**3)
    print(cubeList)

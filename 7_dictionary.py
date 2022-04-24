## dictionary use to store data value in key
# ordered, changeable but do not allow duplicates

thisDict = {
    'firstName': 'Trinh',
    'lastname': 'Nhat'
}

print(thisDict['firstName'])
print(thisDict.get('firstName'))
thisDict['nickName'] = 'bi'
print(thisDict.values())
print(thisDict.items())

for i in thisDict.values():
    print(i)

thisDict.popitem() # this will be remove frist item
del thisDict['lastname']
thisDict.clear()
print(thisDict)
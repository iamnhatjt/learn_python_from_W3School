# list create using square brackets:

"""
list can ordered, changable, allow duplicate values
"""

newList = ['Trinh', 'Duong', "nhat"]
newList[1] = 'Huyen'
newList.insert(2,'haha')

newList.append('Minh huyen')

newList.remove('Trinh')    
newList.pop(1)
# print(newList)

#sort

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# u have to use copy() method to copy list

a = newList.copy()


## A set is a collection which is unordered, unchangeable*, and unindexed.
## a set items are unorder , unchangeable and do not allow  duplicate   values
# we can not access items in set by refering to an index or a key. so we use loop


thisSet = {'trinh', 'Duong', 'Nhat'}

for i in thisSet:
    print(i, ' ')


# we can not add item but we can add item

thisSet.add('haha')

# we can use remove() method to remove item
thisSet.remove('trinh')
print(thisSet)

thisSet.pop(    )
print(thisSet)
## tuples are colection ordered,unchangeable and allow duplicate values
#Tuples are used to store multiple items in a single variable.
 
#if u want to change, but tuples is unchange so we need to convert list collection
x = ('Minh', 'nhat')
y = list(x)
y[1] = "huyen"
print(y)


#unpacking tuple

y = ('trinh', 'duong','nhat')
(trinh,duong,nhat) = y
print(trinh)
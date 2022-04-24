# we can assign a multi line strings

multiLineString = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# print(multiLineString)

# Square brackets can be used to access elements of the string. remember first character start index 0

# LOOPING THOUGHT A STRING
# count string by len()
# check string use in or not in

sliceString = multiLineString

# print(len(sliceString))
# print(sliceString[:5].lower())

# when we wana remove whitespace before string, we use 'strip()' method; lower and upper to change capital or not

# print(sliceString.strip())

#we can slice string by split() method
# print(sliceString.split(' '))


#STRING FORMAT
""" we can not using '+' to combinet string with any type other
we used to format() method"""

age = 17
txt = 'Minh Huyen belong {} {}'
print(txt.format(age, 'i love u'))

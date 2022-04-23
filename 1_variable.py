"""
a variable is create that moment you first assign a value to it

variable don't need to be declared with any particular type, and can even change type affter they have  been set


"""

x = 3 # type of x is number
x = 'Trinh Duong Nhat'  #type of x is string

print('x: ', x)


# GET THE TYPE
#you can get data type of variable with the type() function

variableOne= 1
variableTwo = 'Trinh duong Nhat'
print('Type of variable One: ', type(variableOne))
print('Type of variable Two: ', type(variableTwo))



"""string variable can be declared either by using single or double quotes:"""

variableThree = 'Nhat'
""" the same """
variableFour = "Nhat"



#CASE-SENSITIVE
""" variable name are case-sensitive """

A = 'A'
a = 'a'

""" a different with A"""




#II, VARIABLE NAME
"""
+, a variable name must start with a letter or the underscore character
+, a variable name cannot start with a number
+, a variable name can be only contain apla-numeric characters and underscores(a-z, 0-9, _)
+, variable name are case-sensitive(name, Name and NAME are three different variables)

"""

# MULTIL WORD VARIABLE NAME RULE TO READABLE
""" each word variable name, except the first, start with capital letter, this call camel case(myVariableName)"""
""" each word variable name, start with capital letter, this call pascal case (MYVariableName) """
""" each word varibale name, separated by an underscored characted, this call SNAKE CASE (my_varibale_name)"""

#III, ASSIGN MULTIPLE VALUE     

III_variable_one, III_variable_two, III_variable_three = "orange", "banana", "cherry"
# print(III_variable_one,III_variable_two,III_variable_three)
""" Make sure number of value matches the number of variables, or else you will get an error"""

III_five = III_six = III_seven = 'duongnhat'
# print(III_five, III_six, III_seven)

#UNPACK A COLLECTION
""" if u have a collection like list, tuple, etc. python allow u to extract the values into variable.this call
is unpacking"""

nameOfTheClass = ['Duong Nhat', "Minh Huyen", "Duc Anh"]
nhat, huyen, duc_anh = nameOfTheClass
# print(nhat,huyen,duc_anh)


## IV, OUTPUT VARIABLE
""" the python use (print()) function is often used to output variable"""
""" to connect the valiable for displaying in the line, we are using "," or "+"
but when we use "," python auto add " " affter variable beside '+' is not
print(x, y, z)
or 
print(x + y + z)
"""

#but the best way to ouput we are using ',' because this can be combine two different type of variables


##V, GLOBAL VARIABLES
""" variable  create outside of a function are known as global variables
    varibale can be use anywhere by everybody, both inside and outside function
"""

variableGlobal = 'This is global variable'

def myfunction():
    print(variableGlobal)

# myfunction()

""" WACTH OUT: if u wana create a same variable inside function, this will be local, and can only using in side
the function, python save a new address of variable inside function different outside function.
but when we call in outside function, we point in old address of variable outside.
"""

globalOfThis = 'Trinh Duong Nhat'

def myfunc():
    globalOfThis = 'Minh Huyen'
    # print('inside func: ', globalOfThis, 'id', id(globalOfThis))

myfunc()
# print('outside func: ', globalOfThis, 'id', id(globalOfThis))


""" but normally, we using 'global' key word to set point address outside function
other way, this is way to set global variable, if outside don't have variable, py create a new global value"""


# globalOne = 'Trinh Duong Nhat'

def changeFunction():
    global globalOne 
    globalOne =  'Minh huyen'

changeFunction()










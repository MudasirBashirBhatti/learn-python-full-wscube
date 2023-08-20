# tuple is an ordered sequence of items same as a list. it is defined within a prenthesis(), where items are separated by comas(,). tuple are immutable

x = (1,'now',3.5, 1+3j)
print(x)
print(type(x))


x[1] = 'never'
print(x)    #return error() becuase it is immutable

# :key differences b/w tuple and list
# tuple is immutable, while list is mutable 
# tuple is faster to execute than list 
# tuple is defined within (). while list is defined within []
# atleast more than one items should present else it is not tuple

# if we write only one item in tuple than the data type will be of that item. 
y = (5)
print(y)            #return 5
print(type(y))      #return type = int
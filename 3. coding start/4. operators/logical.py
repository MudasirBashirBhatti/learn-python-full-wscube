# operator        description 
# "and"           return true if both are true
# "or"            return true if only one true
# "not"           reverse the result (true to false)

# and operator 
x=5
y=3
print(x==5 and y<x )  #return true because both are true
print(x==y and y<x )  #return false because x!=y

# or operator 
print(x==y or x>y)    #return true because one is true
print(x!=y or x<y)    #return true because both are true
print(x==y or x<y)    #return false because both are false

# not operator
print(not x==5)       #return false becuse it reverse the true

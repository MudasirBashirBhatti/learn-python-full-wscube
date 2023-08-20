# there are two membership operators
# 1. in 
# 2. not in

x = 'abcdef'
# "in" return (true) if particular character is available
print("a" in x)     #return true
print("A" in x)     #return false
print("ac" in x)    #return false
print("ab" in x)    #return true

# "not in" return (true) if particular character is not available 
print('m' not in x) #return true
print('a' not in x) #return true

print(".......array......")
arr = [3,5,6,8]
print(8 in arr)
print(7 in arr)

# :note
# we can not use (in && not in) only in numbers
# we can use it in array 



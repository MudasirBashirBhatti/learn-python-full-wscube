# operator       name        description

# &              AND         x&y

# |              OR          x|y

# ^              XOR         x^y

# bitwise works on bits (0 or 1)

# ************************ truth table ********************** 
# 1 = true    0 = false 

# A         B       A&B         A|B         A^B

# 0         0       0           0           0
# 0         1       0           1           1
# 1         0       0           1           1
# 1         1       1           1           0

x = 12
y = 8
print(".................x&y..................")
# first we need to convert them in binary
print("binary of x: " + bin(x))   #return 1100
print("binary of y: " + bin(y))   #return 1000

# compare both x and y in "&"
# 1     1    0   0
# 1     0    0   0
# ...................... 
# 1     0    0   0

print(x&y, bin(x&y))
# we get result 8 as binary of 8 is 1000

print(".................x|y..................")
# compare both x and y in "&"
# 1     1    0   0
# 1     0    0   0
# ...................... 
# 1     1    0   0

print(x|y, bin(x|y))


print(".................x^y..................")
# compare both x and y in "&"
# 1     1    0   0
# 1     0    0   0
# ...................... 
# 0     1    0   0

print(x^y, bin(x^y)) #retun 4 because binary of 0100 is four

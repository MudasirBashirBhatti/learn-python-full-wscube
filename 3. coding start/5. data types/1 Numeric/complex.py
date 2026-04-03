# numbers in the form of "a + bj" are called complex numbers 
x = 2+3j
print(x)
print(type(x))

y = 3 + 3j
print(y)
print(type(y))

# we can not write complex numbers
# x = 2i + 3j    'wrong'
# j is imaginary which is necessary for complex 
print(x.real)
print(x.imag)
print(x.conjugate())
print(abs(x)) # magnitude of the complex number

z = complex(2, 3)
print(z)   # (2+3j)

a = 2 + 3j
b = 1 + 2j

print("Addition:", a + b)   # addition 
print("Subtraction:", a - b)   # subtraction
print("Multiplication:", a * b)   # multiplication
print("Division:", a / b)   # division

b = -10
c = 5
print(abs(b)) # returns the absolute value of a number, which is the distance of the number from zero on the number line. For negative numbers, it returns the positive equivalent. In this case, abs(-10) will return 10.
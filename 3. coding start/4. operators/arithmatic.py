# "+" to add            5+2         return 7
# "-" to subtract       5-2         return 3
# "*" to multiply       5*2         return 10
# "/" to divide         5/2         return 2.5
# "%" for modulus       5%2         return 1
# "**" exponents        5**2        return 25
# "//" floor division   5//2        return 2 (2.25 to 2)

# **************** (PEMDAS) - Rules of precedence ************** 
#  1. Parentheses => 2. Exponents => 3. Multiplication => 4. Division => 5. Addition => 6. Subtraction 
# multiplication and division are on the same level, so we evaluate from left to right.
# 5 + 2 * 3 = 11 (Multiplication first)
# (5 + 2) * 3 = 21 (Parentheses first)

# **************** Modulus (%) in detail ************** 
# Python defines modulus using this identity:
# a%b = a - (a//b) * b //This enusures that the result of a%b has the same sign as b and is less than abs(b) in magnitude.
# For example:

print(5 % 2)   # Output: 1
print(-5 % 2)  # Output: 1
print(5 % -2)  # Output: -1
print(-5 % -2) # Output: -1


# **************** Exponents (**) in detail ************** 
# The exponentiation operator (**) in Python is used to raise a number to the power of another number. it is right-associative,
print(2 ** 3 ** 2)  # Output: 512 ==> 2 ** (3 ** 2) == 2 ** 9 == 512
# Membership operators: in, not in

# "in"      → checks if a value exists inside a sequence
# "not in"  → checks if a value does NOT exist inside a sequence


# 🔹 Example with string
x = "abcdef"

# "in" checks substring (case-sensitive)
print("a" in x)     # True  → 'a' exists
print("A" in x)     # False → case-sensitive
print("ac" in x)    # False → 'ac' is not a continuous substring
print("ab" in x)    # True  → 'ab' exists


# "not in"
print("m" not in x) # True  → 'm' is not present
print("a" not in x) # False → 'a' exists (so not in is False)


print("------- LIST (array) -------")

arr = [3, 5, 6, 8]

print(8 in arr)     # True
print(7 in arr)     # False


# 🔥 Real-life example
allowed_users = ["Ali", "Ahmed", "Sara"]
user = "Ali"

if user in allowed_users:
    print("Access granted")
else:
    print("Access denied")


# IMPORTANT:
# Membership operators CAN be used with:
# - strings
# - lists (arrays)
# - tuples
# - sets
# - dictionaries

# ❌ Wrong idea:
# "we cannot use in with numbers"

# ✔ Correct:
print(5 in [1, 2, 3, 4, 5])  # True → works with numbers inside a collection

# ❌ But this is invalid:
# print(5 in 10)  # Error → 10 is not iterable
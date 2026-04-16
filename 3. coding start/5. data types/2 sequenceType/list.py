# list is an ordered sequence of items. it is one of the most used data types in python and is very flexible(we can perform crud as it is mutable). lists are written in [].

arr = [1,"mudasir",3.2, 3+2j]
print(arr)      #return [1, 'mudasir', 3.2, (3+2j)]
print(type(arr))

# mutable example 
arr[1] = "mubashir"
print(arr)  #return [1, 'mubashir', 3.2, (3+2j)]

# list methods
arr.clear()
print(arr)  #return []

arr.append(10)
print(arr)  #return [10]

arr.count(10)  #return 1
print(arr.count(10))
print(arr.index(10))
print (arr.pop(0)) #return and remove 10 from list
print(arr.extend([1,2,3])) #return None but add 1,2,3 to list
print(arr)  #return [1, 2, 3]
print(arr.reverse()) #return None but reverse the list
print(arr)  #return [3, 2, 1]

print(arr.sort(key=None, reverse=True)) #return None but sort the list
print(arr)  #return [3, 2, 1]

words = ["apple", "banana", "cherry"]
words.sort(key=lambda x: x[-1]) #sort the list based on last character of each word
# key is a function that takes an argument and returns a value to be used for sorting purposes.
print(words)  #return ['banana', 'apple', 'cherry']
# list is an ordered sequence of items. it is one of the most used data types in python and is very flexible(we can perform crud as it is mutable). lists are written in [].

arr = [1,"mudasir",3.2, 3+2j]
print(arr)      #return [1, 'mudasir', 3.2, (3+2j)]
print(type(arr))

# mutable example 
arr[1] = "mubashir"
print(arr)  #return [1, 'mubashir', 3.2, (3+2j)]
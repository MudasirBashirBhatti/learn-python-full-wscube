# it is same just like range 
myStr = "I love Pakistan"

# now i wanted to extract or get "love" from whole string 
print(myStr[2:6])   #return "love" here 2 is starting of slice and 6 is ending index

print(myStr[2::])   # this will read whole string => return "love pakistan" "I " not included as we are starting from index 2

print(myStr[2::2])  #this will skip one character after each character
print(myStr[2::1])  #this will whole string

print(myStr[-1::-1])  #whole string will be reversed

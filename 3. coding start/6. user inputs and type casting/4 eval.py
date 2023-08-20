
# ...eval... 
# eval can handle both data type int and float(if you first give int and second time float it will automatically evaluate them and show result.)
firstNum = eval(input('First Number: '))
secondNum = eval(input('Second Number: '))
print(firstNum + secondNum)

# it can evaluate binary operations also 
myBin = eval(input('enter binary'))  #input(0b1010) which is equal to 10
digit = eval(input('enter number'))  #add any number

print(myBin+digit)

# it is proved that we can evaluate any type of numeric (int, float, binary) using eval.
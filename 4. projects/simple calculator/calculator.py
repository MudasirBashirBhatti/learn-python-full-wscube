num1 = eval(input('Enter Num1: '))
num2 = eval(input('Enter Num2: '))
operator = input('What do you wanted to perform e.g. +,-,/,*,%,**: ')

if(operator == "+"):
    print(num1 + num2)
elif(operator =="-"):
    print(num1 - num2)
elif(operator =="*"):
    print(num1*num2)
elif(operator =="/"):
    print(num1/num2)
elif(operator =="%"):
    print(num1%num2)
elif(operator =="**"):
    print(num1**num2)
else:
    print('incorrect operation perform')
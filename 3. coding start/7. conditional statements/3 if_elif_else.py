# if statements are more that one. we use if elif else e.g. grade system
marks= int(input('Enter your marks'))
if (marks>80 and marks<100):
    print('Your grade is : A+')
elif(marks>=60 and marks<=80):
    print('Your grade is: B')
elif(marks >= 40 and marks<60):
    print('Your grade is: C')
else:
    print("You are failed")
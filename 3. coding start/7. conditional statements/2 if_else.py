# if [conditional expression]:
#        [statement(s) to execute]
# else:
#      [alternate statement]

print('............check voting elegibilty............')
age = int(input('Enter Your age:'))
if(age<18):
    print('You can not vote')
else:
    print('You can vote')
# a powerful design pattern that allows you to modify or extend the behavior of functions or classes without changing their actual source code
def performExtraWork(func):
    def wrapper():
        print('extra kaam star kiya asal kaam se pehly')
        func()
        print('asal kaam k baad ka extra kaam khatam hua')
    return wrapper

@performExtraWork
def originalWork():
    print('Real functionality')

originalWork()


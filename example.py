def hello():
    print('Howdy!')
    print('Howdy!!')
    print('Hello there')

hello()
hello()
hello()

def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

print('Hello', end = '') #defines end char - default is newline 
print('World')
print('cat', 'dog', 'mouse')
print('cat', 'dog', 'mouse', sep='ABC') #defines new seperating char - default space

# def function_name()

# null in python = None
# None - only object of type None
# print technically returns 'None'
# default if no return statment in function

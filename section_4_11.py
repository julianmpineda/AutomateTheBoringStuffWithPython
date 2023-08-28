def div42by(divideBy):
    try:
        return 42 / divideBy #divide returns float
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')
        #returns "None" value from print statement
        # None is printed after the print

print(div42by(2))
print(div42by(12))
print(div42by(0)) #error ZeroDivisionError - stops program
print(div42by(1))

#example error if not passed int/float
print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    elif int(numCats) < 0:
        print('You can\'t have negative cats')
    else:
        print('That is not that many cats')
except ValueError:
    print('You did not enter a number.')

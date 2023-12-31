"""

***********
*         *
*         *
*         *
***********

"""

#pass a symbol and makes a box

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of length 1.')
    
    if width < 2 or height < 2:
        raise Exception('"Width" and "Height" must be greater than or equal to 2.')
    
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint('*', 15, 5)
boxPrint('$', 10, 1)
boxPrint('$', 1, 1)

# will print <2 but loop just doesn't run

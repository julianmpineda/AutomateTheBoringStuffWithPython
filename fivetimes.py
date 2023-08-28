print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))
    
# i default to 0
# up to not including x in range(x)

total = 0
for num in range(101):
    total = total + num
print(total)

#range(x) function that defines a range (0,10)

print('My name is')
for i in range(12,16):
    print('Jimmy Five Times ' + str(i))

# will perform from range 12 - 15
# equivalent to (int i = 12; i < 16)

print('My name is')
for i in range(0,10,2):
    print('Jimmy Five Times ' + str(i))

# will perform from range 0 - 9, with step 2
# equivalent to (int i = 0; i < 10; i + 2)

# range(start [inclusive0, end [exclusive], step)
# range(0, x, 1) [default set] 

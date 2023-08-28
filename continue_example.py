spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

#continue jumps back to top of while loop (checking condtion again) - skip everything under it for that iteration


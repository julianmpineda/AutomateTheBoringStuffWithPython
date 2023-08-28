eggs = 24 #global

def bacon():
    print(eggs)

def spam():
    global eggs # cast to global
    eggs = 'hello' 
    print(eggs)

def ham():
    eggs = 42 #new local variable, can have same name. Function assumes global if no assignment statement
    print(eggs)

bacon()
spam()
ham()
bacon() #global variable was changed in spam call

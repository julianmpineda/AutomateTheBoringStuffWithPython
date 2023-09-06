def eggs(cheese):
    cheese.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)
# "cheese" theoretically "destroyed", but still references original "spam" list,
# so changes are not local
 # mutable = references same objects

spam = ['apples',
        'oranges',
        'bananas',
        'cats']

print('Four score and seven' + \
      ' years ago')

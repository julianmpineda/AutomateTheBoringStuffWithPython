import re # import regular expressions

message = 'Call me 123-456-7890 tomorrow, or at 098-765-4321'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # \d = digit
    # use raw string to avoid having to escape all the backslashes
    # re.compile stores as regular expression object

phoneNum = phoneNumRegex.search(message)
    # build in function to apply regex to string
    # will return first match

print(phoneNum.group())
    # .group() removes metatext from return

phoneNumAll = phoneNumRegex.findall(message)
    # find all returns all instances
    # returns list

print(phoneNumAll)

#! python3

# copy etracts phone numbers and code from clipboard

import re, pyperclip

# TODO: regex for numbers

phoneRegex = re.compile(r'''
# 123-456-7890, 456-7890, (123) 456-7890, 123-456-7890 ext 1234

(((\d\d\d)|(\(\d\d\d\)))?  # area code (optional)
(\s|-)                     # separator
\d\d\d                     # first 3 digits
-                          # separator
\d\d\d\d                   # last 4 digits
(((ext(\.)?\s)|x)          # optional extension word
  (\d{2,5}))?)             # optional extension number
''', re.VERBOSE)
# regex for emails

emailRegex = re.compile(r'''
#name.+_@domain.com/gov/net

[a-zA-Z0-9_.+]+ #name
@               # @
[a-zA-Z0-9_.+]+ # domain
''', re.VERBOSE)

# get text off clipboard
text = pyperclip.paste()

# get email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# copy to clipboard
# change this code to change output
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

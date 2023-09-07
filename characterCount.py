import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} # 'char' : count

for character in message.upper(): # ok to use to iterate through string
    count.setdefault(character, 0) # automatically creates char:count pair
    count[character] = count[character] + 1

prettyText = pprint.pformat(count) # will create pretty string instead of printing
pprint.pprint(count)

# python 3.5 doesnt seem to count spaces but 3.11 does
# also lists result in different order - consequence of unordered dictionary?
# triple quote?

# 'pretty print' pre formats in order and single column


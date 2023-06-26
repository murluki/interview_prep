import re

#string
s = input()
#pattern
m = input()
if re.search(f'(?={m})',s):
    for i in re.finditer(f'(?={m})',s):
        print((i.start(),i.start()+len(m)-1))
else:
    print((-1,-1))
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

    import re

    s = input()
    k = input()

    m = re.finditer(f"(?=({k}))", s)

    if re.search(k, s):
        for x in m:
            print((x.start(1), x.end(1) - 1))
    else:
        print((-1, -1))
import re
#?<= lower bound of regex
#?= upper bound of regex
# [] what we are looking for
# {how many occurencies}

r = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])",input())
print("\n".join(r) if r else "-1")
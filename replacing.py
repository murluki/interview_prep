import re

text = []
for _ in range(int(input())):
    text.append(input())
text = "\n".join(text)

text = re.sub(r"(?<=[\s])\&\&(?=[\s])", "and", text)
text = re.sub(r"(?<=[\s])\|\|(?=[\s])", "or", text)
print(text)
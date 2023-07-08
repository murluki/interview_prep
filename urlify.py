# Python code for the same approach
def replaceSpaces(input):
    rep = "%20"
    for i in range(len(input)):
        if (input[i] == ' '):
            input = input.replace(input[i], rep)
    print(input)


# driver code
input = "Mr John Smith"
replaceSpaces(input)

if __name__ == '__main__':

    nested_list = []
    second_list = []
    names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls = [name, score]
        nested_list.append(ls)

#TO-DO: make it one nested loop(?)

    min_score = min(nested_list, key=lambda x: x[1])
    for x in nested_list:
        if (x != min_score):
            second_list.append(x)

    second_min = min(second_list, key=lambda x: x[1])

    for name, score in second_list:
        if (score == second_min[1]):
            names.append(name)

    names.sort()
    for x in names:
        print(x)


percentages = [str(100 - i) for i in range(0,101,10)]

for percentage in percentages:
    print(' '*(3 - len(percentage)), end='')
    print(percentage + '|')
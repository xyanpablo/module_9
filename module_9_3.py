first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(i) - len(j)) for i, j in zip(first, second) if len(i) != len(j))
second_result = (len(i) == len(j) for i in first for j in second if first.index(i) == second.index(j))

print(list(first_result))
print(list(second_result))
from itertools import combinations


def all_variants(text):
    for letter in range(1, len(text) + 1):
        yield from (''.join(combo) for combo in combinations(text, letter))


a = all_variants("abc")
for i in a:
    print(i)

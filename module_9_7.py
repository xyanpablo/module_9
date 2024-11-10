
def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        d = 2
        while res % d != 0:
            d += 1
        if d * d > res:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

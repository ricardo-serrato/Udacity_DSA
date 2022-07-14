def get_fib(position):
    if position < 2:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)

    return -1


print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
import time

def nation_total(y):
    start = time.time()
    x = y * (y + 1) / 2
    stop = time.time()
    print(stop - start)
    return x


print(nation_total(1000))


def nation_total_loop(y):
    start = time.time()
    x = 0
    for count in range(1, y + 1):
        x += count
    stop = time.time()
    print(stop - start)
    return x


print(nation_total_loop(1000))


def nation_total_recursive(y):
    if y == 1:
        return y
    return y + nation_total_recursive(y - 1)


print(nation_total_recursive(100))

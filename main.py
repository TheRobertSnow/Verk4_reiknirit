def memoize(f):
    """Returns a memoized version of f"""
    memory = {}
    def memoized(*args):
        if args not in memory:
            memory[args] = f(*args)
        return memory[args]
    return memoized

@memoize
def my_fact(x):
    assert x >= 0
    if x == 0:
        return 1
    return x * my_fact(x - 1)
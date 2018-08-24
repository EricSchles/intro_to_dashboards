import code
def decorator(f):
    def internal(args):
        return f(args)+5
    return internal

@decorator
def func(x):
    return x


code.interact(local=locals())

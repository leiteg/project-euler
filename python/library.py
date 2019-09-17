import functools


def memoize(fn):
    """Decorator to memoize a function's results"""
    setattr(fn, "table", {})

    @functools.wraps(fn)
    def decorator(n):
        setattr(decorator, "fn", fn)
        if n not in fn.table:
            fn.table[n] = fn(n)
        return fn.table[n]

    return decorator

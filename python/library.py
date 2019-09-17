def memoize(fn):
    setattr(fn, "table", {})

    def decorator(n):
        setattr(decorator, "fn", fn)
        if n not in fn.table:
            fn.table[n] = fn(n)
        return fn.table[n]

    return decorator

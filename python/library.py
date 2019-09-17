import functools
import time
import sys


def memoize(fn):
    """Decorator to memoize a function's results"""
    fn.table = {}
    fn.total_calls = 0
    fn.real_calls = 0

    @functools.wraps(fn)
    def decorator(n):
        fn.total_calls += 1
        if n not in fn.table:
            fn.real_calls += 1
            fn.table[n] = fn(n)
        return fn.table[n]

    return decorator


def timeit(fn):
    """Decorator to measure execution time"""

    @functools.wraps(fn)
    def decorator(*args, **kwargs):
        t0 = time.monotonic()
        ret = fn(*args, **kwargs)
        t1 = time.monotonic()
        print(f"INFO: Function {fn.__name__!r} executed in {t1-t0:.3} seconds",
              file=sys.stderr)
        return ret

    return decorator

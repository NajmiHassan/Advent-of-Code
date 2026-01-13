from functools import lru_cache

def pattern(o, towels):
    towels = list(filter(lambda t: t in o, towels))
    @lru_cache(None)
    def f(res):
        if res == o:
            return 1
        if len(res) >= len(o) or not o.startswith(res):
            return 0
        return any(f(res + t) for t in towels)
    return f('')

with open('input.txt') as f:
    towels, order = f.read().split('\n\n')
    towels = towels.split(', ')
    order = order.split()

    print(sum(pattern(o, towels) for o in order))
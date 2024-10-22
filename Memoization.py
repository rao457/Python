import time
ef_cache = {}
def expensive_func(n):
    if n in ef_cache:
        return ef_cache[n]
    print(f"Computing {n}")
    time.sleep(1)
    result =  n*n
    ef_cache[n] = result
    return result

result = expensive_func(5)
print(result)
result = expensive_func(10)
print(result)
result = expensive_func(5)
print(result)
result = expensive_func(10)
print(result)
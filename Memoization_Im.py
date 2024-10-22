import time
ef_cache = {}
def expense_func(n):
    if n in ef_cache:
        print(ef_cache[n])
    print(f"Computing {n}.....")
    time.sleep(1)
    result = n * n
    ef_cache[n] = result
    print(result)
expense_func(5)
expense_func(10)
expense_func(5)
expense_func(10)
# Memoization first appeared in Xeven Solutions interview keep it in mind
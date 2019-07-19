def fun(n):
    num = 0
    while num < n:
        yield num
        num += 2

for f in fun(10):
    print(f)
def fib_l(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b - 1
        return b

ans = fib_l(42)
print(ans)
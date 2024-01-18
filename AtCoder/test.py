# def fib_l(n):
#     a, b = 1, 2
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         for _ in range(n - 2):
#             a, b = b, a + b - 1
#         return b

# ans = fib_l(42)
# print(ans)

def fib_l(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for _ in range(n-2):
            a, b = b, a + b
        return b

ans = fib_l(42)
print(ans)
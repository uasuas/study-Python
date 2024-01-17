N, S = map(int, input().split())
count = sum(1 for red in range(1, N+1) for blue in range(1, N+1) if red + blue <= S)
print(count)
N, X, Y = map(int, input().split())
count = sum(1 for n in range(1, N+1) if n % X == 0 or n % Y == 0)
print(count)
N, X, Y = map(int, input().split())
# sum(1 for nの部分で以降で記述する、範囲内で条件に合う場合に1を生成して総和する
count = sum(1 for n in range(1, N+1) if n % X == 0 or n % Y == 0)
print(count)
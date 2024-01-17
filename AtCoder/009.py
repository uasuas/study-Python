N, S = map(int, input().split())
# listはリストを生成する組み込み関数、"hello"=['h', 'e', 'l', 'l', 'o']
A = list(map(int, input().split()))
def is_subset_sum(N, arr, S):
    # range(N + 1) は 0 から N までの整数を生成
    # for _ in range(N + 1) は _に代入することなく N + 1 回ループ、_は「この変数は使用しない」という目印
    # dp[i][j]: i番目までのカードを使用して合計がjになるようにできるかどうか
    dp = [[False] * (S + 1) for _ in range(N + 1)]

    # 0枚のカードを使用して合計が0にできる
    for i in range(N + 1):
        dp[i][0] = True

    for i in range(1, N + 1):
        for j in range(1, S + 1):
            # i番目のカードを使用する場合
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            # i番目のカードを使用しない場合
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[N][S]

ans = "Yes" if is_subset_sum(N, A, S) else "No"

print(ans)
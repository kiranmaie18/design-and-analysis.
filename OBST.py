def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j + 1):
                cost = dp[i][k - 1] if k > i else 0
                cost += dp[k + 1][j] if k < j else 0
                cost += sum(freq[i:j + 1])

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]
keys = [10, 20, 30]
freq = [3, 2, 5]

result = optimal_bst(keys, freq)
print("Optimal Cost of BST:", result)

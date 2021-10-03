def MatChainMul(arr, n):
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        dp[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            dp[i][j] = 10 ** 10
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n - 1]


arr = [1, 2, 3, 4]
size = len(arr)

print("Minimum number of multiplications are" + str(MatChainMul(arr, size)))
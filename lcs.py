def LCSubstring(X, Y, m, n):
    dp = [[0 for k in range(n + 1)] for l in range(m + 1)]

    result = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                dp[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result


X = 'abcdxyz'
Y = 'xyzabcd'

m = len(X)
n = len(Y)

print('Length of Longest Common Substring is', LCSubstring(X, Y, m, n))
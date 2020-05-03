def solution(n):
    dp = [[0] * n for _ in range(n + 1)]
    dp[0][0] = dp[1][1] = dp[2][2] = 1

    for j in range(1, n):
        for i in range(n + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= j:
                dp[i][j] += dp[i - j][j - 1]

    return dp[-1][-1]


# for i in range(3, 201):
#     print(i, solution(i))

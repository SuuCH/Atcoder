
s = input()
s_len = len(s)
t = 'chokudai'
t_len = len(t)
dp = [[0] * (s_len+1)] * (t_len +1)

for i in range(t_len+1):
  for j in range(s_len+1):
    if i == 0:
      dp[i][j] = 1
      continue
    if j == 0:
      dp[i][j] = 0
      continue
    if s[j-1] != t[i-1]:
      dp[i][j] = dp[i][j-1]
    else:
      dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[-1][-1] % (10**9 + 7))              


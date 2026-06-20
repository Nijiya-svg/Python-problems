

def is_match(text, pattern):
    # dp[i][j] = True if text[:i] matches pattern[:j]
    rows, cols = len(text), len(pattern)
    dp = [[False] * (cols + 1) for _ in range(rows + 1)]
    dp[0][0] = True

    
    for j in range(1, cols + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif pattern[j - 1] == '?' or text[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[rows][cols]


tests = [
    ("aXXXb", "a*b"),
    ("hello", "h?llo"),
    ("hello", "world"),
]

for text, pattern in tests:
    result = is_match(text, pattern)
    print(f"text='{text}', pattern='{pattern}' → Match: {result}")
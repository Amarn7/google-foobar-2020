def solution(s):
    ans = count = 0
    for ch in s:
        if ch == '>':
            count += 1
        elif ch == '<':
            ans += count
    return ans << 1

# print(solution("--->-><-><-->-"))
# print(solution(">----<"))
# print(solution("<<>><"))

def solution(x, y):
  layer = x + y - 1
  pre_total = layer * (layer - 1) // 2
  return str(pre_total + x)

# print(solution(3, 2))

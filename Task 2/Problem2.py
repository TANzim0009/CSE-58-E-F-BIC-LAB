text = input().strip()
k = int(input())

patterns = []
for i in range (len(text)- k+1):
  patterns.append(text[i:i+k])
  max_count = 0
  for p in patterns:
    if patterns.count(p) > max_count:
      max_count = patterns.count(p)
result = []
for p in patterns:
  if patterns.count(p) == max_count and p not in result:
    result.append(p)
print(*result)

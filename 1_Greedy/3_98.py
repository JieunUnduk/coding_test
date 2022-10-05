N, M = map(int, input().split())
x = 0
for i in range(N):
  A = list(map(int, input().split()))
  if x < min(A):
    x = min(A)

print(x)
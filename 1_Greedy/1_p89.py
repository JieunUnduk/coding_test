# 예제 3-1 거스름돈 (p.89)
count = 0
N = int(input())

# for i in [500, 100, 50, 10]:
#   if N > 0:
#     count += N // i
#     N = N - i *count 

for i in [500, 100, 50, 10]:
  count += N // i
  N %= i
    

print(count)
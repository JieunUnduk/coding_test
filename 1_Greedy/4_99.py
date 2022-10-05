n, k = map(int, input().split())
count = 0
new_n = n

while new_n != 1 :
  if new_n % k == 0:
    new_n = new_n // k
  else :
    new_n = new_n -1
  count +=1

print(count)
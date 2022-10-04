# p.92 큰 수의 법칙
N, M, K = map(int, input().split())

# Numbers = []
# for i in map(int, input().split()):
#   Numbers.append(i)
Numbers = list(map(int, input().split()))

# a = max(Numbers)
# Numbers.remove(max(Numbers))
# b = max(Numbers)
# Numbers.remove(max(Numbers))

Numbers.sort() # 정렬하기
a = Numbers[N-1]
b = Numbers[N-2]

a_count = ( M // (K + 1) ) * K
b_count = M - (a_count)

print(a*a_count + b*b_count)
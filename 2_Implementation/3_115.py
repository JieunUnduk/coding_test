# A = input()
# x = A[0]
# y = A[1]
# count = 0

# if x in ['c', 'd', 'e', 'f']:
#   if y in ['2', '7']:
#     count = 6
#   elif y in ['3', '4', '5', '6']:
#     count = 8
#   else : count = 4
    
# elif x in ['b', 'g']:
#   if y in ['1', '8']:
#     count = 3
#   elif y in ['2', '7']:
#     count = 4
#   else :
#     count = 6

# else : 
#   if y in ['1', '8']:
#     count = 2
#   elif y in ['2', '7']:
#     count = 3
#   else : 
#     count = 4

# print(count)

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0

for step in steps : 
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)
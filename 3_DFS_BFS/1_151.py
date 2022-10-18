n, m = map(int, input().split())
board = []
for i in range(n):
  board.append(list(int, input().split()))

def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y >= m :
    return False
    
  if board[x][y] == 0 :
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True

  return False


result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True :
      result += 1

print(result)
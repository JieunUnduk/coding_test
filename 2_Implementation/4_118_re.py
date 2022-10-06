n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 방문할 위치 표시 위해 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
d[x][y] = 1 # 시작 지점 방문 처리

# 전체 맵 정보를 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True : 
    # (1) 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # (2) 회전한 이후, 다음 칸으로 이동해도 되는 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # (3) 회전한 이후, 다음 칸으로 이동할 수 없는 경우
    else :
        turn_time += 1
        # 만약 회전한 횟수가 4회 이하라면, 다시 (1)부터 반복

    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dx[direction]

        # 육지라면 이동해
        if array[nx][ny] == 0 : 
            x = nx
            y = ny
        
        # 바다라면
        else : 
            break

        turn_time = 0 

print(count)
         


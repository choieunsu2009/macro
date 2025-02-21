import pyautogui

# 지정 위치 확인용 코드
# while 1:
#     print(pyautogui.position())

# 변수지정
loop = int(input("반복 횟수는? >>> "))
temp = 0
times = []

# 시간 간격 지정
for i in loop:
    temp += int(input("분? >>> ")) * 60
    temp += int(input("초? >>> "))
    print(i + 1, "번 째 입력 받음 : ", temp, "초")
    print("")
    times.append(temp)
    temp = 0

# 실행
for j in range(0, loop):
    print(j+1,"번째 작동 중... ",loop+"번 작동 후 정지")
    pyautogui.click(1718,1209,button= 'left', interval= times[j])

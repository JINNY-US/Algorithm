# 가위바위보 게임을 완성해주세요!
# 이중 if 문사용
# 유저 인풋 받을때 while문 사용

import random

options = ['가위', '바위', '보']
computer_choice = random.choice(options)

print("가위, 바위, 보 중에 하나를 골라주세요")

while True:
    user_input = input()
    if user_input not in options:
        print("잘못 입력하셨습니다. 다시 입력해주세요!")
        continue
    if user_input == '가위':
        if computer_choice == '가위':
            print("draw!")
        elif computer_choice == '바위':
            print("lose!")
        else:
            print("win!")
    elif user_input == '바위':
        if computer_choice == '가위':
            print("win!")
        elif computer_choice == '바위':
            print("draw!")
        else:
            print("lose!")
    else:
        if computer_choice == '가위':
            print("lose!")
        elif computer_choice == '바위':
            print("win!")
        else:
            print("draw!")
    break

print(f"당신은 {user_input}를 냈습니다.")
print(f"컴퓨터는 {computer_choice}를 냈습니다.")

#------------------------------------------------------------------

# 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
# 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.

total = int(input())
type = int(input())
sum = 0

for i in range(0, type):
    price, count = map(int, input().split())
    sum += price * count
    
if sum == total:
    print("Yes")
else:
    print("No")

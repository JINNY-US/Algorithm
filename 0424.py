# 조건문을 추가해서 사용자 인풋이 정답보다 작다면 up
# 정답보다 크다면 down을 프린트하게 해주세요

import random

answer = random.randint(10, 100)
while True:
    user_input = int(input())
    if user_input > answer:
        print("down!")
    elif user_input < answer:
        print("up!")
    else:
        print("정답입니다!")
        break
print("게임이 끝났습니다.")


# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

test = int(input())

for t in range(test):
    numA, numB = map(int, input().split())
    sum = numA + numB
    t += 1
    print(f"Case #{t}: {sum}")


# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.

while True:
    numA, numB = map(int, input().split())
    sum = numA + numB
    if sum == 0:
        break
    print(sum)
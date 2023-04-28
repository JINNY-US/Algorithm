import random

def match_game(user, com):
    print(f"당신은 {user_input}을(를) 냈습니다!")
    print(f"컴퓨터는 {computer_choice}을(를) 냈습니다!")
    if user == '가위':
        if com == '가위':
            return "비겼다."
        elif com == '바위':
            return "졌다."
        else:
            return "이겼다."
    elif user == '바위':
        if com == '가위':
            return "이겼다."
        elif com == '바위':
            return "비겼다."
        else:
            return "졌다."
    else:
        if com == '가위':
            return "졌다."
        elif com == '바위':
            return "이겼다."
        else:
            return "비겼다."


def match_result(user, com):
    if user >= 2:
        print("\n당신은 게임에서 승리하셨습니다!")
    elif com >= 2:
        print("\n당신은 게임에서 패배하셨습니다!")
    else:
        print("\n3판 중 아무도 2승을 하지 못했으므로 이 게임은 무효입니다.")


options = ['가위', '바위', '보']
user_cnt = 0
com_cnt = 0

for i in range(3):
    while True:
        computer_choice = random.choice(options)
        user_input = input("\n가위, 바위, 보 중에서 골라주세요: ")
        if user_input in options:
            result = match_game(user_input, computer_choice)
            if result == "이겼다.":
                user_cnt += 1
                print(f"win!\nYOU: {user_cnt}, COM: {com_cnt}")
            elif result == "졌다.":
                com_cnt += 1
                print(f"lose!\nYOU: {user_cnt}, COM: {com_cnt}")
            else:
                print(f"draw!\nYOU: {user_cnt}, COM: {com_cnt}")
        else:
            print("잘못 입력하셨습니다.")
            continue
        break

match_result(user_cnt, com_cnt)

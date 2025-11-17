print("game_logic IMPORTED")
print("Содержит start_game:", 'start_game' in dir())


from scenes import *
from riddles import *

def start_game():
    print("Представьте, что Вы могучий богатырь. Выбери свой путь. Все действия имеют последствия!")

    while True:
        print(MENU)
        path = input("Что Вы выберите? (1/2/3): ")
        print(f"Вы выбрали путь: {path}")

        if path == "1":
            path_left()
        elif path == "2":
            path_right()
        elif path == "3":
            path_forward()
        else:
            print("Нет такого пути!")

        again = input("Хотите ли вы попробовать снова? (да/нет): ")
        if again.lower() != "да":
            print("Конец игры.")
            break


def path_left():
    print(LEFT_START)
    choice = input("Ваши действия: 1) Погнаться 2) Осмотреть место (1/2): ")

    if choice == "1":
        print(LEFT_CHASE)
        sub = input("1. Кричать 2. Выбираться самим (1/2): ")

        if sub == "1":
            print(LEFT_SWAMP_LESHY)
            answer = input("Ваш ответ: ")

            if riddle_shadow(answer):
                print(LEFT_LESHY_WIN)
            else:
                print(LEFT_LESHY_LOSE)

        elif sub == "2":
            print(LEFT_SWAMP_BIRD)
            answer = input("Ваш ответ: ")

            if riddle_wind(answer):
                print(LEFT_BIRD_WIN)
            else:
                print(LEFT_BIRD_LOSE)

    elif choice == "2":
        print(LEFT_WATER_START)
        answer = input("Ваш ответ: ")

        if riddle_time(answer):
            print(LEFT_WATER_CORRECT)
            way = input("1) Через болото 2) В обход (1/2): ")

            if way == "1":
                print(LEFT_WATER_WIN)
            else:
                print(LEFT_WATER_DIE)
        else:
            print(LEFT_WATER_LOSE)


def path_right():
    print(RIGHT_START)
    answer = input("Ваш ответ: ")

    if riddle_mirror(answer):
        print(RIGHT_CHOICES)
        choice = input("1) Болото 2) В обход (1/2): ")

        if choice == "1":
            print(RIGHT_BOG)
            sub = input("1) Поговорить 2) Убежать (1/2): ")

            if sub == "1":
                print(RIGHT_KIKIMORA_TALK)
            else:
                print(RIGHT_KIKIMORA_DIE)

        elif choice == "2":
            print(RIGHT_FOREST)
            sub = input("1) Спросить 2) Идти молча (1/2): ")

            if sub == "1":
                print(RIGHT_FOREST_LOOP)
            else:
                print(RIGHT_FOREST_RING)
    else:
        print(RIGHT_LOSE)


def path_forward():
    print(FORWARD_START)
    answer = input("Ваш ответ: ")

    if riddle_echo(answer):
        print(FORWARD_AFTER_RIDDLE)
        choice = input("1) Уйти 2) Разрушить чары (1/2): ")

        if choice == "1":
            print(FORWARD_LEAVE)
        else:
            print(FORWARD_PALACE)
            sub = input("1) Принять дар 2) Сразиться (1/2): ")

            if sub == "1":
                print(FORWARD_GIVE_UP)
            else:
                print(FORWARD_WIN)
    else:
        print(FORWARD_LOSE)

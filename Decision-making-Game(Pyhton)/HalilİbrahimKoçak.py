import random
FRIEND, ENEMY, BUTTON = 0, 1, 2

def game_func():
    g_list = [random.choice([FRIEND, ENEMY, BUTTON]) for _ in range(10)]
    hp = 10
    sc = 0

    cnt_fr = lambda lst: len(list(filter(lambda x: x == FRIEND, lst)))
    cnt_en = lambda lst: len(list(filter(lambda x: x == ENEMY, lst)))

    def disp_stat():
        print(f"Game list: {g_list}")
        print(f"There are {cnt_fr(g_list)} friends and {cnt_en(g_list)} enemies")
        print(f"Your health is {hp}")
        print(f"Your score is {sc}")
        print(f"You see a {'friend' if g_list[0] == FRIEND else 'enemy' if g_list[0] == ENEMY else 'button'}")
        print("1 - Interact")
        print("2 - Ignore")

    while g_list:
        disp_stat()
        act = input("What will you do? ")

        if act == "1":
            elem = g_list.pop(0)

            if elem == FRIEND:
                hp += random.randint(1, 3)
                sc -= 1
                print(f"Your health increased to {hp}, but your score decreased to {sc}.")

            elif elem == ENEMY:
                hp -= random.randint(1, 3)
                sc += 1
                print(f"Your health decreased to {hp}, but your score increased to {sc}.")

            elif elem == BUTTON:
                trans_to = FRIEND if random.choice([True, False]) else ENEMY
                g_list = [trans_to if e != BUTTON else BUTTON for e in g_list]
                print(f"All {'friends' if trans_to == FRIEND else 'enemies'} became {'enemies' if trans_to == FRIEND else 'friends'}!")

        elif act == "2":
            g_list.pop(0)
            print("Ignored.")

        if hp <= 0:
            print("You died!")
            return

        elif not g_list:
            print(f"You won! Your final score is {sc}.")
            return

if __name__ == "__main__":
    game_func()

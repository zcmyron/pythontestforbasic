import random

import matplotlib.pyplot as plt


def give_the_number():
    number = random.randint(1, 100)

    if number <= 50:
        # print(number, "The number is 1 to 50. You lose. Play again.")
        return False
    else:
        # print(number, "The number is 51-100, you win! Play more to become richman!")
        return True


# x=0
# while x<100:
#     result=give_the_number()
#     print(result)
#     x+=1


def a_fool(funds, wager, game_count):
    current_game_count = 0
    x = []
    y = []
    while current_game_count < game_count:
        if give_the_number():
            funds += wager
            x.append(current_game_count)
            y.append(funds)
            # print("Now you have: ", funds)
        else:
            funds -= wager
            x.append(current_game_count)
            y.append(funds)
            # print("Now you have: ", funds)
        current_game_count += 1
    if funds < 0:
        funds = "Penniless"
    plt.plot(x, y)
    # print("How rich the fool is:", funds)


n = 0
while n < 100:
    a_fool(100000, 100000, 1000)
    n += 1
plt.xlabel("How many games does the fool played")
plt.ylabel("Funds")
plt.show()

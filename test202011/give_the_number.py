import random

def give_the_number():
    number=random.randint(1,100)

    if number <= 50:
        print(number, "The number is 1 to 50. You lose. Play again.")
    else:
        print(number, "The number is 51-100, you win! Play more to become richman!")
x=0
while x<100:
    result=give_the_number()
    print(result)
    x+=1
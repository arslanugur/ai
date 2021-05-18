import random

def main():
    prob = 0.80
    if random.random() < prob:
        favourite = "dogs"  # change this
    elif random.random() < 0.5:
        favourite = "cats"
    else:
        favourite = "bats"
    print("I love " + favourite) 


main()

# 2ND EDITION

import random

def main():
    prob = random.random()
    if prob < 0.1:
        favourite = "bats"
    if prob < 0.2 and prob > 0.1:
        favourite = "cats"
    if prob > 0.2:
        favourite = "dogs"
      # change this
    print("I love " + favourite) 


main()



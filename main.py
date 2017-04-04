import random
import time
import sys
sys.path.append('termcolor')
from termcolor import colored

class Box:
    """
    A box containing balls with red and blue balls
    Attributes:
        red_ball: an integer, the number of red balls
        blue_ball: an integer, represents the number of blue balls
        name: the name of the box
    """
    def __init__(self, name, red, blue):
        self.name = name
        self.red_ball = red
        self.blue_ball = blue

    def transfer_random(self, another_box):
        """Take a random ball from this box and put into another box, the point that it can be red or blue, randomly."""
        random_num = random.randint(a=1, b=self.red_ball + self.blue_ball)
        if random_num <= self.red_ball:  # If this, transfer red ball to the other box
            self.red_ball += -1
            another_box.red_ball += 1
        else:
            self.blue_ball += -1
            another_box.blue_ball += 1

# The fun begins now:
blue_box = Box(name='blue-box', red=0, blue=30)
red_box = Box(name='red-box', red=30, blue=0)

while True:
    blue_box.transfer_random(red_box)
    red_box.transfer_random(blue_box)

    # print them out for fun
    for _ in range(blue_box.blue_ball):
        print (colored('o', 'blue'), end='')
    for _ in range(blue_box.red_ball):
        print(colored('o', 'red'), end='')
    print(end='   |   ')

    for _ in range(red_box.blue_ball):
        print(colored('o', 'red'), end='')
    for _ in range(red_box.red_ball):
        print (colored('o', 'blue'), end='')

    print()
    print()

    time.sleep(0.1)
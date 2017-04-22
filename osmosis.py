# I'll modify it to demonstrate the osmosis phenomenon:
import random
import time
import sys
sys.path.append('termcolor')
from termcolor import colored

class solutionWithSemipermeableMembrane:
    """
    A solution containing balls with solute and solvent balls
    Attributes:
        solute_ball: an integer, the number of solute balls
        solvent_ball: an integer, represents the number of solvent balls
        name: the name of the solution
    """
    def __init__(self, name, solute, solvent):
        self.name = name
        self.solute_ball = solute
        self.solvent_ball = solvent

    def transfer_random(self, another_solution):
        """Take a random ball from this solution and put into another solution, the point that it can be solute or solvent, randomly."""
        random_num = random.randint(a=1, b=self.solute_ball + self.solvent_ball)
        if random_num <= self.solute_ball:  # solute BALLS SHALL NOT PASS THE SEMIPERMEABLE MEMBRANE
            # self.solute_ball += -1
            # another_solution.solute_ball += 1
            pass
        else:  # solvent BALLs CAN PASS THE SEMIPERMEABLE MEMBRANE
            self.solvent_ball += -1
            another_solution.solvent_ball += 1

# The fun begins now:
solution2 = solutionWithSemipermeableMembrane(name='high-concentration', solute=10, solvent=10)
solution1 = solutionWithSemipermeableMembrane(name='low-concentration', solute=2, solvent=20)

while True:
    solution2.transfer_random(solution1)
    solution1.transfer_random(solution2)

    # print them out for fun

    for _ in range(solution1.solute_ball):
        print (colored('o', 'red'), end='')
    for _ in range(solution1.solvent_ball):
        print(colored('o', 'blue'), end='')
    print(end='|')

    for _ in range(solution2.solvent_ball):
        print (colored('o', 'blue'), end='')
    for _ in range(solution2.solute_ball):
        print(colored('o', 'red'), end='')
    print()
    print()

    time.sleep(0.1)

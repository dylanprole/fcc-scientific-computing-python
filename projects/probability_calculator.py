# This code runs experimental simulations to calculate proabibilities of balls
# being drawn from a hat
# Replit code: https://replit.com/@dylanprole/boilerplate-probability-calculator

from copy import deepcopy
import random 
# Consider using the modules imported above.

class Hat:
    counter = 0

    # Construct a hat object
    def __init__(self, **kwargs):
        # Create ID for each hat
        self.id = '{:3.0f}'.format(Hat.counter).replace(' ', '0')
        Hat.counter += 1

        # Create list to store all balls
        self.contents = list()

        # iterate throught kwargs to get each ball entered
        for colour, ball_count in kwargs.items():
            self.contents += [colour]*ball_count

    # Create a method to select N balls from the hat at random (without replacement)
    def draw(self, num_balls):
        # Create draw list which points to contents
        draw_contents = self.contents

        # Ensure number of balls to draw is not greater than balls in hat
        if num_balls > len(draw_contents):
            num_balls = len(draw_contents)

        # Create an empty list to keep track of the balls selected
        selection = list()

        # Create counter variable to keep track of how many balls left to select
        balls_remaining = num_balls
        while balls_remaining > 0:
            # Select ball at random using the random.choice() function
            ball = random.choice(draw_contents)

            # Append the selected ball to the selection list
            selection.append(ball)

            # Remove the selected ball from the contents list
            draw_contents.remove(ball)

            # Decrease counter
            balls_remaining -= 1

        return selection
    
    # Getter for hat contents
    def get_contents(self):
        return self.contents

    # Define the string output when using print()
    def __str__(self):
        return str(self.contents)

# Function which runs N experiments to find the simulated probability of drawing a given
# combination of balls from a hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Function to check if expected balls are in drawn balls
    def is_drawn(expected, drawn):
        # Create a copy of drawn list to remove balls once checked
        drawn_copy = drawn.copy()
        for ball in expected:
            # If expected ball is in the drawn list, remove it from the drawn list
            if ball in drawn_copy:
                drawn_copy.remove(ball)
            else:
                # Return false if the expected ball is not in the drawn list
                return False
        return True

    # Convert expected_balls dicitonary to a list
    expected_list = list()
    for colour, ball_count in expected_balls.items():
        expected_list += [colour]*ball_count

    # Sort list to compare with sorted draw list
    expected_list.sort()

    # Create experiment desired outcomes variable M
    # and number of experiments N
    M = 0
    N = num_experiments

    # Create counter variable to track remaining experiments
    experiments_remaining = N
    while experiments_remaining > 0:
        # Create copy of hat object to perform experiments
        hat_experiment = deepcopy(hat)
        
        # Perform draw method to get balls drawn at random from the hat
        draw_list = hat_experiment.draw(num_balls_drawn)

        # Sort draw list to compare with expected list
        draw_list.sort()

        # If draw outcome is same as expected outcome, increment desired 
        # outcome variable - M
        if is_drawn(expected_list, draw_list):
            M += 1

        # Decrease experiments_remaining counter
        experiments_remaining -= 1
        
    # Calculate experimental probability of expected outcome
    experimental_probability = round(float(M/N), 2)

    return experimental_probability

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
actual = probability
expected = 1.0

print(f'Expected: {expected}')
print(f'  Actual: {actual}')

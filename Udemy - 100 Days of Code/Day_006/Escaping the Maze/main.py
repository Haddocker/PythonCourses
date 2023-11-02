# https://reeborg.ca/
# Maze:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Stopping the infinite loop.
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
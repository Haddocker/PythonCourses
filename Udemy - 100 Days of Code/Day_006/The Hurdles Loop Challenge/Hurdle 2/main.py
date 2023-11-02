# https://reeborg.ca/
# Hurdle 2:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1

# or:
# while not at_goal():
#     jump()
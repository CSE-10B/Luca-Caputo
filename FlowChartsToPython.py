print("Start TwentyPaces")
print("1. Take Twenty Paces")
print("2. Rotate Body 180 Degrees")
print("3. Aim the Target")
print("4. Take the shot")

print("Cooking Turkey")
print("1. Turn on the Oven")
ready_to_eat = False 

if ready_to_eat == False:
    print("2. Has 4 Hours passed OR has the oven reached 180 degrees?")
    print("3. If not, keep roasting turkey")

ready_to_eat = True
if ready_to_eat == True:
    print("4. Take turkey out of the oven")

print("Moving Robot")
print("1. Move the robot forward")
sensor_pressed = False 

if sensor_pressed == False:
    print("...Robot is moving...")

sensor_pressed = True
if sensor_pressed == True:
    print("2. Sensor Pressed! Cut powers to motor to stop")

print("Navigation Route")
print("1. Drive two miles down Liberty Avenue")
print("2. Turn left at 40th St.")
reached_bridge = False

if reached_bridge == False:
    print("...Action: Continue driving straight...")

reached_bridge = True
if reached_bridge == True:
    print("3. Turn right onto Foster St.")

print("4. Take first left turn")
print("5. Continue until you see the National Robotics Consortium")

print("Cross The Curb")
print("1. Wait until arriving at the curb then stop")
print("2. Look left, right, then left again")
is_it_clear = False

if is_it_clear == False:
    print("3. Wait for cars to pass")

is_it_clear = True
if is_it_clear == True:
     print("4. Walk across the street briskly")

print("How to Read a Flow Chart")
print("1. Locate the oval at the top of the page")
print("Follow the oval onto the next shape")

is_the_shape_a_rectangle = False
if is_the_shape_a_rectangle == False:
    print("Is it a diamond?")
is_the_shape_a_diamond = False
if is_the_shape_a_diamond == False:
    print("is the shape an end oval?")
is_the_end_shape_an_oval = False
if is_the_end_shape_an_oval == False:
    print("Ignore the unknown shape, proceed back at the beginning")
is_the_shape_correct = True
if is_the_shape_correct == True:
    print("Perform the action in the shape")

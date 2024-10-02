# Lunar Lander: AI-controlled play

# Instructions:
#   Land the rocket on the platform within a distance of plus/minus 20, 
#   with a horizontal and vertical speed less than 20
#
# Controlling the rocket:
#    arrows  : Turn booster rockets on and off
#    r       : Restart game
#    q / ESC : Quit

import csv
with open("iterative solution data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Test#","Success?","Fuel"])
    testNumber = 0

from LunarLander import *

env = LunarLander()
env.reset()
exit_program = False
while not exit_program:
    env.render()
    (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 

    # Process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                exit_program = True
            if event.key == pygame.K_UP:
                boost = True
            if event.key == pygame.K_DOWN:
                boost = False
            if event.key == pygame.K_RIGHT:
                left = False if right else True
                right = False
            if event.key == pygame.K_LEFT:
                right = False if left else True
                left = False
            if event.key == pygame.K_r:
                boost = False        
                left = False
                right = False
                env.reset()

    # INSERT YOUR CODE HERE
    #
    # Implement a Lunar Lander AI 
    # Control the rocket by writing a list of if-statements that control the 
    # three rockets on the lander 
    #
    # The information you have available are x, y, xspeed, and yspeed
    # 
    # You control the rockets by setting the variables boost, left, and right
    # to either True or false
    #
    # Example, to get you started. If the rocket is close to the ground, turn
    # on the main booster

    


    # Når raketten flyver fra venstre til højre bliver xspeed større
    # Når raketten flyver fra højre mod venstre bliver xspeed mindre

    # Når rakettern flyver opad bliver yspeed mindre
    # Når raketten falder bliver yspeed større


    if x < 0:
        left = True
        right = False

        if xspeed > 20:
            right = True
            left = False
    
    if x > 0:
        right = True
        left = False

        if xspeed < -20:
            right = False
            left = True


    if y < 50:
        if yspeed > 15:
            boost = True
        else:
            boost = False
    elif 40 < y < 200:
        if yspeed > 30:
            boost = True
        else:
            boost = False

    else:
        boost = False

    
    # Modify and add more if-statements to make the rocket land safely
    # END OF YOUR CODE

    #log data
    if y<=0:
        testNumber += 1
        testData = [testNumber, env.won, env.rocket.fuel]
        with open("iterative solution data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(testData)
        print(f"test: {testData[0]}, success?: {testData[1]}, fuel left: {testData[2]}, finalSpeed: {yspeed}")
        env.reset()

env.close()
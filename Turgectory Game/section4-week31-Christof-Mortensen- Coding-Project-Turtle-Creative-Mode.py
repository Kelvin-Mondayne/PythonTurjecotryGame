############################################
## Christof Mortensen
## christof.mortensen@icloud.com
## Intro to Python, Section 4
## Version 0.3
## 4/31/2021
## section4-week31-Christof-Mortensen-Coding-Project-Turtle-Creative-Mode.py
#
#

#############################################
#|  version History:                        |
#|__________________________________________|
#|version 0.1  : Needs optomisation so the program can run
#############################################
#|version 0.2  : Appers that program isn't running the part that
#|-------------- calculates and draws the Trajectory
#############################################
#|version 0.3  : Fixed Problem with while Y[length] > 0 and X[length] < 450:
#|-------------- and X = [0] Y = [0] so now 
#|-------------- while Y[length] > -10 and X[length] < 450:
#############################################
#|version 0.4  : Problem with python implementation of  
#|-------------- cosine and sine only so that only 45 degree
#|-------------- angles work so that there accuret 30 and 60 
#|-------------- degree are especially bad as they go strait
#|-------------- down or backwards
#############################################
#|version 1.0  : Added preclaculted table for sine and cosine
#|-------------- And ploshed the game.
#############################################



#############################################
## week 31
## Pull together what you've learned about loops, decision structures,
## and turtle to create your own creative turtle design of your choice.
## Next week in class, the teacher will show each set of code on the
## screen and demonstrate what happens when we run it. It will be similar to "show and tell."
##
## Ensure that the following details are included:
##
##    Rubric requirements
##    At least one loop
##    At least one decision structure (if/then, etc.)
##    Turtle
##
#
#

##############################################
#    1. What was your favorite coding project from this class this year?
#   This one i like it, it was fun
#   
#    2. What one thing would you change so that you could learn more from this class?
#   More time spent on classes
#   
#    3. What coding project was your least favorite?
#   the ones were we were learning about classes that was confusing
#   
#    4. Do you plan to take more coding classes (and if so, which ones)?
#   Yes I hope to take the next class on Java! 
#   
#   
#    5. What is one thing that you want to learn this summer?
#   Going to learn C#
#   


############################################
## Rules and Pricipules
## Have others check your spelling
## dont use magic numbers
## % is for constent EX: DefaltEx%15 
#
#


import turtle
import math
import random


def main():


    ##Prints the Title
    print("________________________________________________________________________________")
    print("__________O_____________________________________________________________________")
    print("________________________________________________________________________________")
    print("_______KK_____###_|D____A______o__#~~ _### /-\_|D___\/__GGG____A___M___M_EEEE__#")
    print("______KK_______|__|\___/_\_____|__#-  __|_ | |_|\___|__G______A_A__MM_MM_E_____#")
    print("_____##________|__| \_/   \____|__#__ __|_ \_/_| \__|__G__GG__A_A__MM_MM_EEEE__#")
    print("____##_______________________\_/_______________________G___G_AAAAA_M_M_M_E______")
    print("___##___________________________________________________GGG__A___A_M_M_M_EEEE__O")
    print("#######_________________________________________________________________________","\n","\n")
    print("Welcome to Christofs Trajectory Game!","\n","\n","Try to hit the red target using the cannon"
          ,"\n","use inclenation and power to hit the target","\n")




    #set debug to 1
    debug = 1

    #a while loop where it repets if debug is 1
    while debug == 1:

        #runs function TrutleDraw
        TurtleDraw()

        #sets debug to the input
        debug = input("Do you want to try again ? y/n??   ")

        #tells if y is inputed to debug and sets debug as 1
        if debug == 'y':
            debug = 1
            
            #resets turtle
            turtle.goto(0,0)
            turtle.width(0)
            turtle.clear()

            #tells if n is inputed to debug the it breaks the loop
        elif debug == 'n':
            debug = 0
            break
        else:
            #Prints error, sets debug to 1 ,and resets turtle
            print("Error \n    Charicter Not Recognised Please Try Again")
            debug = 1

            #resets turtle
            turtle.goto(0,0)
            turtle.width(0)
            turtle.clear()
    
                         # X is the simplest coordinate since gravity dosent exist
def CoordinateX(t,V,Ang):# t is time, V is volocity, and Ang is Angle
    
    # calculates Volocity for X coordinate
    Vx = V * CPT(Ang)

    # calculates X coordinate
    X = Vx * t

    # returns X coordinate
    return X

                        # Y is more complex to calculate but not by much
def CoordinateY(t,V,Ang):# t is time, V is volocity, and Ang is Angle
    # defines gravity
    g = 9.8
    
    # calculates Volocity for Y coordinate
    Vy = V * SPT(Ang)

    # calculates Y coordinate
    Y = (Vy * t) - (0.5 * g * (t * t))

    # returns Y coordinate
    return Y



def TurtleDraw():

    #X ,Y coordinate ,and time 
    X = [0]
    Y = [0]
    t = 0
    count = 1
    length = 0
    
    #Angle Input and prossesing
    Ang = int(round(float(input("please input the angle (in degrees) you want your cannon to shoot at: ")),0))

    

    #Velocity Input
    V = float(input("please input the speed (in pixels per second) you want your cannon ball to shoot at: "))

    #Error Correction
    
        #Error for to big or small of an angle
    if Ang > 89 or Ang < 1:

        #Prints Error
        print("\n","Error: Angle not inside accepted range","\n    Please try an angle between 0 and 90 degrees","\n")

        #calls TurtleDraw Function
        TurtleDraw()


        
        #Error for if volocity is greater then map size
    if V >= 200:

        #Prints Error
        print("\n","Error: Volocity is greater then map size","\n     try a lower volocity","\n")

        #calls TurtleDraw Function
        TurtleDraw()
    
    
    
    
    
    
    
    #Draws background and target We dont look at this just pretend it not there

    #Draws Background
    turtle.speed(0)
    turtle.color('green')
    turtle.hideturtle()
    turtle.goto(0,-10)
    turtle.goto(450,-10)
    turtle.goto(450,-50)
    turtle.goto(-50,-50)
    turtle.goto(-50,0)
    turtle.goto(0, 0)
    
    #Draws Target
    turtle.penup()
    turtle.pencolor('red')
    turtle.width(3)
    turtle.goto(450,-10)
    turtle.pendown()
    turtle.goto(440,-10)

    #Draws Cannon barrel
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.color('black')
    turtle.degrees()
    turtle.goto(6,5)

    #Draws Cannon Base
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.goto(4,0)
    turtle.goto(-4,0)
    
    #Draws Trajectory of shot
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.width(2)
    turtle.pencolor('orange')

    #A while loop that claculates a list of the cordinents
    while Y[length] > -10 and X[length] < 450:
        #appends X and Y functions into lists
        X.append(CoordinateX(t,V,Ang))
        Y.append(CoordinateY(t,V,Ang))
        #Debug Info gives you cordinents lists
        #print("Debug Info","\n X info",round(X[length],2),"\n Y info",round(Y[length],2),"\n t info",round(t,2))
        t = t + 0.01
        
        #Finds length of X and Y list since there the same lenght
        length = len(X) - 1
    
    
    # Draws parabolic arc
    for _ in range(0,length):
        turtle.goto(X[count],Y[count])

        count = count + 1

    #Determins if youv'e hit the target or not
    if X[length] >= 440 and  X[length] <= 450:
        print("You Win!!! :D","\n","Good Job!")


        #Draws explotion
        turtle.penup
        turtle.color('red','orange')
        turtle.begin_fill()
        turtle.goto(445,-10)
        turtle.pendown
        turtle.goto(440,-10)
        turtle.goto(435,0)
        turtle.goto(440,-2)
        turtle.goto(445,8)
        turtle.goto(450,-2)
        turtle.goto(455,0)
        turtle.goto(450,-10)
        turtle.end_fill()
        
        
        
    else:
        #loose print out
        print("You loose!!! >:(","\n","To bad, better luck next time!")




             
def CPT(Ang):

    #converts from deg to rad and usses the python cosine funtion
    return math.cos(Ang/(180/math.pi))
    


             
def SPT(Ang):

    #converts from deg to rad and usses the python sine funtion
    return math.sin(Ang/(180/math.pi))

    
main()



























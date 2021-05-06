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
    Ang = float(input("please input the angle (in degrees) you want your cannon to shoot at: "))

    

    #Velocity Input
    V = float(input("please input the speed (in pixels per second) you want your cannon ball to shoot at: "))


    #Time Resolution
    TRes = float(input("input the time resolution smaller is higher resolutuion but takes longer, \n lower you may hit the target but not get the right screen \n 0.01 is around good resolution and speed"))

    
    #Error Correction
    
        #Error for to big or small of an angle
    if Ang > 89.99 or Ang < 0.01:

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
        t = t + TRes
        
        #Finds length of X and Y list since there the same lenght
        length = len(X) - 1
    SX = str(X[:])
    SY = str(Y[:])
    file001 = open("FlightDataFile.txt","a")
    file001.write("X cordinates: \n")
    file001.writelines(SX)
    file001.write("\n")
    file001.write("Y cordinates: \n")
    file001.writelines(SY)
    file001.write("\n")
    file001.close()

    
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
        print("You loose!!! >:(","\n","To bad, better luck next time!")




             #Cosine Precalculated Table
def CPT(Ang):#This is a work around for the cosin in the Imported Math


    return math.cos(Ang/(180/math.pi))


    #Cosine is a dictionary with the calculated values of each angle
    #Cosine = {1:0.9998477,2:0.9993908,3:0.9986295,4:0.9975641,5:0.9961947,6:0.9945219,7:0.9925462,8:0.9902681,
    #          9:0.9876883,10:0.9848078,11:0.9816272,12:0.9781476,13:0.9743701,14:0.9702957,15:0.9659258,16:0.9612617,
    #          17:0.9563048,18:0.9510565,19:0.9455186,20:0.9396926,21:0.9335804,22:0.9271839,23:0.9205049,24:0.9135455,
    #          25:0.9063078,26:0.898794,27:0.8910065,28:0.8829476,29:0.8746197,30:0.8660254,31:0.8571673,32:0.8480481,
    #          33:0.8386706,34:0.8290376,35:0.819152,36:0.809017,37:0.7986355,38:0.7880108,39:0.777146,40:0.7660444,
    #          41:0.7547096,42:0.7431448,43:0.7313537,44:0.7193398,45:0.7071068,46:0.6946584,47:0.6819984,48:0.6691306,
    #          49:0.656059,50:0.6427876,51:0.6293204,52:0.6156615,53:0.601815,54:0.5877853,55:0.5735764,56:0.5591929,
    #          57:0.544639,58:0.5299193,59:0.5150381,60:0.5,61:0.4848096,62:0.4694716,63:0.4539905,64:0.4383711,
    #          65:0.4226183,66:0.4067366,67:0.3907311,68:0.3746066,69:0.3583679,70:0.3420201,71:0.3255682,72:0.309017,
    #          73:0.2923717,74:0.2756374,75:0.258819,76:0.2419219,77:0.2249511,78:0.2079117,79:0.190809,80:0.1736482,
    #          81:0.1564345,82:0.1391731,83:0.1218693,84:0.1045285,85:0.0871557,86:0.0697565,87:0.052336,88:0.0348995,
    #          89:0.0174524}
    


    
    

             #Sine Precalculated Table
def SPT(Ang):#This is a work around for the sin in the Imported Math
        
        
    return math.sin(Ang/(180/math.pi))
        
        

    #Sine is a dictionary with the calculated values of each angle
    #Sine = {89:0.9998477,88:0.9993908,87:0.9986295,86:0.9975641,85:0.9961947,84:0.9945219,83:0.9925462,82:0.9902681,
    #          81:0.9876883,80:0.9848078,79:0.9816272,78:0.9781476,77:0.9743701,76:0.9702957,75:0.9659258,74:0.9612617,
    #          73:0.9563048,72:0.9510565,71:0.9455186,70:0.9396926,69:0.9335804,68:0.9271839,67:0.9205049,66:0.9135455,
    #          65:0.9063078,64:0.898794,63:0.8910065,62:0.8829476,61:0.8746197,60:0.8660254,59:0.8571673,58:0.8480481,
    #          57:0.8386706,56:0.8290376,55:0.819152,54:0.809017,53:0.7986355,52:0.7880108,51:0.777146,50:0.7660444,
    #          49:0.7547096,48:0.7431448,47:0.7313537,46:0.7193398,45:0.7071068,44:0.6946584,43:0.6819984,42:0.6691306,
    #          41:0.656059,40:0.6427876,39:0.6293204,38:0.6156615,37:0.601815,36:0.5877853,35:0.5735764,34:0.5591929,
    #          33:0.544639,32:0.5299193,31:0.5150381,30:0.5,29:0.4848096,28:0.4694716,27:0.4539905,26:0.4383711,
    #          25:0.4226183,24:0.4067366,23:0.3907311,22:0.3746066,21:0.3583679,20:0.3420201,19:0.3255682,18:0.309017,
    #          17:0.2923717,16:0.2756374,15:0.258819,14:0.2419219,13:0.2249511,12:0.2079117,11:0.190809,10:0.1736482,
    #          9:0.1564345,8:0.1391731,7:0.1218693,6:0.1045285,5:0.0871557,4:0.0697565,3:0.052336,2:0.0348995,
    #          1:0.0174524}


    

    
main()



























#Christopher Lebovitz
#CSC 412 Intro to AI
#Dr. Li


"""
Implement a performance-measuring environment simulator for the vacuum-cleaner
world and specified on page 38. Your implementation should be modular
so that the sensors, actuators, and environment characteristics (size, shape, dirt placement,
etc.) can be changed easily. (Note: for some choices of programming language and operating
system there are already implementations in the online code repository.)

The performance measure awards one point for each clean square at each time step,
over a “lifetime” of 1000 time steps.
• The “geography” of the environment is known a priori (Figure 2.2) but the dirt distribution
    and the initial location of the agent are not. Clean squares stay clean and sucking
    cleans the current square. The Left and Right actions move the agent left and right
    except when this would take the agent outside the environment, in which case the agent
    remains where it is.
• The only available actions are Left , Right, and Suck.
• The agent correctly perceives its location and whether that location contains dirt.

"""




## defining global variables to be used in more than one function
rooms = []
position = 5
pMeasure = 0

## function creates the rooms and populates them as clean and dirty
def createRoom():

    global rooms

    for x in range(10):
        ## set those rooms that have a remainder of 0 as clean
        if x%2 == 0:
            rooms.append('C')
        ## set the rooms that have a remainder of 1 as Dirty
        elif x%2 == 1:
            rooms.append('D')
        print(x)

#this function is used to tell the robot if it has hit a wall then go in the opposite the direction
def hitWall():

    global position 

    if (position >= 0) & (position <=9):
        return True   
    else:
        return False

    ## this frunction is the main driver of the program. it is used to tell the robot to clean or not go to the next room if already clean
    ## in here the hitwall() function is called to see if the robot has hit a wall and if it has then reverse direction 
def action():

    #this variable is used to keep track of when to switch direction
    Flag = True

    ## counter that is used to keep track of thye lifetime
    step = 0

    #use global variable that were defined eairler
    global rooms 
    global position 
    global pMeasure 

    ## while the lifetime is less than or equal to 1000 keep going
    while step <= 1000:

        ## use this variable to be able to output what room the vacuum has cleaned
        roomNum = position +1

      ## if the flag is set to true check to see if the room is clean or dirty  
        if Flag == True:

            ##if dirty set the clean the room, report the action to the user, increase performance measure, and move the vacuum to the next room
            if rooms[position] == 'D':

                rooms[position] = 'C'
                print("Action Performd: Cleaned Room:", roomNum)
                pMeasure = pMeasure + 1
                position= position + 1
                
            elif rooms[position] == 'C':
                print("No Action Performed in Room:", roomNum)
                position = position + 1

            ## check to see if moving forward will make the vacuum hit the vall, if so decrease position and roomNum, and set the flag to false
            if hitWall() == False:
                        Flag = False
                        position = position - 1
                        roomNum = roomNum - 1
        ## if flag is set to false reverse direcion
        if Flag == False:

            if rooms[position] == 'D':
                print("Action Performd: Cleaned Room:", roomNum)
                pMeasure = pMeasure + 1
                position= position - 1
            elif rooms[position] == 'C':
                 print("No Action Performed in Room:", roomNum)
                 position = position - 1

            if hitWall() == False:
                Flag = True
        ## increment step for each successfull run
        step = step+1


   
 
    
###Main###

createRoom()
print(*rooms)
action()
print()
/*
christopher lebovitz
9/14/2019
Dr. Li
CSC 412
Wed night

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

Room:
D C D C D

or something similar
* = the vacuum robot
C = clean spots in the room
D = dirty spots in the room

*/

#include <iostream>


using namespace std;


void createRoom(char a[], int numOfRooms);
void print(char a[], int numOfRooms);
bool inBound(char a[], int position);
int action(char a[], int position,int pMeasure);

int main()
{

	// set the how many rooms there are
	int const numOfRooms = 10;

	// create the array and use the number of rooms to set the array to that size
	char room[numOfRooms];

	// keep track of when doing performing the intendec action ie. sucking up dirt
	int performancemeasure = 0;
	

	//place the position of the robot
	int position = 5;
	
	cout << "The vacuum starts out in room 5" << endl;

	// create the room and populate every other room with dirt starting at the first index
	createRoom(room, numOfRooms);
	// print the array to show the user what rooms are dirty/clean
	print(room, numOfRooms);

	// this function is the that drives the robot vacuum 
	action(room, position, performancemeasure);
	
		
}


// print the room using a ranged based for loop
void print(char a[],int numOfRooms)
{

	for (int col = 0; col < numOfRooms; col++)
		{

		cout << a[col] << " ";

		}
	cout << endl;

}

// check to see if robot has hit a wall and if so return false
// to the action funtion to reverse the direction of the vacuum
bool inBound(char a[], int position)
{
	if ((position > 0) && (position <10))
	{
		return true;
	}
	else
	{
		return false;
	}
}

// run the action to drive the vacuum robot
int action(char a[], int position, int pMeasure)
{

	//use this value to act as a switch to reverse direction
	bool flag = true;

	//use this as a timer for the robot to 
	int step = 0;
	// if the position of the vacuuum is in bounds perform an action untill the end

	while ( step <= 100)
	{
		

		int roomNum = position + 1;

		if (flag == true)
		{

			if (a[position] == 'D')
			{
				a[position] = 'C';
				cout << "Action Performed: Cleaned room:" << roomNum << endl;;
				pMeasure++;
				position++;
				step++;
			}
			else if (a[position] == 'C')
			{
				cout << "No Action Performed in room:" << roomNum << endl;
				position++;
				step++;
			}
			if (inBound(a, position) == false)
					{
						flag = false;
						position--;
						roomNum--;
					}
		}

		// if the position of the vacuum has hit the boundry then reverse direction and go back
		if (flag == false)
		{
			int reverDir = position;

			if (a[position] == 'D')
			{
				a[position] = 'C';
				cout << "Action Performed: Cleaned room:" << roomNum << endl;;
				pMeasure++;
				position--;
				step++;
			}
			else if (a[position] == 'C')
			{
				cout << "No Action Performed in room:" << roomNum << endl;
				position--;
				step++;
			}
			if (inBound(a, position) == false)
			{
				flag = true;
			}
		}
	}
	return position;
}

// create the room and make the room dirty
void createRoom(char a[] ,int numOfRooms)
{
	for (int i = 0; i < numOfRooms; i++)
	{
		a[i] = 'C';
	}
	
	for (int i = 1; i < numOfRooms; i += 2)
	{
		a[i] = 'D';
	}
}


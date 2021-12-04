Dexter Hoang

A description of the class:

The purpose of the "Create" class is to let the user create a character and make it easier for the user to save features about their character in a neat and organized manner. The purpose of the "Customize" class is to let the user give their character appearances such as eye color or body type and lets the user save and display this info in a neat and organized manner as well. I decided to create these two classes because as an artist I love creating characters and thought that I should create classes/methods that helps me save information about my characters.


A description of each of the class and data variables:

self.__name - Assigned to the "name" argument. This will be the name of the character. Under the "__init__" method.

self.__gender - Assigned to the "gender" argument. This will be the gender of the character. Under the "__init__" method.

self.__set_height - This represents the character's height. This is set to 0 as a starting value. Under the "__init__" method.

self.__set_weight - This represents the character's weight. This is set to 0 as a starting value. Under the "__init__" method.

self.inches - Assigned to the number of inches added to the character's height. Under the "add_height" method.

self.lbs - Assigned to the number of lbs. added to the character's weight. Under the "gain" method.

self.hours - Assigned to the number of hrs of exercise done by character, which will be used to decrease the character's weight. Under the "exercise" method.

self.__eyecolor - Assigned to the character's eye color given by user. Under the "eye_color" method.

self.__haircolor - Assigned to the character's hair color given by user. Under the "hair_color" method.

self.__faceshape - Assigned to the character's face shape given by user. Under the "face_shape" method.

self.__bodybuild - Assigned to the character's body type given by user. Under the "body_build" method. 


A description of each of the methods:

For "Create" class:

def __init__: This method contains 4 arguments (self, name, gender, race). This sets the data attributes and sets the weight/height of the character to 0.

def add_height: This method contains 2 arguments (self, inches). This method converts the amount of inches given by user to ft. and adds that amount to the self.__set_height variable. 

def decrease_height: This method contains 2 arguments (self, inches). This method converts the amount of inches given by user to ft. and subtracts that amount to the self.__set_height variable. 

def get_height: This method contains 1 argument (self). This method returns a string containing the character's height to the user.

def gain: This method contains 2 arguments (self, lbs). This method adds the amount of lbs. given by user to the self.__set_weight variable.

def exercise: This method contains two arguments (self, hours). Based on the amount of hours given by the user, this method subtracts the amount of lbs lost based on the number of hrs. of exercise to the self.__set_weight variable. 

def get_weight: This method contains 1 argument (self). This method returns a string containing the character's weight to the user.

def display: This method contains 1 argument (self). This method returns a string containing all variables given bu the user. This contains the name, gender, height, weight, and race of the character.


For "Customize" class:

def __init__: This method contains 2 arguments (self, name). This sets the data attribute for the character's name.

def eye_color: This method contains 2 arguments (self, color). This sets the data attribute for the character's eye color.

def hair_color: This method contains 2 arguments (self, color). This sets the data attribute for the character's hair color.

def face_shape: This method contains 2 arguments (self, color). This sets the data attribute for the character's face shape.

def body_build: This method contains 2 arguments (self, color). This sets the data attribute for the character's body build. 


Demo Program Documentation:

For my demo program, I will be creating myself using both of my classes. With my "Create" class, I gave the name, gender, and race of myself. I then used the "add_height" method to give myself the appropriate height and the "gain" method to give myself the appropriate weight. I then used the "display" method to show all the variables I gave to the character(myself). Then with my "Customize" class I used the "eye_color", "hair_color", "face_shape", and "body_build" methods to give the character same features as me. Finally I used the "display" method to show all the customizations I gave to the character. 

Instructions on how to run the demo program:

To run this demo program you must have Python3 installed. You can either use Visual Studio Code to load and run the file, or you can use terminal and inside the directory containing the file, type in "python3 custom_class.py". This should run the file and return a string containing the character Dexter and his characteristics.  


















#Dexter Hoang
#Assignment 10.1: Your Own Class
#Create a script that includes your implementation of a custom class that is based on a real-world object.


#The class I will be implementing is "Create Your Own Character" " 
#This class will be creating the general foundation of character
class Create:
    def __init__(self, name, gender, race):
        #Create data attributes 
        self.__name = name
        self.__gender = gender
        self.__race = race
        #Setting height and weight for later use
        self.__set_height = 0
        self.__set_weight = 0

    #This method will add height to the character's height
    def add_height(self, inches):
        self.inches = inches
        #Converting inches to ft
        convert_inches = self.inches / 12 

        #Implementing "my_round" method I created from previous assignment to round the number  when converting inches to ft
        shift_x = (convert_inches * (10)**1)
        answer = int(shift_x)
        remainder = (shift_x - int(shift_x))
        if remainder >= 0.5:
            answer += 1
        else:
            answer  
        backshift_x = (answer / (10)**1)
        #Adding converted height to character's height
        self.__set_height += backshift_x
    
    #This method will decrease the character's height
    def decrease_height(self, inches):
        self.inches = inches
        #Converting inches to ft
        convert_inches = self.inches / 12 

        #Rounding the converted inches to the first decimal point
        shift_x = (convert_inches * (10)**1)
        answer = int(shift_x)
        remainder = (shift_x - int(shift_x))
        if remainder >= 0.5:
            answer += 1
        else:
            answer  
        backshift_x = (answer / (10)**1)
        #Adding converted height to character's height
        self.__set_height -= backshift_x

    #This method will show the character's height
    def get_height(self):
        #Returning current height of character
        return f"{self.__name}'s current height is {self.__set_height} ft."

    #This method will add weight to the character's weight
    def gain(self, lbs):
        self.lbs = lbs
        #Adding lbs to character
        self.__set_weight += lbs

    #This method will decrease the character's weight based on hrs of exercise
    def exercise(self, hours):
        self.hours = hours
        #Since exercising for an hour can lose about the average of 6 lbs, I decided to create a function for finding how much lbs would be lost based on the nunber of hrs of exerise"
        lbs_lost = hours * 6
        #Subtracting current weight of character by lbs lost
        self.__set_weight -= lbs_lost

    #This method will show the character's weight
    def get_weight(self):
        #Returning current weight of charactere
        return f"{self.__name} currently weighs {self.__set_weight} lbs."

    #This method will display all variables about the character
    def display(self):
        return f"Character: {self.__name}\nGender: {self.__gender}\nRace: {self.__race}\nHeight: {self.__set_height} ft.\nWeight: {self.__set_weight} lbs."

#This class will be for customizing appearance of character
class Customize:
    def __init__(self, name):
        self.__name = name
    #All these methods below will let the user set the appearance for different things for the character
    def eye_color(self, color):
        self.__eyecolor = color
    def hair_color(self, color):
        self.__haircolor = color
    def face_shape(self, shape):
        self.__faceshape = shape
    def body_build(self, build):
        self.__bodybuild = build
    #This method is for displaying all the customizations set by user
    def display(self):
        return f"Character: {self.__name}\nEye Color: {self.__eyecolor}\nHair Color: {self.__haircolor}\nFace Shape: {self.__faceshape}\nBody Type: {self.__bodybuild}"
    
    


def main():
    x = Create("Dexter", "Male", "Asian")
    (x.gain(135))
    (x.add_height(67))
    print(x.display())

    y = Customize("Dexter")
    y.eye_color("Blue")
    y.hair_color("Black")
    y.body_build("Average")
    y.face_shape("Diamond")
    print(y.display())
   

if  __name__ == "__main__":
    main()

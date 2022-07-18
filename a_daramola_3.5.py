#Akinola Daramola Jr
#Programming Exercise 3.5
#Due Date: 6/19/22


"""Mass and Weight
Scientists measure an object’s mass in kilograms and its weight in newtons.
If you know the amount of mass of an object in kilograms, you can calculate its weight in newtons with the following formula:
 
w e i g h t = m a s s × 9.8
 
Write a program that asks the user to enter an object’s mass, then calculates its weight.
If the object weighs more than 500 newtons, display a message indicating that it is too heavy.
If the object weighs less than 100 newtons, display a message indicating that it is too light.
"""


#Initializing value of mass
mass = 0.0

#Declaring value of mass
mass =  float(input("Enter mass of object: "))

#Declaring value of weight in newtons
weight = mass * 9.8

#Declaring value of newton parameters
newtons_100 = 100
newtons_500 = 500

#Output
print(f"mass: {mass:.2f}kg")
print(f"weight: {weight:.2f}lb")

#Conditional statement
if weight < newtons_100:
    print("Object weight is too light.")
elif weight > newtons_500:
    print("Object weight is too heavy.")
else:
    print('Object weight is just right.')








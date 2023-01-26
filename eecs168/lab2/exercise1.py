'''
Author: Srihari Meyoor
KUID: 3094412
Date: blah thursday
Lab: lab 02
Last modified: idk
Purpose: weather shit
'''


speed = int(input("Input a wind speed (m/s): "))
if speed > 69:
  print("A wind speed of " + str(speed) + "m/s is a Category 5 hurricane.")
elif speed < 70 and speed > 57:
  print("A wind speed of " + str(speed) + "m/s is a Category 4 hurricane.")
elif speed < 58 and speed > 49:
  print("A wind speed of " + str(speed) + "m/s is a Category 3 hurricane.")
elif speed < 50 and speed > 42:
  print("A wind speed of " + str(speed) + "m/s is a Category 2 hurricane.")
elif speed < 43 and speed > 32:
  print("A wind speed of " + str(speed) + "m/s is a Category 1 hurricane.")
elif speed < 33 and speed > 17:
  print("A wind speed of " + str(speed) + "m/s is a Tropical Storm")
elif speed < 18 and speed > -11:
  print("A wind speed of " + str(speed) + "m/s is a tropical depression")
else:
  print("Negative wind? Sorry, that's invalid.")
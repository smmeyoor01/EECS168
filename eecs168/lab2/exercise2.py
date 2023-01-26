numer = int(input("Enter a numerator: "))
denom = int(input("Enter a denominator: "))
answer = int(numer / denom)
if denom == 0:
    print("Sorry, you may not divide by zero. \n Exiting..")
print( str(numer) + " / " + str(denom) + " = " + str(answer) + " Remainder " + str(numer % denom) + " \n Exiting.." )
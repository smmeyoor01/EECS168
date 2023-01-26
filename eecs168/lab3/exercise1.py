st = input("Enter a string: ")
ask = input("Do you want case-sensitive match?: ")
sequence = input("Enter a sequence to count: ")

if ask == 'n' or ask == 'N':
    total = st.count(sequence.upper()) + st.count(sequence.lower())

else:
    total = st.count(sequence)

print("In the string " + str(st) + " the sequence " +  "\'" + str(sequence)  + "\' occurs " + str(total) + " time(s)")

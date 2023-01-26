file1 = input("Enter name of first data file: ")
input_file1 = open(file1, "r")

file2 = input("Enter name of second data file: ")
input_file2 = open(file2, "r")
num1 = []
num2 = []
for line in input_file1:
    num1.append(int(line))

for line in input_file2:
    num2.append(int(line))











def sum(order):
    sum = 0
    for i in order:
        sum += i
    return sum

def big_sum(num1, num2):
    if (sum(num1) > sum(num2)):
        print("The first list has the larger sum of " + str(sum(num1)))
    elif(sum(num1) == sum(num2)):
        print('The lists have an equal sum of ' + str(sum(num1)))
    else:
        print('The second lsit has the large sum of ' + str(sum(num2)))

def avg(order):
    return (sum(order) / len(order))

def big_avg(num1, num2):
    if (avg(num1) > avg(num2)):
        print("The first list has the large average of " + str(avg(num1)))
    elif(avg(num1) == avg(num2)):
        print('The lists have an equal average of ' + str(avg(num1)))
    else:
        print('The second lsit has the large average of ' + str(avg(num2)))

def compare(num1, num2):
    for i in num1:
        count = 0
        if i in num2:
            count+= 1
    return count

def isPalindrome(num1, num2):
    if num1[::-1] == num2:
        print("The lists are palindromes")
    else: print("The lists are not palindromes")







print('List Statistics:')
big_sum(num1, num2)
big_avg(num1, num2)
print('Count of the values that appear in both lists: ' + str(compare(num1, num2)))
isPalindrome(num1, num2)

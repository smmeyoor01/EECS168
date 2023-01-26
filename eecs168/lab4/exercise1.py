shop = []
while(True):
    print("Welcome to your shopping list \n 1) Add Item \n 2) Check off item \n 3) Print list \n 4) Exit")
    answer = input("Enter a choice: ")
   
    if answer == '1':
        add = input('What will you add to the list?: ')
        shop.append(add)
    

    elif answer == '2':
        subtract = int(input("Which item would you like to check off?: "))
        
        dashes = ''
       
        for i in range(1, len(shop[subtract - 1])):
            dashes += '-'
        
        shop[subtract - 1] = shop[subtract-1][0] + dashes + shop[subtract-1][-1]
    
    elif answer == '3':
        print('Here is your list:')
        for i in range(len(shop)):
            print(str(i+1) + ") " + shop[i])
    
    elif answer == '4':
        print('Goodbye!')
        break
    print('')

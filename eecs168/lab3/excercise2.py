print("Guess the secret phrase!")
secret_phrase = "bringcoffee"
count1 = 0
while(True):
    guess = input("Guess: ")
    count1 += 1
    if len(guess) < len(secret_phrase):
        print("Too few characters")
    
    elif len(guess) > len(secret_phrase):
        print("Too many characters")
    
    elif len(guess) == len(secret_phrase) and guess != secret_phrase:
        for i in range(len(secret_phrase)):
            if guess[i] != secret_phrase[i]:
                break
        print(str(i))
    elif len(guess) == len(secret_phrase) and guess == secret_phrase:
        print("Correct!") 
        print("Number of guesses: " + str(count1))
        break
# This program will try to guess the word the user is thinking of within 16 guesses.

def compPick(lower,higher,count):
    
    with open('usa.txt') as f:
        lines = f.readlines()

    index = round((higher+lower)/2) # Finds the number inbetween the two indexes
    guess = lines[round(index)] # Index number for the guess in the text file

    if count == 16:
        print("Your word is: "+ guess.upper() + "It took 16 trys to guess your word.")
        quit()
    else:
        print("Guess #"+ str(count) + ": " + guess.upper())
        answer = input("Is this your word?(y/n):")
        if answer == "y":
            print("Your word is: " + guess.upper() + "It took " + str(count) + " trys to guess your word.")
            quit()
    
    print("Does your word come before or after " + guess.upper())
    string = input("(b/a):")
    
    if string == "a":
        lower = index
        count += 1
        compPick(lower,higher,count)
        
    elif string == "b":
        higher = index
        count += 1
        compPick(lower,higher,count)
        
def WordsInDictionary():

    file = open("usa.txt", "r")
    data = file.read()
    words = data.split()
    num = len(words)

    return num

def main():
    
    num = WordsInDictionary()
    lower = 0
    higher = num
    count = 1
    compPick(lower,higher,count)
    
main()
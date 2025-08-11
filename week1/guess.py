#guessing game 
def guessNumber():
    guess= int(input("Enter guess number: "))
    return guess #send data back to the function 

def main():
    guess= guessNumber() #we can reuse guess variable since it exists on guessNumber only
    if guess== 12:
        print("Correct!")
    else:
        print("incorrect!")

main()#call main function

    





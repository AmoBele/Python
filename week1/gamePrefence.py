def main():
    level= input("You prefer a hard or easy game ")
    if not(level =="hard" or level=="easy"):# if user does not enter hard or simple this statement will be true
        print("Enter a valid level! ")
        return #terminate 
        
    player= input("Player preference multi or single ")
    if not(player== "multi" or player== "single"):
        print("Enter a valid player selection!")
        return
    
    #game selection
    if level=="hard" and player== "multi":
        difficulty("EA Sport Fifa")
    elif level=="hard" and player== "single":
        difficulty("Escape")

    elif level=="easy" and player== "multi":
        difficulty("mini Milatia")
    elif level=="easy" and player== "single":
        difficulty("Candy Crush")
    
 

def difficulty(game):
    print("I think you would love,",game)

main()
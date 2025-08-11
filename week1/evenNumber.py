def evenNumber(n):
     return n % 2 == 0

def main():
    try:
       score =int(input("Enter a number: "))
       if evenNumber(score):
        print(f"{score} Even number")
       else:
        print(f"{score}Odd number")

    except ValueError:
       print("Please enter a valid integer")

    finally:
       print("Operation complete!")

main()

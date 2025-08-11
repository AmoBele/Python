#prompt the user to enter 
x = input("Enter you name ")

print("Hello, "+x)# string concatenation +
#method that removes whitespace from a string 
print("Hello,",x.strip())
"""
e.g Enter your name            amo
the method strip comes in handy to remove the space in between 
"""

#method used to capitalize user input
print("Hello,",x.capitalize())
'''
the limitation of using capitalize is it only capitalize first letter of first word
'''

#method title() can address the limitation on capitalize
print("Hello,",x.title())
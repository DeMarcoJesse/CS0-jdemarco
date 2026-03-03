"""
    StdIO Lab
    ASCII Art - using literals and variables

    Updated By: <Jesse>
    Date: ... 02/05/2026

    This program produces an ASCII art on the console.

    Algorithm steps:
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""

print("Welcome to ASCII Art Program...\n")

name = input("Enter your name: ")
# FIXME4: greet the name using the variable as the following output
# must output: Nice meeting you, <name>!
print(f"Nice meeting you, {name}!")

# prompt user to enter the semester and store the value into semester variable using input function
semester = input("Enter the semester: ")
print(f"This is the {semester} semester.")

# FIXME5: prompt user to enter the year and store the value into year variable using input function
# FIXME6: print the year using the variable as the following output
# must output: This is <year> year.
year = input("Enter the year: ")
print(f"The year is {year}")
print("Hope you like my ASCII art...\n\n")

line1: str = "  |\\_/|   **********************    (\\_/)"
print(line1)
line2: str = "  |O .O|      ***************      |^ _o|"
print(line2)
line3: str = "  (>.< )*       *********          d(8.8)b" \

print(line3)
line4: str = "   W .W           *****              W . W"
print(line4)
line5: str = "  8+++++++++++++++++++++++++++++++++++++++++++8"
print(line5)
# FIXME9: use variable to print the fourth line
# FIXME10: use variable to print the fifth line
# Note: You can add more lines or print more ASCII arts of your choice if you'd like...

print("\nGood bye...  \n")

print(" (\_/)")

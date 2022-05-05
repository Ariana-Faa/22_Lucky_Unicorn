# Funtions go here


# Main routine goes here

error = "Please enter a whole number between 1 and 10"

valid = False
while not valid:
    response = input(input("How much would you like to play with?"))

    if 0 < response <= 10:
        print("You have asked to play with ${}".format(response))

    else:
        print("error")

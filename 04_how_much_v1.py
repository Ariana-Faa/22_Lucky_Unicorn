# Funtions go here

# Main rountine goes here

error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        response = int(input("How much would you like to play with? "))

        # ask the question
        if 0 < response <= 10:
            print("You have asked to play with${}".format(response))

        # if the amount is too low / too high give...
        else:
            print(error)

    except ValueError:
        print(error)
# Print the ...

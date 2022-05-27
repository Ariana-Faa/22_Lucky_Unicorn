

# Funtion goes here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter yes or no")

show_instructions = yes_no("Have you played this game before?")
print("You chose {}".format(show_instructions))

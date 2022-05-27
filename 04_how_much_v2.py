# Funtions go here
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            response = int(input(question))

            # ask the question
            if low < response <= high:
                return response

            # if the amount is too low / too high give...
            else:
                print(error)

        except ValueError:
            print(error)


# Main rountine goes here
how_much = num_check("How much would you like to play with?", 0, 10)

print("You will spending ${}".format(how_much))

# Print the ...

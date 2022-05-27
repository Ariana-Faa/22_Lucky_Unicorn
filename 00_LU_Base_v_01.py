import random

# Funtion goes here

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter yes or no")


def instructions():
    statement_generator("How to Play", "+")
    print()
    print("Choose a starting amount (minimum $1, maximum $10).")
    print()
    print("Then press <enter> to  play. You will get either a horse, a zebra a donkey or a unicorn.")
    print()
    print("It costs a $1 per round. Depending on your prize you might win")
    print("some of the money back. Here's the payout amounts...")
    print("Unicorn: $5.00 (balance increases by $4)")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1)")
    print()
    print("Can you avoid the donkeys, get the unicorns and walk home with")
    print("the money??")
    print()
    print("Hint: to quit while you are ahead, type 'xxx' instead of")
    print("pressing <enter>")
    return ""


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


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine goes here...
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

played_before = yes_no("Have you played this game before?")

print()

if played_before == "no":
    instructions()

print()

statement_generator("Let's get Started...", "-")
print()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with?", 0, 10)

balance = how_much

rounds_played = 0

print()

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    print()

    chosen_num = random.randint(1,100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "|"
        balance += 4
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    # The token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is " "${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        #If balance is to low, exit the game and
        # Output a suitable message
        play_again = "xxx"
        print()
        print("Sorry you have run out of money")
    else:
        print()
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
statement_generator("Results", "=")
print()
print("Final balance $", balance)
print("Thank you for playing")

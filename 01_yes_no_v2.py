show_instructions = ""

while show_instructions != "xxx":
    show_instructions = input("Have you played this game before?").lower()

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("program continues")

    else:
        print('Please either "yes" or "no"')
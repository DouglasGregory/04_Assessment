# ah yeh g'day mate uh this is my uh unit checker. it works hard at making sure you
# enter what should be entered.
def unit_checker(question):
    while True:
        response = input(question).lower()

        if response == "grams" or response == "g":
            return "grams"
        elif response == "kilograms" or response == "kg":
            return "kilograms"
        elif response == "millilitres" or response == "mL":
            return "millilitres"
        elif response == "litres" or response == "litres":
            return "litres"
        elif response == "":
            return "<blank>"
        elif response == "xxx":
            return "Next Question"
        else:
            print("Yeah, uh, I think it only accepts the following:\n"
                  " - grams or g\n"
                  " - kilograms or kg\n"
                   " - millilitres or mL\n"
                  " - litres or L\n"
                  " - <blank> or BL\n"
                  "It miiiiiiight be best if you used those instead of\n"
                  "whatever you put in...     Just a thought")

while True:
    unit = unit_checker("What’s the unit?")
    print(f"you chose {unit}")
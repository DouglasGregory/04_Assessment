# Bring in pandas
import pandas


# functions go here

def num_check(question):
    while True:
        try:
            response = float(input(question))
            if 1 <= response <= 9999:
                return response
            elif response < 1:
                print("Yeah nah, you need to put a number in (That aint 0 buddy.)")
                continue

        except ValueError:
            print("Yeah, nah, that didn't work. Maybe check your response mate..?")


# Yes/No checker
def yes_no(question):
    to_check = ["yes", "no"]
    valid = False
    while not valid:
        response = input(question).lower()
        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print("Yeah, uh, I don't see a yes or a no.. \n")


# Formatting the currency
def currency(x):
    return f"${x:.2f}"


# Blanks = Error
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print("{}. \nPlease try again. \n".format(error))
        else:
            valid = True
    return response


# checking if all units are correct
def unit_checker(question):
    while True:
        response = input(question).lower()

        if response == "grams" or response == "g":
            print("You have selected 'Grams'")
            return "grams"
        elif response == "kilograms" or response == "kg":
            print("You have selected 'Kilograms'")
            return "kilograms"
        elif response == "millilitres" or response == "ml":
            print("You have selected 'Millilitres'")
            return "millilitres"
        elif response == "litres" or response == "L":
            print("You have selected 'Litres'")
            return "litres"
        elif response == "" or response == "blank":
            print("How do you even manage to put in a unit with 0 value! Nice job superstar!")
            return ""
        elif response == "END" or response == "end":
            print("You have gone to the next step.")
            return "Next Question"
        else:
            print("Yeah, it only works if you use these buddy!:\n"
                  " - grams or g\n"
                  " - kilograms or kg\n"
                  " - millilitres or mL\n"
                  " - litres or L\n"
                  " - <blank> or BL\n"
                  "It might be best if you used those instead of\n"
                  "whatever you put in egg head...    Just a thought")


# main routine goes here

# Print introduction
print("************** INTRODUCTION *****************\n\n\n"


      "WELCOME TO THE BLIMMIN CALCULATOR MATE!\n"
      "This thing is super easy to use if you are a toddler\n"
      "you need to make things like food or drinks. Instructions have been created to\n"
      "to show you how to use it. If you'd like to view the instructions, please answer\n"
      "the next question with a yes. If you'd like to give it a go without reading the\n"
      "the instructions, then simply say no to the following question. I hope you have a snazzy time using \n"
      "my calculator!\n\n\n"


      "************ READ INSTRUCTIONS? *************")

want_instructions = yes_no("Do you need to see the instructions? ")

# do users want instructions
if want_instructions == "yes":
    print('''\n
    ****** Instructions ******

    Cheers mate Thanks for using the calculator 

    HOW DO I USE THIS CALCULATOR???

    THE BLIMMIN CALCULATOR IS EASY AS PIE ALL YOU NEED TO DO IS JUST SAY YES OR NO TO INSTRUCTIONS IS THAT EASY!!!

    The calculator will calculate all the provided information and will give you the total amount you'd
    need to produce whatever it is you are making for the amount of persons you have entered.
    The calculator will also write the information to a text file so it can be shared with other people
    GOOD LUCK.


    **************************
    ''')

# making dictionaries
ingredient_name = []
ingredient_price = []
unit = []
required_amount = []
current_amount = []
creation_cost = []

# Get recipie name
recipe_name = not_blank("What's the name of your recipe?", "Yeah nah mate, can't leave this blank.")
print()

# How many people are eating (size)
serve = num_check("How many of your mates are you serving?")
print()

print("Please enter your ingredients. You can type 'END' to move onto the next step.\n\n")

# Get ingredients, unit, etc.
while True:

    # get ingredients

    get_ingredient = not_blank("Your ingredient is: ", "Yeah nah, ingredient not found"
                                                       "You sure it exists?")
    print()

    if get_ingredient == "END" and len(ingredient_name) >= 3:
        break
    elif get_ingredient == "END" and len(ingredient_name) < 3:
        print("Yeah, nah mate,You might need some more ingredients.")
        continue

    if get_ingredient == "end" and len(ingredient_name) >= 3:
        break
    elif get_ingredient == "end" and len(ingredient_name) < 3:
        print("Yeah, nah mate,You might need some more ingredients.")
        continue

    # check unit response
    unit_response = unit_checker("What number you need for this ingrediant? \n")

    # append thingy
    unit.append(unit_response)

    # Checking operations
    required = num_check("How much do you need mate? ")
    print()
    bought = num_check("How much did you Aquire through purchase: ")
    print()
    price_per_unit = num_check("How much of your hard earned cash did you use for it? $")
    print()

    unit_cost = ((price_per_unit / bought) * required)

    ingredient_name.append(get_ingredient)
    ingredient_price.append(price_per_unit)
    required_amount.append(required)
    current_amount.append(bought)
    creation_cost.append(unit_cost)

# Give goods c:
recipe_dict = {
    "Ingredient": ingredient_name,
    "Price": ingredient_price,
    "Unit": unit,
    "Required": required_amount,
    "Current": current_amount,
    "Cost": creation_cost
}

recipe_panda = pandas.DataFrame(recipe_dict)


# Total cost and cost per serve
total_cost = recipe_panda["Cost"].sum()
serving_cost = total_cost / serve

print('''\n
    **************************\n\n
Cheers for using my calculator!.\n
This was made to allow people to include multiple recipes and ingredients and drinks!. 


Your final costs have been summed up and can be found below:\n
    **************************\n\n\n
''')
print(recipe_panda)
print("Total Cost: ${:.2f}".format(total_cost))
print("Cost per Serving: ${:.2f}".format(serving_cost))


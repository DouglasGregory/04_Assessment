import pandas


# FUNCTIONS
# Ensures answer is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \n Please try again. \n".format(error))
            continue

        return response


# Number Checker (ensures valid number is inputted)
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# currency formatting
def currency(x):
    return f"${x:.2f}"


# OTHER CRAP
# loop to get component, quantity and price


# Set up dictionaries and lists
item_list = []
ingredient_list = []
amount_list = []
price_list = []
unit_list = []

recipe_dict = {
    "Item": item_list,
    "Ingredient": ingredient_list,
    "Amount": amount_list,
    "Unit": unit_list,
    "Price": price_list,
}

item_name = ""

while item_name.lower() != "xxx":

    print()
    # get name, quantity and item
    item_name = not_blank("Item name: ",
                          "The component name can't be blank.")

    if item_name.lower() == "xxx":
        break

    amount = num_check("Amount:", "The amount must be a whole number which is more than zero", int)

    price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

    # add item, quantity and price to lists
    item_list.append(item_name)
    amount_list.append(amount)
    price_list.append(price)

    recipe_frame = pandas.DataFrame(recipe_dict)
    recipe_frame = recipe_frame.set_index('Item')

    recipe_frame['Cost'] = recipe_frame['Amount'] * recipe_frame['Price']
    # Find sub-total
    recipe_sub = recipe_frame['Cost'].sum()
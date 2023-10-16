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

        print("Oi mate you got it wrong - bloody fix it. "
              "make it one of these mate: yes (y) / no (n). \n")


# main routine goes here
want_instructions = yes_no("Do you want to see the instructions? ")

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
to_units = 24
name_to_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * to_units} {name_to_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)

        # we want to do a conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered a 0, please enter a valid positive number")
        else:
            print("Dear user, you entered a negative number, its not valid for the program")
    except ValueError:
        print("Dear user, I have requested a number of days")


user_input = ""
while user_input != "exit":
    user_input = input("Hey dear user, enter number of days as a comma separated list and I will conv ert it to hours:\n")
    print(user_input)
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit} minutes"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])

        # we want to do a conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered a 0, please enter a valid positive number")
        else:
            print("Dear user, you entered a negative number, its not valid for the program")
    except ValueError:
        print("Dear user, I have requested a number of days")


user_input = ""
while user_input != "exit":
    user_input = input("Hey dear user, enter number of days and conversion unit!:\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()
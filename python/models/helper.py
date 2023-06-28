def days_to_unit_dictionary(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 3600} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 86400} {conversion_unit}"
    else:
        return "Unsupported unit"

# we have to pass it like a variable
def validate_and_execute_dictionary(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            my_var = days_to_unit_dictionary(user_input_number, days_and_unit_dictionary["unit"])
            print(my_var)
        elif user_input_number == 0:
            print("You entered a 0, please try a bigger number ♥")
        else:
            print("Error, the number can't be negative")
    except ValueError:
        print("your input is not a number, we can't calculate")

user_input_messages = "Enter the number of days and I will convert it to hours or exit for stop the program: \n"
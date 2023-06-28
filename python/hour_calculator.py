calculation_to_units = 24
name_of_unit = "hours"

# def days_to_unit(num_of_days):
#     print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

# days_to_unit(20)
# days_to_unit(30)
# days_to_unit(299)
# days_to_unit(98)

# using a input
def days_to_unit(num_of_days):
      return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
# we have to casting it, or we will have a repetitive number
# user_input = int(input("Enter the number of days and I will convert it to hours: \n"))

def validate():
    # user input is a digit? if yes is bigger than 0? all ok, if not we will show all the errors
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            my_var = days_to_unit(user_input_number)
            print(my_var)
        else:
            print("Error, the number can't be negative")
    else:
        print("your input is not a number, we can't calculate :(")
   

user_input = input("Enter the number of days and I will convert it to hours: \n")
validate()


# doing the part validation whit try and except

# def validate_and_execute():
#     try:
#         user_input_number = int(num_of_days_element)
#         if user_input_number > 0:
#             my_var = days_to_unit(user_input_number)
#             print(my_var)
#         elif user_input_number == 0:
#             print("You entered a 0, please try a bigger number ♥")
#         else:
#             print("Error, the number can't be negative")
#     except ValueError:
#         print("your input is not a number, we can't calculate")
#
#
#
# user_input_validate2 = ""
# while user_input_validate2 != "exit":
#     user_input_validate2: str = input("Enter the number of days and I will convert it to hours: \n")
#     # set for not duplicate numbers
#     for num_of_days_element in set(user_input_validate2.split()):
#         validate_and_execute()

# now we will use a dictionary
def days_to_unit_dictionary(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 3600} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 86400} {conversion_unit}"
    else:
        return "Unsupported unit"
def validate_and_execute_dictionary():
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

user_input_validate3 = ""
while user_input_validate3 != "exit":
    user_input_validate3: str = input("Enter the number of days and I will convert it to hours: \n")
    days_and_unit = user_input_validate3.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit)
    validate_and_execute_dictionary()


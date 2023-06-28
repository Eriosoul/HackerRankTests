from helper import validate_and_execute_dictionary, user_input_messages

user_input_validate3 = ""
while user_input_validate3 != "exit":
    user_input_validate3: str = input(user_input_messages)
    days_and_unit = user_input_validate3.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute_dictionary(days_and_unit_dictionary)

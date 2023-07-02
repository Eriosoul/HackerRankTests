import datetime
import time

user_input = input("Enter your goal whit your deadline, separated by colon: \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.datetime.today()
time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"Time remaining for your goal : {goal} is {hours_till} hours")


# while True:
#     date = datetime.datetime.today()
#     time.sleep(1)
#     print(date)
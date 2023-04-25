from datetime import datetime

user_input = input("enter your goal with a deadline separeted by colon with format dd.mm.yyyy\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
dateline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y") #date format that method can read -> dd.mm.YYYY

#calculation -> how many from now to deadline
now = datetime.datetime.today()
time_till = dateline_date - now

print(f"Dear user! Time to {goal} is {time_till.days} days left until deadline")

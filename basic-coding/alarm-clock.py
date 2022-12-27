import ast
input_str = input()
input_list = ast.literal_eval(input_str)

day_of_the_week = input_list[0]
is_on_vacation = input_list[1]

weekend = [6,7]

def set_alarm(day_of_the_week, is_on_vacation):
    if is_on_vacation:
        if day_of_the_week not in weekend:
            alarm = "10:00"
        else:
            alarm = "off"
    else:
        if day_of_the_week in weekend:
            alarm = "10:00"
        if day_of_the_week not in weekend:
            alarm = "7:00"
    return alarm
print(set_alarm(day_of_the_week, is_on_vacation))
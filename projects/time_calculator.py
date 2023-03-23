def convert_12_to_24(time_12):
    # Extract hour, minute, and time of day
    hour = time_12.split()[0].split(':')[0]
    minute = time_12.split()[0].split(':')[1]
    am_pm = time_12.split()[1].lower()

    # Add 12 hours if pm
    if am_pm == 'pm' and int(hour) != 12:
        hour = str(int(hour) + 12)
    elif am_pm == 'am' and int(hour) == 12:
        hour = str(int(hour) - 12)

    # String concat to make 24 hour time
    time_24 = hour + ':' + minute

    return time_24

def convert_24_to_12(time_24):
    # Extract hour and minute
    hour = time_24.split(':')[0]
    minute = time_24.split(':')[1]

    # Subtract 12 hours if past 12pm
    if int(hour) > 12 and int(hour) < 24:
        hour = str(int(hour) - 12)
        am_pm = ' PM'
    elif int(hour) == 12:
        am_pm = ' PM'
    elif int(hour) == 24:
        hour = str(int(hour) - 12)
        am_pm = ' AM'
    elif int(hour) == 0:
        hour = str(int(hour) + 12)
        am_pm = ' AM'
    else:
        am_pm = ' AM'

    # String concat to get 12 hour time
    time_12 = hour + ':' + minute + am_pm

    return time_12

def add_time(start, duration, start_day=''):
    
    start_day = start_day.lower()

    # Convert start time to 24 hour time
    start_24 = convert_12_to_24(start)

    # Calculate the total minutes by adding start_time and duration minutes
    total_minutes = int(start_24.split(':')[1]) + int(duration.split(':')[1])
    # How many hours we will add to the hour value
    quotient_minutes = total_minutes // 60
    # Leftover minutes which will be our final minutes
    remainder_minutes = total_minutes % 60

    # Calculate the total hours in 24 hour time by adding start_time and duration hours
    total_hours = int(start_24.split(':')[0]) + int(duration.split(':')[0]) + quotient_minutes
    days = total_hours // 24
    remainder_hours = total_hours % 24

    # Add an extra zero if final hours is 1 digit
    final_hours = str(remainder_hours)
    if remainder_minutes < 10:
        final_minutes = '0' + str(remainder_minutes)
    else:
        final_minutes = str(remainder_minutes)

    # Format for 24 hour time
    final_time_24 = final_hours + ':' + final_minutes
    # Convert to 12 hour time
    final_time_12 = convert_24_to_12(final_time_24)

    # Calculate how many days have elapsed and format string 
    if days == 1:
        days_later = ' (next day)'
    elif days > 1:
        days_later = ' ' + '(' + str(days) + ' days later)'
    else:
        days_later = ''

    # If a day has been entered, find the new day
    if start_day != '':
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_index = days_of_week.index(start_day.lower())

        # Modulus of 7 to ensure we don't go out of range
        new_day_index = (day_index + days) % 7

        # Capitilize and format
        final_day = ', ' + days_of_week[new_day_index].capitalize()
    else:
        final_day = ''

    # Format the final new time
    new_time = final_time_12 + final_day + days_later

    return new_time

# print(add_time("11:59 PM", "24:05"))
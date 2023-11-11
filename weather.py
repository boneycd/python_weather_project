import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

#PASSED
def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    return date.strftime('%A %d %B %Y')
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass

#PASSED
def convert_f_to_c(temp_in_farenheit):    
    convertion = (float(temp_in_farenheit) -32)*float(5.00/9.00)
    return round(convertion,1)


    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass

#PASSED
def calculate_mean(weather_data):
    
    total = 0
    for num in weather_data:
        total += float(num)
    return total/ len(weather_data)

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    
#weather_data = ["51", "58", "59", "52", "52", "48", "47", "53"]
#mean_value = calculate_mean(weather_data)
#print(calculate_mean(weather_data))
    pass


def load_data_from_csv(csv_file):
    # with open(csv_file, newline='') as csvfile:
    #     csv_reader = csv.reader(csvfile)
    #     next(csv_reader)
    #     data = [row for row in csv_reader if row]

    # return data
   
    data = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row:
                data.append([row[0], int(row[1]), int(row[2])])
    return data
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

#PASSED
def find_min(weather_data):
    if not weather_data:
        return ()    
    min_val = min(weather_data)
    f_min_val = float(min_val)
    last_index = len(weather_data) - 1 - weather_data[::-1].index(min_val)
    return f_min_val, last_index
   
  
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass

    
 

#PASSED
def find_max(weather_data):
    if not weather_data:
        return ()    
    max_val = max(weather_data)
    f_max_val = float(max_val)
    last_index = len(weather_data) - 1 - weather_data[::-1].index(max_val)
    return f_max_val, last_index
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


def generate_summary(weather_data):
    summary = ""
    min_list = []
    max_list = []
    for mintemp in weather_data:
        min_list.append(mintemp[1])

    for maxtemp in weather_data:
        max_list.append(maxtemp[2])

        

    num_of_days = len(weather_data)
    for day in weather_data:
        #date = convert_date(day[0])

        high_temp = find_max(max_list)
        high_temp_day_pos = high_temp[1]
        high_temp_day = weather_data[high_temp_day_pos]
        high_date = convert_date(high_temp_day[0])

        low_temp = find_min(min_list)
        low_temp_day_pos = low_temp[1]
        low_temp_day = weather_data[low_temp_day_pos]
        low_date = convert_date(low_temp_day[0])

        f_high_temp = convert_f_to_c(high_temp[0])
        f_low_temp = convert_f_to_c(low_temp[0]) 
        average_low = calculate_mean(min_list)
        f_average_low = convert_f_to_c(average_low)
        average_high = calculate_mean(max_list)
        f_average_high = convert_f_to_c(average_high)
        
        #summary += f"On {date}, the high temperature is {high_temp}°C and the low temperature is {low_temp}°C.\n\n"

    summary += (
        f"{num_of_days} Day Overview\n  The lowest temperature will be {f_low_temp}°C, and will occur on {low_date}.\n  The highest temperature will be {f_high_temp}°C, and will occur on {high_date}.\n  The average low this week is {f_average_low}°C.\n  The average high this week is {f_average_high}°C.\n"
        )
    # print (min_list)
    # print (average_low)
    # print(f_average_low)

    # print(average_high)
                    
    return summary

        


    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    summary = ""
    for day in weather_data:
        date = convert_date(day[0])
        min_temp = convert_f_to_c(day[1])
        max_temp = convert_f_to_c(day[2])
        summary += f"---- {date} ----\n  Minimum Temperature: {min_temp}°C\n  Maximum Temperature: {max_temp}°C\n\n"
    return summary

    
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

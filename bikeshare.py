# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:58:35 2026

@author: Lisa
"""

import time
import pandas as pd
import numpy as np



city_data = { "Chicago": "chicago.csv",
              "New York City": "new_york_city.csv",
              "Washington": "washington.csv" }


""" For all functions available variables"""
allowed_months = ["January", "February", "March", "April", "May", "June"]
allowed_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

month_word_number = {"January": 1, "February": 2, "March": 3, "April" : 4, "May" : 5, "June" : 6}
month_number_word = dict([(value, key) for key, value in month_word_number.items()])

day_word_number = {"Monday" : 0, "Tuesday" : 1, "Wednesday" : 2, "Thursday" : 3, "Friday" : 4, "Saturday" : 5, "Sunday" : 6}
day_number_word = dict([(value, key) for key, value in day_word_number.items()])



def print_seperator():
    """ Prints a seperating line for better readability"""

    print("\n")    
    print('-'*40)
    print("\n") 
    return


def get_units_of_interest(time_unit, allowed_values):
    """
    If the user wants to filter the data by month resp. day the function asks the user which month(s) resp. day(s) he wants to look at.    
    Args:
        (str) time_unit - "month" or "day" depending on which time unit the user wants to filter for
        (list) allowed_values - allowed months resp. days of the week the user can filter for            
    Returns:
        (list) units_of_interest - list of months resp. days the user wants to filter for
    """
   
    # asks the user for how many months resp. days he would like to filter the data for
    
    print("\nThere is data available for the following {}s: {}".format(time_unit, allowed_values))  
    number = input("How many of these {}s would you like to look at? ".format(time_unit))
    number = number.strip()
    max_number = len(allowed_values)
    
    while True:     
        try:
            number = int(number)
            while number not in range(1, max_number + 1):
                print("Please enter a number between 1 and {}. If you enter {} you will not filter by {} at all.".format(str(max_number), str(max_number), time_unit))
                number = input("How many {}s would you like to look at? ".format(time_unit))
                number = number.strip()
                try:
                    number = int(number)
                except:
                    print("Please enter a numerical value.")
            break
        except:
            print("Please enter a number between 1 and {}. If you enter {} you will not filter by {} at all.".format(str(max_number), str(max_number), time_unit))
            number = input("How many {}s would you like to look at? ".format(time_unit))
            number = number.strip()
    
    
    # asks the user for which months resp. days he would like to filter the data for
    
    units_of_interest = []
    available_values = allowed_values.copy()
    
    if number == max_number:
         units_of_interest = allowed_values
         print("Then we will apply no filter on the {}".format(time_unit))
         return units_of_interest
    else:
        for i in range(1, number + 1):
            while True:
                unit_of_interest = input("\nWhich {}(s) would you like to look at? Please enter the {}. {}. ".format(time_unit, str(i), time_unit)) 
                unit_of_interest = unit_of_interest.strip().title()
                if unit_of_interest in available_values:
                    units_of_interest.append(unit_of_interest)
                    available_values.remove(unit_of_interest)
                    break
                else:
                    print("Please enter a valid response. You can choose from the following {}s: {}".format(time_unit, allowed_values))


        # sorts the input             
        if time_unit == "month":   
             units_of_interest_temp = sorted([month_word_number[month] for month in units_of_interest])
             units_of_interest = [month_number_word[month] for month in units_of_interest_temp]        
        else: 
             units_of_interest_temp = sorted([day_word_number[day] for day in units_of_interest])
             units_of_interest = [day_number_word[day] for day in units_of_interest_temp]
                
        print("\nThen we will look at data for the following {}(s): {}.".format(time_unit, units_of_interest))       
    
    return units_of_interest
                
 
    
def get_cities(allowed_cities):
    """
    If the user wants to look at data for more than one city the function asks the user which cities he wants to compare.    
    Args:
        (list) allowed_cities - allowed cities for which data is available            
    Returns:
        (list) cities - list of cities the user would like to compare
    """

    # asks the user for how many cities he would like to compare data for
    
    number = input("\nHow many cities would you like to look at? ")
    number = number.strip()
    max_number = len(allowed_cities)
    
    while True:
        try:
            number = int(number)
            while number not in range(1, max_number + 1):
                print("Please enter a number between 1 and {}. If you enter {} we will compare all {} cities.".format(str(max_number), str(max_number), str(max_number)))
                number = input("How many cities would you like to look at? ")
                number = number.strip()
                try:
                    number = int(number)
                except:
                    print("Please enter a numerical value.")
            break
        except:
            print("Please enter a number between 1 and {}. If you enter {} we will compare all {} cities.".format(str(max_number), str(max_number), str(max_number)))
            number = input("How many cities would you like to look at? ")


    # asks the user for which cities he would like to compare the data for

    cities = []

    if number == max_number:
        cities = allowed_cities
        print("Then we will compare data for all cities.")
        return cities
            
    else:
        for i in range(1, number + 1):
            while True:
                city = input("\nFor which cities would you like to compare the data? Please enter the {}. city. ".format(str(i))) 
                city = city.strip().title()
                if city in allowed_cities:
                    cities.append(city)
                    allowed_cities.remove(city)
                    break
                else:
                    print("Please enter a valid response. You can choose from the following cities: {}".format(allowed_cities))  
    
    print("\nThen we will compare data for the following cities: {}.".format(cities)) 
    
    return cities
     
           

def get_filters():
    """
    Asks user to specify a city, month(s), and day(s) to analyze.
    Returns:
        (str / list) city - name(s) of the city / cities to analyze
        (list) months - list of the months the user wants to look at - outputs a list with 'None' as the only value if there is no filter desired
        (list) days - list of the days the user wants to look at - outputs a list with 'None' as the only value if there is no filter desired
    """
    
    print("Hello! Let\'s explore some US bikeshare data!")
    
    
    # Get user input for city (Chicago, New York City, Washington). It is also possible to select more than one city to compare the data for the selected cities
    allowed_cities = ["Chicago", "New York City", "Washington"]
    city = input("\nWould you like to see data for Chicago, New York City, or Washington? If you would like to compare data for more than one city please enter 'several'. ")    
    city = city.strip().title()

    if city == "Several":
        city = get_cities(allowed_cities)
    elif city == "None":
        return None, None, None         
    else:
        while not city in allowed_cities:        
            print("Please enter a valid response.")
            city = input("Would you like to see data for Chicago, New York City, or Washington? If you would like to compare data for more than one city please enter 'several'. If you don't want to see any data at all please enter 'none'. " )
            city = city.strip().title()
            if city == "Several":
                city = get_cities(allowed_cities)
                break
            elif city == "None":
                return None, None, None
  
        
    # Get user input for the time period (month / day)
    filters = ["month", "day", "both", "not"]      
    filter_desired = input("\nWould you like to filter the data by month, day, both or not at all? (month / day / both / not) ")   
    filter_desired = filter_desired.strip().lower()
    while not filter_desired in filters:
        print("Please enter a valid response.")
        filter_desired = input("Would you like to filter the data by month, day, both or not at all? (month / day / both / not) ")
        filter_desired = filter_desired.strip().lower()

    # get user input for month 
    if filter_desired in ["month", "both"]:
        months_of_interest = get_units_of_interest("month", allowed_months)
    else:
        months_of_interest = ["None"]

    # get user input for day of week 
    if filter_desired in ["day", "both"]:
        days_of_interest = get_units_of_interest("day", allowed_days)
    else:
        days_of_interest = ["None"]  
        
    print_seperator()

    return city, months_of_interest, days_of_interest



def join_dfs(city_data, cities):
    """
    Joins the dateframes for the respective cities when the user wants to compare data for more than one city.
    Args:
        (dict) city_data - matches the cities with the corresponding file names
        (list) cities - list if cities the user wants to compare data for         
    Returns:
        (dateframe) df - Pandas DataFrame including data for the relevant cities; the city is marked in the new column "City"
    """
 
    print("\nMerging the dataframes for the relevant cities...\n")
    
    # loads the dataframes for all relevant cities, includes a new column indicating the respective city and merging the city data to the new overall data frame
    
    df = pd.DataFrame(columns = ["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type", "Gender", "Birth Year", "City"])
    
    if "Chicago" in cities:  
        df_chicago = pd.read_csv("I:/Users/Lisa/Udacity/Python/Chapter 8/Projekt/" + city_data["Chicago"])
        # df_chicago = pd.read_csv(city_data["Chicago"])
        df_chicago = df_chicago[["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type", "Gender", "Birth Year"]]
        df_chicago["Trip Duration"] = df_chicago["Trip Duration"].astype(float) 
        df_chicago["City"] = "Chicago"
        df = pd.merge(df, df_chicago, how = "outer")
    
    if "New York City" in cities:
        df_newyorkcity = pd.read_csv("I:/Users/Lisa/Udacity/Python/Chapter 8/Projekt/" + city_data["New York City"])
        # df_newyorkcity = pd.read_csv(city_data["New York City"])
        df_newyorkcity = df_newyorkcity[["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type", "Gender", "Birth Year"]]
        df_newyorkcity["Trip Duration"] = df_newyorkcity["Trip Duration"].astype(float)  
        df_newyorkcity["City"] = "New York City"   
        df = pd.merge(df, df_newyorkcity, how = "outer")

    if "Washington" in cities:
        df_washington = pd.read_csv("I:/Users/Lisa/Udacity/Python/Chapter 8/Projekt/" + city_data["Washington"])  
        # df_washington = pd.read_csv(city_data["Washington"])
        df_washington = df_washington[["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type"]]
        df_washington["City"] = "Washington"
        df = pd.merge(df, df_washington, how = "outer")

    return df



def load_data(city, months, days):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str / list) city - name(s) of the city / cities to analyze
        (list) month - list of the month(s) to filter by
        (list) day - list of the day(s) of week to filter by
    Returns:
        (dataframe) df - Pandas DataFrame containing city data filtered by month and day
    """
 
    start_time = time.time()
    print("Loading the relevant data... ")
 
    if isinstance(city, list):
        df = join_dfs(city_data, city)
    else:
        df = pd.read_csv(city_data[city])
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    
    df["Month_num"] = df["Start Time"].dt.month
    df["Month"] = df["Month_num"].replace(month_number_word) 
    
    df["Day of week"] = df["Start Time"].dt.day_name()
    
    
    if months != ["None"]:       
        df = df[df["Month"].isin(months)]
    
    if days != ["None"]:       
        df = df[df["Day of week"].isin(days)]     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print_seperator()  
 
    return df



def get_frequencies(count, unit = None, matching_dict1 = None, matching_dict2 = None):
    """
    Sorts the frequency counts to show data in a "natural" order (e. g. "Monday, Tuesday, Wednesday, ...", "January, Febraury, March, ...")
    Args:
        (pd.series) count - frequency count for a specific unit (months, days, ...)
        (dict) matching_dict - matches for months and days the text description ("January", "February", ...) with the respective number (1, 2, ...) for sorting purposes
    Returns:
        (tuple) values - tuples of the values in the "natural" order
        (tuple) counts - frequencies matching the values
    """
    
    tuples = [tuple((x, y)) for x, y in count.items()]
    
    if unit in ["month", "day"]:
        tuples_temp = sorted([tuple((matching_dict1[element[0]], element[1])) for element in tuples])
        tuples = [tuple((matching_dict2[element[0]], element[1])) for element in tuples_temp]        
    elif unit == "hour":   
        tuples = sorted(tuples) 
     
    values, counts = zip(*tuples)   
    
    return values, counts
    


def show_frequencies(df, unit):
    """
    Prints frequencies for the requested unit
    Args:
        (dataframe) df - Panday DataFrame with the city data
        (str) unit - unit of analysis that has to be displayed         
    """
    
    if unit == "Month":
        count = df["Month"].value_counts()
        values, counts = get_frequencies(count, "month", month_word_number, month_number_word)
        
        print("This is the number of rentals per month:")
        for i in range(0, len(values)):
            print(values[i], ": ", counts[i])
        print("\n\n")
    
    elif unit == "Day":
        count = df["Day of week"].value_counts()
        values, counts = get_frequencies(count, "day", day_word_number, day_number_word)
        
        print("This is the numbers of rentals per day:")
        for i in range(0, len(values)):
            print(values[i], ": ", counts[i])
        print("\n\n")
        
    elif unit == "Hour":
        count = df["Hour"].value_counts()
        values, counts = get_frequencies(count, "hour")
        
        print("This is the number of rentals per hour:")
        for i in range(0, len(values)):
            print(values[i], ": ", counts[i])
        print("\n\n")

    elif unit == "Start Station":
        count = df["Start Station"].value_counts()
        values, counts = get_frequencies(count)

        print("This is the number of rentals for the top 5 start stations:")
        for i in range(0, 5):
            print(values[i], ": ", counts[i])
        print("\n\n")
                
    elif unit == "End Station":
        count = df["End Station"].value_counts()
        values, counts = get_frequencies(count)

        print("This is the number of rentals for the top 5 end stations:")
        for i in range(0, 5):
            print(values[i], ": ", counts[i])
        print("\n\n")
    
    return
        
        

def time_stats_more_cities(df, cities, time_unit):
    """Displays statistics on the most frequent times of travel for each city when more than one city is looked at.
    Args:
        (dataframe) df - Pandas DataFrame with the city data
        (list) cities - list if cities the user wants to compare data for  
        (str) time_unit - time unit of analysis that has to be displayed      
    """

    if time_unit == "Month":
        print("\nCalculating the most common month for each individual city...\n")
        for city in cities:
            print("Statistics for {}:\n".format(city))
            df_temp = df[df["City"] == city]
            most_common_month = df_temp["Month"].mode()[0]
            most_common_month_count = df_temp["Month"].value_counts().max()
            print("The most common month in {} is {} with {} rentals.\n".format(city, most_common_month, most_common_month_count))
            show_frequencies(df_temp, "Month")
            
    elif time_unit == "Day":
        print("\nCalculating the most common day of the week for each individual city...\n")
        for city in cities:
            print("Statistics for {}:\n".format(city))
            df_temp = df[df["City"] == city]
            most_common_day = df_temp["Day of week"].mode()[0]
            most_common_day_count = df_temp["Day of week"].value_counts().max()
            print("The most common day in {} is {} with {} rentals.\n".format(city, most_common_day, most_common_day_count))
            show_frequencies(df_temp, "Day")

    elif time_unit == "Hour":
        print("\nCalculating the most common hour for each individual city...\n")
        for city in cities:
            print("Statistics for {}:\n".format(city))
            df_temp = df[df["City"] == city]
            most_common_hour = df_temp["Hour"].mode()[0]
            most_common_hour_count = df_temp["Hour"].value_counts().max()
            print("The most common hour in {} is {} with {} rentals.\n".format(city, most_common_hour, most_common_hour_count))
            show_frequencies(df_temp, "Hour")

    return



def time_stats(df, cities, months, days):
    """Displays statistics on the most frequent times of travel.
    Args:
        (dataframe) df - Pandas DataFrame with the city data
        (str / list) cities - city / cities the user wants to compare data for  
        (list) months - list of the months the user wants to look at 
        (list) days - list of the days the user wants to look at        
    """

    print("\nCalculating the most frequent times of travel...\n")
    start_time = time.time()

    
    # display the most common month
    if len(months) == 1 and months[0] != "None":
        print("Since you filtered the data only for one specific month ({}) no statistic for the most common month will be provided.".format(months[0]))
        print("Specifically in {} there were {} rentals.\n\n".format(months[0], len(df)))
    else:
        most_common_month = df["Month"].mode()[0]
        most_common_month_count = df["Month"].value_counts().max()
        print("The most common month is {} with {} rentals.\n\n".format(most_common_month, most_common_month_count))
        show_frequencies(df, "Month")
        
    if isinstance(cities, list):
        time_stats_more_cities(df, cities, "Month")

               
    # display the most common day of week
    if len(days) == 1 and days[0] != "None":
        print("Since you filtered the data only for one specific day ({}) no statistic for the most common day will be provided.".format(days[0]))
        print("Specifically on {} there were {} rentals.\n\n".format(days[0], len(df)))
    else:
        most_common_day = df["Day of week"].mode()[0]
        most_common_day_count = df["Day of week"].value_counts().max()
        print("The most common day of the week is {} with {} rentals.\n".format(most_common_day, most_common_day_count))
        show_frequencies(df, "Day")

    if isinstance(cities, list):
        time_stats_more_cities(df, cities, "Day")
        

    # display the most common start hour
    df["Hour"] = df["Start Time"].dt.hour
    most_common_hour = df["Hour"].mode()[0]
    most_common_hour_count = df["Hour"].value_counts().max()
    print("The most common hour is {} with {} rentals.\n".format(most_common_hour, most_common_hour_count))
    show_frequencies(df, "Hour")
    
    if isinstance(cities, list):
        time_stats_more_cities(df, cities, "Hour")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print_seperator()
    
    return




def station_stats(df, city):
    """Displays statistics on the most popular stations and trip.
    Args:
        (dataframe) df - Pandas DataFrame with the city data
        (str) citiy - city for which stats should be shown      
    """

    print("\nCalculating the most popular stations and trip in {} ...\n".format(city))

    # display most commonly used start station
    most_common_start = df["Start Station"].mode()[0]
    most_common_start_count = df["Start Station"].value_counts().max()
    print("The most common start station is {} with {} rentals.\n".format(most_common_start, most_common_start_count))
    show_frequencies(df, "Start Station")
    
    
    # display most commonly used end station
    most_common_end = df["End Station"].mode()[0]
    most_common_end_count = df["End Station"].value_counts().max()
    print("The most common end station is {} with {} rentals.\n".format(most_common_end, most_common_end_count))
    show_frequencies(df, "End Station")

    # display most frequent combination of start station and end station trip
    start_end_combinations = df.groupby(["Start Station", "End Station"]).size()
    most_common_start_end_combination = start_end_combinations.sort_values(ascending = False)
    print("The most common combination of start and end station is {} with {} rentals.\n".format(most_common_start_end_combination.idxmax(), most_common_start_end_combination.max()))

    return
    
    

def get_station_stats(df, cities):
    """Calls the function to display statistics on the most popular stations for a specific city / specific cities.
    Args:
        (dataframe) df - Pandas DataFrame with the city data
        (str / list) cities - city / cities the user wants to compare data for      
    """
 
    start_time = time.time()

    if isinstance(cities, str):
        station_stats(df, cities)   
    else:
        for city in cities:
            df_temp = df[df["City"] == city]
            station_stats(df_temp, city)       

    print("\nThis took %s seconds." % (time.time() - start_time))
    print_seperator()
    
    return



def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration.
    Args:
        (dataframe) df - Pandas DataFrame with the city data
        (str) citiy - city for which stats should be shown     
    """

    print('\nCalculating trip duration in {}...\n'.format(city))

    # display total travel time
    sum_travel_time = df["Travel Time"].sum()
    print("The total travel time is {} seconds.\n".format(sum_travel_time))

    # display mean travel time
    mean_travel_time = df["Travel Time"].mean()
    print("The average travel time is {} seconds.\n".format(mean_travel_time))
    
    return



def get_trip_duration_stats(df, cities):
    """Calls the function to display statistics on the total and average trip duration for a specific city / specific cities.
    Args:
        (dataframe) df - Pandas DataFrame with the city data
        (str / list) cities - city / cities the user wants to compare data for      
    """

    start_time = time.time()

    df["Travel Time"] = (df["End Time"] - df["Start Time"]) / pd.Timedelta(seconds = 1)
    
    if isinstance(cities, str):
        trip_duration_stats(df, cities)
    
    else:
        for city in cities:
            df_temp = df[df["City"] == city]
            trip_duration_stats(df_temp, city)
            print("\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print_seperator()
    
    return



def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (dataframe) df - dataframe with the city data
        (str) citiy - city for which stats should be shown     
    """

    print("\nCalculating user stats for {}...\n".format(city))

    # Display counts of user types
    print("Distribution of user types: ")
    print(df["User Type"].value_counts())
    print("\n")


    # Display counts of gender
    if city == "Chicago" or city == "New York City": 
        print("\nDistribution of gender: ")
        print(df["Gender"].value_counts())
        print("\n")

    # Display earliest, most recent, and most common year of birth
    if city == "Chicago" or city == "New York City": 
        print("\nThe earliest birth year is: {}".format(int(df["Birth Year"].min())))
        print("The most recent birth year is: {}".format(int(df["Birth Year"].max())))
        print("The most common birth year is: {}".format(int(df["Birth Year"].mode()[0])))
    
    return



def get_user_stats(df, cities):
    """Calls the function to displays statistics on bikeshare users.
    Args:
        (dataframe) df - Pandas DataFrame with the city data
        (str / list) cities - city / cities the user wants to compare data for       
    """
    
    start_time = time.time()
    
    if isinstance(cities, str):
        user_stats(df, cities)
    
    else:
        for city in cities:
            df_temp = df[df["City"] == city]
            user_stats(df_temp, city)
            print("\n\n")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print_seperator()
    
    return



def show_raw_data(df, cities):

    raw_data = input("Do you want to see some of the raw data? (yes / no) ")
    raw_data = raw_data.strip().title()
    
    while not raw_data in ["Yes", "No"]:
        print("Please enter a valid response") 
        raw_data = input("Do you want to see some of the raw data? (yes / no) ")
        raw_data = raw_data.strip().title()

    if raw_data:
        index_min = 0
        index_max = 0
              
        while raw_data == "Yes":
            
            if isinstance(cities, list):
                columns = ["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type", "Gender", "Birth Year", "City"]
            elif cities in ["Chicago", "New York City"]:
                columns = ["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type", "Gender", "Birth Year"]
            elif cities == "Washington":
                columns = ["Start Time", "End Time", "Trip Duration", "Start Station", "End Station", "User Type"]
                            
            index_min = index_max
            index_max += 5
            print("Raw data: ")
            print(df.iloc[index_min:index_max][columns])
            raw_data = input("Do you want to see more raw data? (yes / no) ")
            raw_data = raw_data.title() 
            while not raw_data in ["Yes", "No"]:
                print("Please enter a valid response") 
                raw_data = input("Do you want to see some of the raw data? (yes / no) ")
                raw_data = raw_data.title()
                
    return



def main():
    restart = True
    
    while restart:
        city, months, days = get_filters()
        df = load_data(city, months, days)


        time_stats(df, city, months, days)
        get_station_stats(df, city)
        get_trip_duration_stats(df, city)
        get_user_stats(df, city)
        show_raw_data(df, city)

        restart = input("\nWould you like to restart? Enter yes or no. \n")
        restart = restart.lower()
        while restart != "yes" and restart != "no":
            print("Please give a valid response.")
            restart = input("\nWould you like to restart? Enter yes or no. \n")
            restart = restart.lower()

        if restart == 'no':
            restart = False
            break
            


if __name__ == "__main__":
	main()


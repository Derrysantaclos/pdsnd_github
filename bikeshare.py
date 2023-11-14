import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list =['all', 'january', 'february','march', 'april','may','june']
refactoring_change ="Just a test line"
working_var ="Improving EFFICIENCY"
def get_filters():
    
   
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    users_name = input("Hello, I will like to get familiar with you.\n Provide me with your name:    ")
    print(f'Hello {users_name}! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print(f'Lets get started {users_name}')
    city_list =['chicago','new york city', 'washington']
    users_city_input = input(f"""
Dear {users_name}, please select a city from below -You may select a city by option number or by entering the city name
    1. Chicago
    2. New York City
    3. Washinton
City :  """).strip()
    while users_city_input.lower() not in [*city_list,'1','2','3']:
         print(f"""
Sorry {users_name}, I do not have information for the city provided Please enter a city from the list provided.
Press Ctrl C to exit this application.
""")
         users_city_input = input(f"""
please select a city from below -You may select a city by option number or by entering the city name
    1. Chicago
    2. New York City
    3. Washinton
City:   """).strip()
        
    if users_city_input in ['1','2','3']:
        
        users_city =city_list[int(users_city_input)-1]
    else:
        
        users_city = users_city_input.lower()   
     
     # TO DO: get user input for month (all, january, february, ... , june)
  
    users_month_input = input(f""" Nice, lets dive into {users_city}'s data. Which month are you particular about?
     1. all
     2. january
     3. february
     4. march
     5. april
     6. may
     7. june
     (type in full or enter the option's number)
Your choice:  """).strip()
    
    while users_month_input.lower() not in [*month_list,'1','2','3','4','5','6','7']:
         print(f"""Sorry {users_name}, I do not have information for the month provided Please enter a month from the options indicated.
Press Ctrl C to exit this application.
        """)
         users_month_input = input(f"""
Which month are you particular about?
    1. all
    2. january
    3. february
    4. march
    5. april
    6. may
    7. june
         (type in full or enter the option's number)
         Your choice:  """).strip()
    if users_month_input in ['1','2','3','4','5','6','7']:
         users_month = month_list[int(users_month_input) -1]
    else:
         users_month = users_month_input.lower()
         



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week_day_list =['all','monday','tuesday','wednesday','thursday','friday','saturday' ,'sunday']
    print(f" Finally, Pick a day from below to have a more focused view on {users_city}'s data for the month of {users_month}, feel free to select all for a broad view.")
    for index, item in enumerate(week_day_list):
         print(f"{index+1}. {item}")

    users_week_day_input = input(f"""type in full or enter the option\'s number
weekday:   """).strip()
   
    while users_week_day_input.lower() not in [*week_day_list, *[str(x) for x in range(1,len(week_day_list)+1)]]:
         for index, item in enumerate(week_day_list):
            print(f"{index+1}. {item}")
         users_week_day_input = input(f"""type in full or enter the option\'s number
weekday:   """).strip()
    
    if users_week_day_input in ['1','2','3','4','5','6','7','8']:
         user_week_day = week_day_list[int(users_week_day_input) -1]
    else:
         user_week_day = users_week_day_input.lower()

    city, month, day = users_city, users_month, user_week_day
    print('-'*40)
    print(f"Dear {users_name}, I would be providing you with information for {users_city} for the month of {users_month} and day of week to focus on is {user_week_day}")
    return city, month, day, users_name


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    file_name = CITY_DATA[city]
    print("loaded................")
    df =pd.read_csv(file_name)
    print("loadING................")

    # conver Start Time colume to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # get month and week_Day from the converted column
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    

    # filter by month
    if month != 'all':
      
         
         df = df[df['Month']==month_list.index(month)]
    if day != 'all':
        df = df[df['Day of Week']==day.title()]
   
    


    return df


def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if df['Month'].count() > 0:
        common_month = df['Month'].mode()[0]
        print(f' The most common travel month is {month_list[common_month]} for your choices')
    


        # TO DO: display the most common day of week
        if df['Day of Week'].count()  >0:
            common_week_day = df['Day of Week'].mode() [0]           
            print(f' The most common week day is {common_week_day} for your choices')
    


    # TO DO: display the most common start hour

        df['hour'] =df['Start Time'].dt.hour
        common_hour = df['hour'].mode()[0]
        print(f' The most common travel hour is {common_hour} for your choices')
    else:
        print("No Data for Chosen Date")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most popular stop station is {popular_start_station}')
                                                     


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most popular end station is {popular_end_station}')


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] +' & '+ df['End Station']
    most_frequent_comb = df['combination'].mode()[0]
    print(f'The most frequent combination is {most_frequent_comb}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    
    print(f"Total travel time for your chosen data is {total_time} seconds")


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    
    print(f"Total average travel time for your chosen data is {mean_time} seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()

        print(f" We found {user_types.count()} type of Users.\n They are:    ")
        for each_type, each_count in user_types.items():
            print(f"{each_type}, appearing {each_count} times")


        # TO DO: Display counts of gender
        gender_types = df['Gender'].value_counts()
        print(f" We found {gender_types.count()} type of gender.\n They are:    ")
        for each_type, each_count in gender_types.items():
            print(f"{each_type}, appearing {each_count} times")


        # TO DO: Display earliest, most recent, and most common year of birth
        most_earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print(f"""The earliest year birth is {most_earliest_birth_year}.
    The most recent year of birth is {most_recent_birth_year}.
    The most common year of birth is {most_common_birth_year}.
        """)
    except:
        print("Are the results incomplete? Seems our data is incomplete, work with another city while we roll up our sleeves and fix the data")
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_more_data(df, name_):
    """"
    This Function is to help the user see sample of data they have chosen
    """
    print('\nLet\s Enhance your view...\n')
    start_time = time.time()
    data_count = len(df.index)
    print(f"Dear {name_} we have come to the end of the program, I hope it was interactive and helped you with the information you were looking into.")
    start_row=0
    end_row_input = input("To give you a view of your data - Please input the number of rows you would like to see. Enter \"n\" to skip this process. (press enter to get first 5 rows).\nYour input:  ")
    
    while end_row_input != 'n':
        #if enter key
        if end_row_input.strip() =='':
            end_row_input = start_row+6
            print('Next 5 rows are')
         
        try:
            
            end_row =int(end_row_input)
            #limit to 10 rows
            if end_row -start_row >10:
                print("This has exceeded 10 rows and has thereby being trimmed to 10")
                end_row = start_row+10
             #if max reach
            if end_row >len(df.index):
                print("Almost at maximum Data, see next 10 data")
                end_row = start_row + 5
                
                
            if end_row < start_row:
                print("Sorry, this section only allows you to coninue, lets restart with first row")
                end_row =  1
                start_row = 0
                
                
            print(f"Next {end_row -start_row} rows of data are:")   
            print(df[start_row:end_row])
            start_row = end_row -1
            if start_row + 5> len(df.index):
                print("We are around the last column of data. Input 'n' to quit, else it will be restarted at 0")
                start_row =0
            start_row = end_row -1
            
        except:
            print("Input not an Integer")
        finally:
            end_row_input = input("Enter another number if you wish to continue.Ensure number is not more than 10 for better visuals. \n Note that your data would start form the previous last row (inclusive). Enter \"n\" to skip this process. press enter to get first 5 rows).\nYour input:  ")
            
        
   
    
def main():
    while True:
        city, month, day, users_name = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_more_data(df,users_name)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

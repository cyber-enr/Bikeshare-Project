import time
import pandas as pd        #https://pandas.pydata.org/pandas-docs/stable/index.html
import statistics
import matplotlib.pyplot as plt   #https://pythonprogramming.net/internet-data-matplotlib-tutorial/?completed=/loading-file-data-matplotlib-tutorial/

#Dictionary for city names so as to use later on as key-values.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'all':'all'}
DATA_TO_MONTH = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'} #Two dictionaries for the purpose of exchanging values with one another
DAY_DATA = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6,'all':'all'}
DATA_TO_DAY = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'} #Same as in months. Two dictionaries instead of using a bulkier code.

#Filtering requirements for user input
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('\nInput is not case sensitive so, HAVE FUN!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """ USE .lower() to exempt case sensitive input from user (in all while loops) """
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nWhich city do you wish to analyze? \nAVAILABLE CITIES: Chicago, New York City, Washington.\nSELECT : ")
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
            continue
        else:
            print("\nThe input you have selected does not figure in our repository! Please select any of the THREE cities stated previously!\n")    
    
    # get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nSelect the month to analyze. \nMONTHS THAT APPLY: January through June, both included. TO SELECT ALL DATA USE: all.\nSELECT : ")
        if month_name.lower() in MONTH_DATA:
            month = month_name.lower()
            continue
        else:
            print("\nNo data available for month selected! Revisit applicable months.\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nWhat specific day do you want to filter data? \nDAYS THAT APPLY: Monday through Sunday, both included. TO SELECT ALL DATA USE: all.\nSELECT : ")
        if day_name.lower() in DAY_DATA:
            day = day_name.lower()
            continue
        else:
            print("\nNo data available for the selected day! Revisit applicable days.\n")

    print('-'*40)
    return city, month, day


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
    start_time = time.time()
    print("Data is being analyzed.")
    df = pd.read_csv(city)
    # extract start month from the Start time column to create Start Month column
    df['Start Month'] = pd.DatetimeIndex(df['Start Time']).month

    # extract start day from the Start time column to create Start Day column
    df['Start Day'] = pd.DatetimeIndex(df['Start Time']).weekday

    # extract start hour from the Start Time column to create an Start Hour column
    df['Start Hour'] = pd.DatetimeIndex(df['Start Time']).hour
        
    # filter on month, if month is specified        
    print("Data was analyzed correctly.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    from statistics import mode
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # output most common month for specified filter
    while month == 'all':
        top_month = df['Start Month'].dropna()
        if top_month.empty:
            print("No popular month found for the filter specified!! Please adjust your filter!!")
            break
        else:
            top_month = top_month.mode().iat[0]
            print('The most popular month for renting a bicycle is : {}'.format(DATA_TO_MONTH.get(top_month)))
            break
    while month != 'all':
        top_month = df['Start Month'].dropna()
        if top_month.empty:
            print('User input is non existent in tables!')
            break
        elif int(MONTH_DATA.get(month)) == (top_month.mode().iat[0]):
            print('You chose {} which is the most common month for renting'.format(month.title()))
            break
        else:
            int(MONTH_DATA.get(month)) != top_month.mode().iat[0]
            print('{} is not the most popular for renting. Thus it will not be calculated'.format(month.title()))
            break
 
    # output most common day of week for specified filter
    while day == 'all':
        top_day = df['Start Day'].dropna()
        if top_day.empty:
            print('No popular day found for the filters specified!! Please adjust your filter!!!')
            break
        else:
            top_day = top_day.mode().iat[0]
            print('The most popular day for renting a bike is : {}'.format(DATA_TO_DAY.get(top_day)))
            break
    while day != 'all':
        top_day = df['Start Day'].dropna()
        if top_day.empty:
            print('User input is non existent in tables!')
            break
        elif int(DAY_DATA.get(day)) == (top_day.mode().iat[0]):
            print('You chose {} which is the most common day for renting'.format(day.title()))
            break
        else:
            int(DAY_DATA.get(day)) != top_day.mode().iat[0]
            print('{} is not the most popular day for renting. Thus it will not be calculated'.format(day.title()))
            break

    # output most common start hour for specified filter
    top_start_hour = df['Start Hour'].dropna()
    if top_start_hour.empty:
        print('No popular start hour found for the filter specified!! Please adjust your filter !!!')
    else:
        top_start_hour = top_start_hour.mode().iat[0]
        print('The most popular starting hour for the filters chosen is -> {}:00 hrs'.format(top_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    top_start_station = df['Start Station'].dropna()
    if top_start_station.empty:
        print('\'Start Station\' data NOT found!!!')
    else:
        top_start_station = top_start_station.mode().iat[0]
        print('The most common start station for the filter specified is : {}'.format(top_start_station))

    # display most commonly used end station
    top_end_station = df['End Station'].dropna()
    if top_end_station.empty:
        print('\'End Station\' data NOT found!!!')
    else:
        top_end_station = top_end_station.mode().iat[0]
        print('The most common end station for the filter specified is : {}'.format(top_end_station))

    # display most frequent combination of start and end station trip
    most_frequent_combination = df[['Start Station', 'End Station']].dropna()
    if most_frequent_combination.empty:
        print('Data NOT found!!!')
    else:   # group and sort by ascending values
        most_frequent_combination = most_frequent_combination.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
        trip_count = most_frequent_combination.iloc[0]
        stat_frame = most_frequent_combination[most_frequent_combination == trip_count].index[0] # FIND the exact trip count related to the most frequent combination of stations for selected filters!
        start_station, end_station = stat_frame      #Separates the combination station column(stat_frame) for each output
        print('\nMost frequent combination from start to finish:\n--> Start Station : {}\n--> End Station : {}\n--> Total nº of : {} trips'.format(start_station, end_station, trip_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in hours & mean travel time in minutes
    time_constraint = df['Trip Duration'].dropna()
    if time_constraint.empty:
        print("There is no recorded data for the specified trip! Adjust filters accordingly!")
    else:
        total_time = time_constraint.sum()
        mean_travel_time = time_constraint.mean()
        print("The total travel time is around %s hours." % (int(total_time/3600)))
        print("The mean travel time is approximately %s minutes." % (int(mean_travel_time/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Statistics...\n')
    start_time = time.time()
    # Display counts of user types
    if 'User Type' in df:
        user_type = df['User Type'].dropna()
        if user_type.empty:
            print("There is no recorded data at this stage!")
        else:
            user_type = user_type.value_counts()
            print('User type details: \n{}'.format(user_type))

    # Display counts of gender
    if 'Gender' in df:
        user_gender = df['Gender'].dropna()
        if user_gender.empty:
            print("There is no recorded data at this stage!")
        else:
            user_gender = user_gender.value_counts()
            print('Gender count:\n{}'.format(user_gender))

    # Display earliest, most recent, and most common year of birth
    # No need to separate by cities since washington is the only one with missing information! No error will be logged.
    if 'Birth Year' in df:
        birth_year = df['Birth Year'].dropna()
        if birth_year.empty:
            print('No data available, please adjust your filters!')
        else:
            eldest_user = birth_year.min()
            print('Earliest year of birth : {}'.format(int(eldest_user)))

            youngest_user = birth_year.max()
            print('Most recent year of birth : {}'.format(int(youngest_user)))

            most_common_year_of_birth = birth_year.mode().iat[0] #take first row as default(in case of array)
            print('Most common year of birth : {}'.format(int(most_common_year_of_birth)))
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Raw data is shown on user request. A block of five lines is shown"""
    answer = input("\nWould you like to see how the blocks of raw data are organized? [Y/N] : ")

    row_count = 0
    for index, row in df.dropna().iterrows():
        if answer.upper() == 'N':
            break
        elif answer.upper() == 'Y':
            print('\nBlock of raw data nº {}'.format(index + 1))
            print(row)
        else:
            print('\nTypo error!!! TRY AGAIN with the specified input.')
        row_count += 1
        if row_count != 0 and row_count %5 == 0:   # Percentage ends looped row extraction. Otherwise we could use another FOR loop. 
            answer = input("\nWould you like to see more raw data? [Y/N] : ")
            if answer.upper() == 'N':
                print('\nYOU TOOK THE RED PILL...'*5)
                break


def plot1(df):
    """ User gets to visualise sample data from the respective city chosen!"""   
    answer = input("\n\nWould you like to see how age relates to trip duration? [Y/N] : ")
    try:
        birth_year = df['Birth Year']
    except:
        print('Data does no exist')
    while 'Birth Year' in df:
        birth_year = df['Birth Year'].dropna()
        if birth_year.empty:
            print('No data available for selected filter, please choose another!')
            break
        elif answer.upper() == 'N':
            print('\nVery well.')
            break
        elif answer.upper() == 'Y':
            print('\n\nShowing User age vs. Trip Duration Plot...\n')
            # a data frame is made to store age
            df['user age'] = (2017 - birth_year) 
            index_names = df[(df['user age'] >=81)].index # Values above 80 are subjective & are not part of the bulk!
            index_names_2 = df[(df['user age'] >=0) & (df['user age'] <=9)].index # Values below 10 are subjective & are not in the bulk!
            # drop these row indexes from dataFrame 
            df.drop(index_names, inplace = True) 
            df.drop(index_names_2, inplace = True)
            # include duration into key to convert further on from seconds to hours.
            trip_duration = df[('Trip Duration')].dropna()
            # age is compared with trip duration, x & y axis respectively
            plt.scatter(df['user age'],(trip_duration/3600))
            plt.xlabel('User Age')
            plt.ylabel('Trip Duration (hours)')
            plt.show()
            break
        else:
            print('\Correct your input type!')
            return plot1(df)


def main():
    while True:
        city, month, day = get_filters()
        print("Input to be processed -> City : {}, Month : {}, Day : {}".format(city, month, day))

        df = load_data(city, month, day)

        if df.empty:
            print('No data found for specified filter, please adjust your filters!!!')
            continue

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        plot1(df)
        
        restart = input('\nWould you like to restart? [Enter yes or no]:\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

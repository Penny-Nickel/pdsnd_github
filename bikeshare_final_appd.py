import time
import pandas as pd
import numpy as np
import calendar
import datetime
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months= ['All','January', 'February', 'March', 'April', 'May', 'June']
days=['All','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
 
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
 
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities=['chicago', 'new york city', 'washington']
        city=input('Please type in a city to explore from Chicago, New York City, or Washington:').lower()
        if city in cities:
            break
        else:
            print("That is not a valid city, please try again and verify it is spelled correct:")
 
    # get user input for month (all, january, february, ... , june)
    while True:
        month =input('Please type in the month name for data you want to see - January, February, March, April, May, June or \"All\" for all data:').title()
        if month not in months:
           print('That is not a valid month, please enter a month or All.')
           continue
        else:
            break
 
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Please type in the day you want to see.  Example - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday, or \"all\" for all days:').title()
        if day not in days:
          print('That is not a valid day, please enter a day or all.')
          continue
        else:
            break
 
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
    ## load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
   
    return df
 
def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""
    ## convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    print('\nCalculating The Most Frequent Times of Travel...\n')
  
    ## month, day, hour into new columns from start time
    start_time = time.time()
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
   
    ## filter by month
    if month != 'all':
        month = months.index(month)+1
    ## filter by month for new dataframe
        df = df[df['month'] == month]
      
    ## filter by day of week
    if day != 'all':
    ## filter by day for new dataframe
        df = df[df['day'] == day.title()]
    return df
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
def common_data(df):
    start_time = time.time()
    # display the most common month
    most_common_mth = df['month'].mode()[0]
    most_common_mth = calendar.month_name[most_common_mth]
    print('Most common month is: ', most_common_mth)
 
    # display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('Most common day of week is: ', most_common_day)
 
    # display the most common start hour
    most_common_hr = df['hour'].mode()[0]
    #value_counts().idxmax()
    print('Most common start hour is: ', most_common_hr)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
 
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    # display most commonly used start station
    most_com_start_station = df['Start Station'].mode()[0]
    print('The most common start station: {}'.format(most_com_start_station))
 
    # display most commonly used end station
    most_com_end_station = df['End Station'].mode()[0]
    print('The most common end station: {}'.format(most_com_end_station))
 
    # display most frequent combination of start station and end station trip
    comb_group = df.groupby(['Start Station','End Station'])
    most_freq_startend_station = comb_group.size().nlargest(1)
    print ('The most frequent combination of start and end station: \n {} '.format(most_freq_startend_station))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
 
    # display total travel time
    Total_TT = df['Trip Duration'].sum()
    print('The total travel time: ')
    ##converts to show days & time from seconds
    print(str(datetime.timedelta(seconds=int(Total_TT))))
    #print('The total travel timerev:{}'pd.timedelta(seconds=int(Total_YY)))
    # display mean travel time
    Mean_TT = df['Trip Duration'].mean()
    print('\nThe mean travel time: ')
    ##converts to show days & time from seconds
    print(str(datetime.timedelta(seconds=int(Mean_TT))))
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
 
def user_stats(df):
    """Displays statistics on bikeshare users."""
 
    print('\nCalculating User Stats...\n')
    start_time = time.time()
 
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: \n {}'.format(user_types))
 
    # Display counts of gender
    #genders = df('Gender').value_counts()
    if "Gender" in df.columns:
        print('\nGender Counts: \n', df['Gender'].value_counts())
    else:
        print('Sorry, gender data is not available for this city.')
 
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_by = df['Birth Year'].min()
        print('\nThe earliest birth year:{}'.format(int(earliest_by)))
        most_recent_by = df['Birth Year'].max()
        print('The most recent birth year: {}'.format(int(most_recent_by)))
        most_com_by = df['Birth Year'].value_counts().idxmax()
        print('The most common birth year: {}'.format(int(most_com_by)))
    else:
        print('Sorry, birth year data is not available for this city.')
 
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
##Raw data view     
def raw_data(df):
    view_data=('yes','no')
    row=0
    print('Do you want to see 5 lines of raw data?\n')
    while view_data !='no':
        view_data=input('Yes or No?\n').lower()
        if view_data=='yes':
            print(df.loc[row:row+4])
            row+=5
            print('Do you want to see 5 lines of raw data?')
            next
        elif view_data =='no':
            print('Thank you, have a great day.')
            break
        else:
            print('Please enter either yes or no,')
  
            
## This is the main program and where all functions defined are within
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        common_data(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
 
if __name__ == "__main__":
    main()
 
## referenced material https://www.geeksforgeeks.org/python-string-format-method/?ref=gcse [geeksforgeeks.org] [geeksforgeeks.org]
## https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html# [pandas.pydata.org] [pandas.pydata.org]
## https://www.geeksforgeeks.org/title-in-python/ [geeksforgeeks.org] [geeksforgeeks.org]
## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html [pandas.pydata.org] [pandas.pydata.org]
##https://docs.python.org/3/library/calendar.html?highlight=calendar%20month#calendar.month_name [docs.python.org] [docs.python.org]
##https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html?highlight=iloc [pandas.pydata.org]
##https://docs.python.org/3/library/datetime.html#timedelta-objects [docs.python.org]
##http://introtopython.org/while_input.html


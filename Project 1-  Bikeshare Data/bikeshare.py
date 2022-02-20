import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#Nickname/Kareem Osama//zadkareem@gmail.com
#-                                             * Thanks for checking my work! * 
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city= str(input('\nPlease input one of the following cities: (Chicago, New York City, Washington) \n')).replace(' ','').lower()
    cities=['chicago','newyork','newyorkcity', 'washington','washingtoncity','chicagocity','washingtondc']
    
    while city not in cities:
        city= str(input('TypeError. Please input one of the following cities: (Chicago, New York City, Washington) \n')).replace(' ','').lower()
    
    if city == cities[0] or city == cities[5]:
        city = 'chicago'
    elif city == cities[1] or city== cities[2]:
        city = 'new york city'
    elif city == cities[-1] or city== cities[-3] or city ==cities[-4]:
        city= 'washington'   
    month=str(input('\nWhich month? (Type all for no prefrences)\n')).replace(' ','').lower()
    months= ['january', 'february', 'march', 'april', 'may', 'june','all']
    while month not in months:
        month=str(input('TypeError .Which month? ([Junuary -- June]...or all) \n')).replace(' ','').lower()
    if month == months[0]:
        month=1
    elif month == months[1]:
        month=2
    elif month == months[2]:
        month=3
    elif month == months[3]:
        month=4
    elif month == months[4]:
        month=5
    elif month == months[5]:
        month=6
    elif month == months[6]:
        month=7

    day= str(input('\nWhat day? (Type all for no prefrences) \n')).replace(' ','').lower()
    days=['sunday', 'monday', 'tuesday','wednesday','thursday','friday','saturday','all']
    while day not in days:
        day=str(input('TypeError .What day? (ie. Sunday, Monday,...or all) \n')).replace(' ','').lower()

    if day == days[7]:
        day=7
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
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month']= df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    if month != 7:
        df= df[df['month']==month]
    if day !=7:
        df= df[df['day']==day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months= ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month:',months[int(df['month'].mode())-1])

    print('The most common day:',str(df['day'].mode()[0]))

    print('The most common start hour:',int(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Most commonly used start station:',df['Start Station'].mode()[0],'// Occurred',df['Start Station'].value_counts()[0],'Times')

    print('Most commonly used end station:',df['End Station'].mode()[0],'// Occurred',df['End Station'].value_counts()[0],'Times')

    print('most common Start-End station trips:',df.groupby(['Start Station','End Station']).size().idxmax())
    # I can't seem to figure out how to find the number of occurrences of this groupby method unlike the two codes above

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    print('Total travel time:',int(df['Trip Duration'].count()),'Seconds','//',(int(df['Trip Duration'].count()))/60,'Minutes')


    print('Average travel time:',int(df['Trip Duration'].mean()),'Seconds','//',(int(df['Trip Duration'].mean()))/60,'Minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('User types counts:\n',df['User Type'].value_counts(ascending=False))
    print('-')
    
    try:
        print('Subscribers gender count:\n',df['Gender'].value_counts(ascending=False))
    except KeyError:
        print('Subscribers gender count:\nNot enough data.')
    print('-')

    try:
        print('Earliest year of birth:',int(df['Birth Year'].min()))
    except KeyError:
        print('Earliest year of birth:    Not enough data.')
    try:
        print('Most recent year of birth:',int(df['Birth Year'].max()))
    except KeyError:
        print('Most recent year of birth: Not enough data.')
    try:
        print('Most common year of birth:',int(df['Birth Year'].mode()[0]))
    except KeyError:
        print('Most common year of birth: Not enough data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_data(df):
    answer=input('Would you like to see some data!? (Yes/No)\n').replace(' ','').lower()
    answers=['yes','no']
    while answer not in answers:
        answer=input('\nTypeError. Would you like to see some data!? (Yes/No)\n')
    for i in range(5,100,5):
        if answer=='yes':
            print(df[['Start Time','End Time','Trip Duration','Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']].iloc[i-5:i])
            answer=input('Continue? (Yes/No)\n')
            while answer not in answers:
                answer=input('\nTypeError. Would you like to continue? (Yes/No)\n')
        else:
            break   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
        answers=['yes','no']
        restart = input('\nWould you like to restart? Enter yes or no.\n').replace(' ','').lower()
        while restart not in answers:
            restart=input('\nTypeError. Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

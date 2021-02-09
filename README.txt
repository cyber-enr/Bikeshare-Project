Udacity project: Python for bikeshare data exploration.
BUILT BY: ENRIQUE GARCIA
--------------------------------------------------------------------------
Abstract:
Three major U.S. cities - Chicago, Washington, and New York City - are put into 
evaluation to display information on bikeshare statistics. It is not clear
if this is an application that is functioning or not but the information
required and given is valid for anyone trying to start their own business.
Outputs such as most common days or most common stations are given to facilitate
user experience and see which cities have more sharing statistics in bulk and
futher evaluate other foreseeable information.
---------------------------------------------------------------------------------
Program:
Input 'python bikeshare_3UPDATED.py' on your terminal to execute this program,
or use any python type program to execute. In my case, spyder, through anaconda, 
was utilised.
---------------------------------------------------------------------------------
Details:
Three cities are given along with their specific information. Out of these,
the program takes the intial input from the user for the city, month and day. 

Upon receiving the user input, a series of blocks of code are executed to extract
the information shown below: 

Most common:
Month
Day
Hour
Start station
End station
Combination of start and end stations
Trip duration
Average trip duration

Then the program goes ahead and asks the user if they want 
to view raw data (5 rows of initial block code) or not. Following the 
input received, the program prints the following details:

Subscriber and customer count
Type of users by number
Type of users by gender 
The oldest user
The youngest user
The most common birth year amongst users 

Once this is executed the next function in the program gives us 
a plotting scenario in which , two variables are compared: user age
and trip duration with the bikes. 

*** Important to note that only CHICAGO and NEW YORK CITY have 
all the outputs available but washington is missing user information
such as: gender & age. Thus the code has been altered to not give any
errors when inputing washington.

Finally, the user is prompted with the choice of restarting the program or not.
----------------------------------------------------------------------------------
Specific Needs:
Language: Python 3.8 or above
Libraries: time, pandas, numpy, matplotlib, statistics, pyplot.
Included in the enclosed zip is the excel data given by udacity
to call in python:
chicago.csv - Dataset containing all bikeshare information for the city of Chicago.

new_york_city.csv - Dataset containing all bikeshare information for the city of New York.

washington.csv - Dataset containing all bikeshare information for the city of Washington.
Not included in the dataset information on the 'Gender' or 'Birth Year'.

Websites utilised to further expand the knowledge obtained in UDACITY:
https://realpython.com/

https://pythonprogramming.net/

https://problemsolvingwithpython.com/08-If-Else-Try-Except/08.05-Try-Except-Statements/

https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

https://www.geeksforgeeks.org/



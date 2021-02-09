# ----------------- Udacity Project -----------------
## Python for bikeshare data exploration
--------------------------------------------------------------------------
###### BUILT BY: ENRIQUE GARCIA
--------------------------------------------------------------------------
## Abstract:
Three major U.S. cities - _Chicago, Washington, and New York City_ - are put into
evaluation to display information on bikeshare statistics. The information
required and given is valid for anyone trying to start their own business.
Outputs such as most common days or most common stations are given to facilitate
user experience and see which cities have more sharing statistics in bulk and
further evaluate other foreseeable information.

---------------------------------------------------------------------------------
### Program:

To execute file, input 'python bikeshare_3UPDATED.py' on your terminal to execute this program,
or use any python type program to execute. In my case, Spyder , through Anaconda, was utilized.

---------------------------------------------------------------------------------
### Details:
Three cities are given along with their specific information. Out of these,
the program takes the initial input from the user for the city, month and day.

Upon receiving the user input, a series of blocks of code are executed to extract
the information shown below:

Most common:

- Month
- Day
- Hour
- Start station
- End station
- Combination of start and end stations

The next block calculates the Total Trip duration and the Average trip duration.

Then the program goes ahead and asks the user if they want
to view raw data (**5 rows of initial block code**) or not. Following the
input received, the program prints the following details:

- Subscriber and customer count
- Type of users by number
- Type of users by gender
- The oldest user
- The youngest user
- The most common birth year amongst users

Once this is executed the next function in the program gives us
a plotting scenario in which , two variables are compared: *user age*
and *trip duration* with the bikes.

**_Important to note that only CHICAGO and NEW YORK CITY have
all the outputs available but Washington is missing user information
such as: gender & age. Thus the code has been altered to not give any
errors when inputting Washington_**.

Finally, the user is prompted with the choice of restarting the program or not.

----------------------------------------------------------------------------------
### Requirements
**Language**: _Python 3.8 or above_

**Libraries**: _time, pandas, numpy, matplotlib, statistics, pyplot._

Included in the enclosed zip is the excel data given by Udacity
to call in python:

- chicago.csv - Dataset containing all bikeshare information for the city of Chicago.

- new_york_city.csv - Dataset containing all bikeshare information for the city of New York.

- washington.csv - Dataset containing all bikeshare information for the city of Washington.
Not included in the dataset information on the 'Gender' or 'Birth Year'.

**_Websites utilized to further expand the knowledge obtained in UDACITY:_**

https://realpython.com/

https://pythonprogramming.net/

https://problemsolvingwithpython.com/08-If-Else-Try-Except/08.05-Try-Except-Statements/

https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

https://www.geeksforgeeks.org/

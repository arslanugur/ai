What is Pandas?
      #Pandas is a module that helps us "read data" and "manipulate data". (Pandas = Panel Data: i.e. rows, cols etc.)
      #What's cool about pandas is that you can take in data and view it as a table that's human readable, 
      #but it can also be interpreted numerically so that you can do lots of computations with it.

      #We call the table of data a DataFrame (structured data). 
      
      #DataFrame, the data object for data manipulation with integrated indexing. 
      #Tools for reading and writing data between in-memory data structures and different file formats. 
      #Data alignment and integrated handling of missing data. 
      #Reshaping and pivoting of data sets. Label-based slicing, fancy indexing, and subsetting of large data sets. 
      #Data structure column insertion and deletion. Group by engine allowing split-apply-combine operations on data sets. 
      #Data set merging and joining. 
      #Hierarchical axis indexing to work with high-dimensional data in a lower-dimensional data structure. 
      #Time series-functionality: Date range generation and frequency conversion, 
      #moving window statistics, moving window linear regressions, date shifting and lagging. Provides data filtration.
      
Read in Your Data
      #We need to start by importing Pandas. 
      #It's standard practice to nickname it pd so that it's faster to type later on.
import pandas as pd   
      #A dataset of Titanic passengers. 
      #For each passenger, we’ll have some data on them as well as whether or not they survived the crash.
    
      #Our data is stored as CSV (comma-separated values) file. The titanic.csv file is below. 
      #The first line is the header and then each subsequent line is the data for a single passenger. 

Survived, Pclass,    Sex,    Age, Siblings/Spouses, Parents/Children, Fare
       0,      3,   male,   22.0,                1,                0, 7.25
       1,      1, female,   38.0,                1,                0, 71.2833
       1,      3, female,   26.0,                0,                0, 7.925
       1,      1, female,   35.0,                1,                0, 53.1
      
      #to pull the data into pandas so we can view it as a DataFrame.
      #The read_csv function takes a file in csv format and converts it to a Pandas DataFrame. 
df = pd.read_csv('titanic.csv')
      
      #The object df is now our pandas dataframe with the Titanic dataset. 
      #Now we can use the head method to look at the data.
      #The head method returns the first 5 rows of the DataFrame.
print(df.head())
      
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
print(df.head())
      #output:
"""Survived  Pclass     Sex   Age  Siblings/Spouses  Parents/Children     Fare
0         0       3    male  22.0                 1                 0   7.2500
1         1       1  female  38.0                 1                 0  71.2833
2         1       3  female  26.0                 0                 0   7.9250
3         1       1  female  35.0                 1                 0  53.1000
4         0       3    male  35.0                 0                 0   8.0500
"""

      #Generally data is stored in CSV (comma-separated values) files, 
      #which we can easily read in with panda’s read_csv function. 
      #The head method returns the first 5 rows.
      
      #to read in a file called mydata.csv as a pandas DataFrame and print a table of the first 15 rows.
import pandas as pd 
df = pd.read_csv('mydata.csv')
print(df.head(15))
      #To get last 5 rows: print(df. tail())

Summarize the Data
      #Usually our data is much too big for us to be able to display it all.
      #Looking at the first few rows is the first step to understanding our data, 
      #but then we want to look at some summary statistics.
      #In pandas, we can use the describe method. It returns a table of statistics about the columns.
print(df.describe())
      #to add a line in the code below to force python to display all 6 columns. 
      #Without the line, it will abbreviate the results. 
import pandas as pd
pd.options.display.max_columns = 6
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
print(df.describe())
      #output:
"""      Survived      Pclass         Age  Siblings/Spouses  Parents/Children      Fare
count  887.000000  887.000000  887.000000        887.000000        887.000000      887.00000 
mean     0.385569    2.305524   29.471443          0.525366          0.383315      32.30542  
std      0.487004    0.836662   14.121908          1.104669          0.807466      49.78204
min      0.000000    1.000000    0.420000          0.000000          0.000000      0.00000  
25%      0.000000    2.000000   20.250000          0.000000          0.000000      7.92500 
50%      0.000000    3.000000   28.000000          0.000000          0.000000      14.45420
75%      1.000000    3.000000   38.000000          1.000000          0.000000      31.13750 
max      1.000000    3.000000   80.000000          8.000000          6.000000      512.32920
"""

"""
       For each column we see a few statistics. Note that it only gives statistics for the numerical columns.
       Let's review what each of these statistics means:
       Count: This is the number of rows that have a value. 
              In our case, every passenger has a value for each of the columns, 
              so the value is 887 (the total number of passengers).
       Mean: Recall that the mean is the standard average.
       Std: This is short for standard deviation. This is a measure of how dispersed the data is.
       Min: The smallest value
       25%: The 25th percentile
       50%: The 50th percentile, also known as the median.
       75%: The 75th percentile
       Max: The largest value
       We use the Pandas describe method to start building some intuition about our data.
"""
      #what is the maximum Pclass (PassengerClass) and the median age on the dataframe?
      #max = 3 / median = 28

      #Extra Infos:
      #a library is a collection of related functionality, 
      #a module only provides a single piece of functionality.
      #https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#:~:text=to%20different%20objects.-
      #https://www.youtube.com/playlist?list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy
      #https://docs.python.org/3/library/csv.html
      #"Five-number summary" is called to: Min: , 25%: ,50%: ,75%: ,Max https://en.wikipedia.org/wiki/Five-number_summary
      
      
      
      
      
      

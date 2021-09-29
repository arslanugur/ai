Selecting a Single Column
      #We often will only want to deal with some of the columns that we have in our dataset. 
      #To select a single column, we use the square brackets and the column name.

      #In this example,to select just the column with the passenger fares.
col = df['Fare']
print(col)

      #The result is what we call a Pandas Series.
      #A series is like a DataFrame, but it's just a single column. 
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
col = df['Fare']
print(col)

"""output:
0       7.2500
1      71.2833
2       7.9250
3      53.1000
4       8.0500
        ...   
882    13.0000
883    30.0000
884    23.4500
885    30.0000
886     7.7500
Name: Fare, Length: 887, dtype: float64
"""

      #A Pandas Series is a single column from a Pandas DataFrame.
      #Panda Series: Pandas Series is a one-dimensional labeled array capable of holding data of any type
      #(integer, string, float, python objects, etc.). 
      #The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet.
      
      #df['col_name'] gives a series. 
      #df[['col_name']] gives dataframe
      
      #To select 6 rows and 5 colums: 
import pandas as pd 
pd.options.display.max_rows = 6 
pd.options.display.max_columns = 5 
df = pd.read_csv('https://***.com/uploads/files/titanic.csv') 
print(df)

      #You can use slice notation with series. 
      #print(col[0]) prints the first element of the series. 
      #print(col[::-1]) prints the whole series in reverse order.
      
      
      #What datatype is the variable age_col? age_col = df['Age'] --> PandasSeries = column
      #As the question is asking about column only. The panda series is known as column. Therefore no need to select the whole dataframe.
      
      
Selecting Multiple Columns
      #To select multiple columns from our original DataFrame, creating a smaller DataFrame.
      #To select just the Age, Sex, and Survived columns from our original DataFrame.
      #To put these values in a list as follows:
['Age', 'Sex', 'Survived']

      #to use that list inside of the bracket notation df[...] 
      #When printing a large DataFrame that’s too big to display, 
      #It can be used the head method to print just the first 5 rows.
small_df = df[['Age', 'Sex', 'Survived']]
print(small_df.head()) 


import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
small_df = df[['Age',  'Sex', 'Survived']]
print(small_df.head())

"""output:
    Age     Sex  Survived
0  22.0    male         0
1  38.0  female         1
2  26.0  female         1
3  35.0  female         1
4  35.0    male         0
"""      
      #When selecting a single column from a Pandas DataFrame, use single square brackets. 
      #When selecting multiple columns, use double square brackets.

      #creates a DataFrame new_df which has the columns Pclass, Age, and Fare?
new_df = df[['Pclass', 'Age', 'Fare']]

      #https://youtu.be/vmEHCJofslg
      
      
Creating a Column
      #Data in a slightly different format than it originally comes in. 
      #For example, our data has the sex of the passenger as a string ("male" or "female"). 
      #This is easy for a human to read, but when we do computations on our data later on, 
      #we’ll want it as boolean values (Trues and Falses).

      #To create a new column in our DataFrame that is True if the passenger is male and False if they’re female.
      #Recall the syntax for selecting the Sex column:
df['Sex']
      #We create a Pandas Series that will be a series of Trues and Falses
      #(True if the passenger is male and False if the passenger is female). 
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
print(df['Sex'] == 'male')
      
"""output
0       True
1      False
2      False
3      False
4       True
       ...  
882     True
883    False
884    False
885     True
886     True
Name: Sex, Length: 887, dtype: bool
"""
      #Now we want to create a column with this result. 
      #To create a new column, we use the same bracket syntax (df['male']) and then assign this new value to it.
df['male'] = df['Sex'] == 'male'

      #Code
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
df['male'] = df['Sex'] == 'male'
print(df.head())

"""output
   Survived  Pclass     Sex  ...  Parents/Children     Fare   male
0         0       3    male  ...                 0   7.2500   True
1         1       1  female  ...                 0  71.2833  False
2         1       3  female  ...                 0   7.9250  False
3         1       1  female  ...                 0  53.1000  False
4         0       3    male  ...                 0   8.0500   True

[5 rows x 8 columns]
"""
      #Our dataframe now looks as follows. Note the new column at the end. 
      
      #Often our data isn’t in the ideal format. 
      #Pandas makes it easy to create new columns based on our data so we can format it appropriately.

      #If you don't want true and false you can use: 
import pandas as pd 
df = pd.read_csv('https://***.com/uploads/files/titanic.csv') 
df['male'] = df['Sex'].apply(lambda x:"man" if x== 'male' else "not male") 
print(df.head()) 
      #Obviously change 'male' and 'not male' to anything you want
      
      #To create the “First Class” column, which is True if the passenger is in Pclass 1 and False otherwise.
df['First Class'] = df['Pclass'] == 1
            


      

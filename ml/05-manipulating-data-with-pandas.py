Selecting a Single Column
      //We often will only want to deal with some of the columns that we have in our dataset. 
      //To select a single column, we use the square brackets and the column name.

      //In this example,to select just the column with the passenger fares.
col = df['Fare']
print(col)

      //The result is what we call a Pandas Series.
      //A series is like a DataFrame, but it's just a single column. 
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

      //A Pandas Series is a single column from a Pandas DataFrame.
      //Panda Series: Pandas Series is a one-dimensional labeled array capable of holding data of any type
      //(integer, string, float, python objects, etc.). 
      //The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet.
      
      //df['col_name'] gives a series. 
      //df[['col_name']] gives dataframe
      
      //To select 6 rows and 5 colums: 
import pandas as pd 
pd.options.display.max_rows = 6 
pd.options.display.max_columns = 5 
df = pd.read_csv('https://***.com/uploads/files/titanic.csv') 
print(df)

      //You can use slice notation with series. 
      //print(col[0]) prints the first element of the series. 
      //print(col[::-1]) prints the whole series in reverse order.
      
      
  
  

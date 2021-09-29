What is Numpy?
      #Numpy is a Python package for manipulating lists and tables of numerical data. 
      #We can use it to do a lot of statistical calculations. 
      #We call the list or table of data a numpy array.

      #We often will take the data from our pandas DataFrame and put it in numpy arrays. 
      #Pandas DataFrames are great because we have the column names and other text data that makes it human readable. 
      #A DataFrame, while easy for a human to read, is not the ideal format for doing calculations. 
      #The numpy arrays are generally less human readable, but are in a format that enables the necessary computation.
      #Numpy is a Python module for doing calculations on tables of data. 
      #Pandas was actually built using Numpy as it’s foundation.

      #Handling Tabular Data: Panda (Dataframe) --> DataFrame is a multidimensional array.
      #Handling Numerical Data: Numpy (Numpy Array)
      
      #The data object in numpy is called a(n) array
      
Converting from a Pandas Series to a Numpy Array
      #We often start with our data in a Pandas DataFrame, 
      #but then want to convert it to a numpy array. The values attribute does this for us.

      #To convert the Fare column to a numpy array.

      #First we recall that we can use the single bracket notation to get a pandas Series of the Fare column as follows.
df['Fare']

      #Then we use the values attribute to get the values as a numpy array.
df['Fare'].values

import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
print(df['Fare'].values)

      #This is what the above array looks like:
"""output: 
array([ 7.25 , 71.2833,  7.925, 53.1, 8.05, 8.4583, …
"""

      #The result is a 1-dimensional array. 
      #You can tell since there's only one set of brackets and it only expands across the page (not down as well). 
  
      #The values attribute of a Pandas Series give the data as a numpy array.
    
      #to get a numpy array of the values in the 'Age' column from the DataFrame df.
df['Age'].values

      #The values attribute of a Pandas Series give the data as a numpy array.

      

Converting from a Pandas DataFrame to a Numpy Array
      #If we have a pandas DataFrame (instead of a Series as in the last part), 
      #we can still use the values attribute, 
      #but it returns a 2-dimensional numpy array.

      #Recall that we can create a smaller pandas DataFrame with the following syntax.
df[['Pclass', 'Fare', 'Age']]

      #Again, we apply the values attribute to get a numpy array.
df[['Pclass', 'Fare', 'Age']].values 

import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
print(df[['Pclass', 'Fare', 'Age']].values)

      #This is what the above array looks like:
"""output
[[ 3.      7.25   22.    ]
 [ 1.     71.2833 38.    ]
 [ 3.      7.925  26.    ]
 ...
 [ 3.     23.45    7.    ]
 [ 1.     30.     26.    ]
 [ 3.      7.75   32.    ]]
"""
      #This is a 2-dimensional numpy array. 
      #You can tell because there’s two sets of brackets, 
      #and it expands both across the page and down. 
  
      #The values attribute of a Pandas DataFrame give the data as a 2d numpy array.
    
      #1.) Use the 'values' attribute with a pandas series to get a 1-D numpy array. 
      #2.) Use the same with a smaller dataframe from a bigger pandas dataframe to get a 2-D array.
      
      #The following code returns what type of numpy array:
df[['Survived', 'Pclass']].values    
      #2 dimensional - The number of brackets is the number of the dimensions of the array.
      #2 dimensional arrays are nested lists in python.

  
Numpy Shape Attribute
      #We use the numpy shape attribute to determine the size of our numpy array. 
      #The size tells how many rows and columns are in our data.

      #First, let's create a numpy array with the Pclass, Fare, and Age.
arr = df[['Pclass', 'Fare', 'Age']].values

      #If we look at the shape, we get the number of rows and the number of columns: 
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr.shape)    #output: (887, 3)

      #This result means we have 887 rows and 3 columns. 
  
      #Use the shape attribute to find the number of rows and number columns for a Numpy array. 
      #You can also use the shape attribute on a pandas DataFrame (df.shape).
    
      #Don’t confuse shape with dimension. 
      #If an array has 4 rows and 9 columns, the array’s shape will (4, 9). 
      #Length of the shape tuple is equal to the dimension. In this example, the dimension is 2
      
      #https://stats.stackexchange.com/questions/284995/are-1-dimensional-numpy-arrays-equivalent-to-vectors
      
      #Example
import pandas as pd 
df = pd.read_csv('https://***.com/uploads/files/titanic.csv') 
arr = df[['Pclass', 'Fare', 'Age']].values 
print(arr.shape) 
arr = arr.reshape(3,887) 
print(arr.shape)

      #Example
import pandas as pd 
df = pd.read_csv('https://***.com/uploads/files/titanic.csv') 
arr = df[['Pclass', 'Fare', 'Age']].values 
print(arr.shape) 
arr = df[['Pclass', 'Fare', 'Age']].head().values 
print(arr.shape) 
arr = df[['Pclass', 'Fare', 'Age']].head(2).values 
print(arr.shape) 
arr = df[['Pclass', 'Fare']].head(500).values 
print(arr.shape) 
arr = df[['Pclass', 'Fare']].head(300).values.shape 
print(arr)    #output: (887, 3) (5, 3) (2, 3) (500, 2) (300, 2)

      #Pandas DataFrame also has a shape attribute 
      #that returns a tuple that contains the number of rows and columns in the DataFrame.
  

      #Recall that we have 887 datapoints in our Titanic dataset. What is the output of the following code?
arr = df[['Survived', 'Pclass']].values
print(arr.shape)    #output: (887, 2)
      #For a 2-d array, the shape will always include the number of "rows first" and then the number of columns
      #shape = (rows, cols)
 

    


  

      
      
    

      

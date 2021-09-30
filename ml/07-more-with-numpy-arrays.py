SELECT FROM A NUMPY ARRAY
      #to see a numpy array:
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr)

"""output:
[[ 3.      7.25   22.    ]
 [ 1.     71.2833 38.    ]
 [ 3.      7.925  26.    ]
 ...
 [ 3.     23.45    7.    ]
 [ 1.     30.     26.    ]
 [ 3.      7.75   32.    ]]
 """
      #to select a single element from a numpy array
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr[0, 1])
      #output: 7.25
  
      #This will be the 2nd column of the 1st row (remember that we start counting at 0).
      #So it'll be the Fare of the 1st passenger, or 7.25.

      #We can also select a single row, for example, the whole row of the first passenger:
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr[0])   #output: [ 3.    7.25 22.  ]

      #To select a single column (in this case the Age column), we have to use some special syntax:
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr[:,2])
      #output: ---
  
      #Code II
import pandas as pd
df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr[0, 1])
print(arr[0])
      #output: ---
  
      #The syntax can be interpreted as we’re taking all of the rows, but just the column at index 2. 
  
      #Using different syntax within brackets, we can select single values, a whole row or a whole column.

      #To summarise (assume arr to be a numpy array and L to be a normal Python list): 
      #1) arr[x, y] is similar to L[x][y] (starting index is 0). 
      #2) arr[x] is similar to L[x]. 
      #3) arr[a:b] is similar to L[a:b] 
      #   (A 2-D array/list of the rows from index positions a to b, not including the one at b) 
      #4) arr[a:b, y] is similar to L[a:b][y] 
      #   (A 1-D array/list of the elements/items in the rows at index a to b, not including b, of the column at index y). 
      #5) arr[:, y] is similar to L[:][y] (the whole column at index y)

      #Example
import pandas as pd 
df = pd.read_csv('https://***.com/uploads/files/titanic.csv') 
arr = df[['Pclass', 'Fare', 'Age']].head().values 
print(arr) 
print(arr[0,:]) 
print(arr[2]) 
print(arr[:,2]) 
print(arr[0,2])
"""output
[[ 3.      7.25   22.    ]
 [ 1.     71.2833 38.    ]
 [ 3.      7.925  26.    ]
 [ 1.     53.1    35.    ]
 [ 3.      8.05   35.    ]]
[ 3.    7.25 22.  ]
[ 3.     7.925 26.   ]
[22. 38. 26. 35. 35.]
22.0
"""

      #An array of some of our data:
arr = df[['Pclass', 'Fare', 'Age']].values
      How would you select the Fares of all the passengers?
arr[:, 1]

MASKING
      #Often times you want to select all the rows that meet a certain criteria.
      #In this example, we'll select all the rows of children (passengers under the age of 18). 
      #A reminder of our definition of the array:
arr = df[['Pclass', 'Fare', 'Age']].values

      #Recall that we can get the Age column with the following syntax:
arr[:, 2]
      
      #We create what we call a mask first. 
      #This is an array of boolean values (True/False) of whether the passenger is a child or not.
mask = arr[:, 2] < 18

      #Let's look at the mask array to make sure we understand it.
array([False, False, False, False, False, False, False, True, False, …
       
      #The False values mean adult and the True values mean child, so the first 7 passengers are adults, 
      #then 8th is a child, and the 9th is an adult.
      #Now we use our mask to select just the rows we care about:
arr[mask]
      #Let's look at this new array.
array([[3., 21.075, 2.],
       [2., 30.0708, 14.],
       [3., 16.7, 4.],
       [3., 7.8542, 14.],

       #If we recall that the third column is the passengers age, 
       #we see that all the rows here are for passengers that are children.
        
       #Generally, we don't need to define the mask variable and can do the above in just a single line:
arr[arr[:, 2] < 18] 
       
       #Example  
import pandas as pd

df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
# take first 10 values for simplicity
arr = df[['Pclass', 'Fare', 'Age']].values[:10]

mask = arr[:, 2] < 18
print(arr[mask])
print(arr[arr[:, 2] < 18])
       
"""output
[[ 3.     21.075   2.    ]
 [ 2.     30.0708 14.    ]]
[[ 3.     21.075   2.    ]
 [ 2.     30.0708 14.    ]]
"""
       
      #A mask is a boolean array (True/False values) that tells us which values from the array we’re interested in.
             
      #Pay attention to the fact, looks still using Pandas module to convert Pandas Data Frames into Numpy Arrays.
      #All manipulations have been executed without importing Numpy module
      #but, we are STILL using numpy arrays from NumPy. 
      #In fact pandas was built on top of numpy, that is, it's derived from it. 
      #So basically we're leveraging the powers of NumPy. 
      #https://www.quora.com/Is-Numpy-necessary-for-Data-analysis-in-Python-I-already-know-Pandas-and-Matplotlib
             
      #How mask might work in background (Custom Implementation): https://code.sololearn.com/c6J21B61GKEP/?ref=app
      
       
      #array of some of our data:
arr = df[['Pclass', 'Fare', 'Age']].values

      #Which of the following would complete the code to subset the array to get just the passengers in Pclass1?
arr[ arr[:, 0] == 1]
      #to select 1st column as in Py index start from 0 
      #Now we have to select Pclass 1 arr[:, 0] == 1 Will select the class 1 We want this value in an array arr[arr[:, 0]] 
      #arr[0] gets all the entries in the first row, 
      #meaning that you get the pclass, fare, and age for the only first person in our dataframe. 
      #arr[:,0] gets all the entries in the first column, 
      #meaning that we get the pclass for all the passengers in our dataframe.
      #For passengers in pclass which means whole column for that we use [:.0] 
      #That is , : is for rows and 0 for column. If they had asked for the row then we could use [0]. 
      #And for single passenger we could use [1,0]
       
SUMMING and COUNTING
      #Let’s say we want to know how many of our passengers are children. 
      #We still have the same array definition and can take our mask or boolean values from the previous part.
arr = df[['Pclass', 'Fare', 'Age']].values
mask = arr[:, 2] < 18
      
      #Recall that True values are interpreted as 1 and False values are interpreted as 0. 
      #So we can just sum up the array and that’s equivalent to counting the number of true values.
print(mask.sum()) 
       
      #Again, we don’t need to define the mask variable.
print((arr[:, 2] < 18).sum())
       
      #Example
import pandas as pd

df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
mask = arr[:, 2] < 18

print(mask.sum())             #output: 130
print((arr[:, 2] < 18).sum()) #output: 130
              
      #Summing an array of boolean values gives the count of the number of True values.
      
      #Example
import pandas as pd

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
mask = arr[:, 2] < 18

#This function does the same thing as all
#of those build in functions
def get_child_len():
    count=0
    for i in mask:
        if i == True:
            count+=1
        continue
    return count

print(mask.sum())
print(len(arr[mask]))
#and this proves it
print(get_child_len())

       
      #Which of the following is correct for counting the number of passengers in Pclass 1? 
      #We have the following array definition:
arr = df[['Pclass', 'Fare', 'Age']].values 
(arr[:, 0] == 1).sum() #answer
      #Explanation: Counting passengers in Pclass 1. arr[rows,columns] is the syntax. 
      #Now the ".sum()" will consider all the passengers and give a number. 
      #The "== 1" is a Boolean value where 1 = True and 0 = False.
       
       
      #Example
      #Trying different mask variations 8/19/20. Double mask and triple mask 8/21/20
import pandas as pd

df = pd.read_csv('https://***.com/uploads/files/titanic.csv')
# take first 10 values for simplicity
arr = df[['Pclass', 'Fare', 'Age']].values[:10]

print(arr) #Original Arr of 10 values
print('-')

mask = arr[:, 2] < 18 #Age
print(arr[mask])
print('-')

print(arr[arr[:, 2] < 18]) #Age
print('-')

mask = arr[:, 1] > 30 #Fare
print(arr[mask])
print('-')

mask = arr[:, 1] < 8 #Fare
print(arr[mask])
print('-')

mask = arr[:, 0] == 1 #Pclass
print(arr[mask])
print('-')

#Wanted to try a double mask before continuing tutorial. 
arr2 = arr[mask] #1st Pclass
mask2 = arr2[:, 1] > 60 #Fare
print(arr2[mask2]) #This was not doing what I wanted. Got it to work now! 8/21/20
print('-')

#OK time for a triple mask next. 8/21/20
arr3 = arr[mask] #1st Pclass
mask3 = arr3[:, 1] < 60 #Fare
arr4 = arr3[mask3]
mask4 = arr4[:, 2] > 35 #Age
print(arr4[mask4]) #There is probably another way to do this that I'll learn later. 
       
       

       
      #Example
import numpy as np

data = [15, 16, 18, 19, 22, 24, 29, 30,45,48, 34]

print("mean:", np.mean(data))
print("median:", np.median(data))
print("50th percentile (median):", np.percentile(data, 50))
print("25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))
print("standard deviation:", np.std(data))
print("variance:", np.var(data))

"""output:
mean: 27.272727272727273
median: 24.0
50th percentile (median): 24.0
25th percentile: 18.5
75th percentile: 32.0
standard deviation: 10.745746804208876
variance: 115.47107438016528
"""

       
       

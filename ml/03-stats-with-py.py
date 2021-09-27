Statistics with Python
      #We can calculate all of these operations with Python. We will use the Python package numpy. 
      #We will use numpy more later for manipulating arrays, 
      #but for now we will just use a few functions for statistical calculations: mean, median, percentile, std, var.
      #First we import the package. It is standard practice to nickname numpy as np
import numpy as np
      #Let’s initialize the variable data to have the list of ages.
data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
      #Now we can use the numpy functions. 
      #For the mean, median, standard deviation and variance functions, we just pass in the data list. 
      #For the percentile function we pass the data list and the percentile (as a number between 0 and 100). 

      #Example
import numpy as np
      #Numpy is a python library that allows fast and easy mathematical operations to be performed on arrays.
data = [15, 16, 18, 19, 22, 24, 29, 30, 34]                   #outputs

print("mean:", np.mean(data))                                 #mean: 23.0
print("median:", np.median(data))                             #median: 22.0
print("50th percentile (median):", np.percentile(data, 50))   #50th percentile (median): 22.0
print("25th percentile:", np.percentile(data, 25))            #25th percentile: 18.0
print("75th percentile:", np.percentile(data, 75))            #75th percentile: 29.0
print("standard deviation:", np.std(data))                    #standard deviation: 6.342099196813483
print("variance:", np.var(data))                              #variance: 40.22222222222222


      # the code for calculating and printing the 60th percentile of the data array.
import numpy as np
print(np.percentile(data, 60))




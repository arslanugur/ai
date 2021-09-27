Percentiles
      #Percentile - percentage (% - 100). 
      #Half of 100 it 50 - hence the 50th percentile is the median (middle value).
    
      #The median can also be thought of as the 50th percentile. 
      #This means that 50% of the data is less than the median
      #and 50% of the data is greater than the median. 
      #This tells us where the middle of the data is, 
      #but we often want more of an understanding of the distribution of the data. 
      #We’ll often look at the 25th percentile and the 75th percentile. 
      
      #The 25th percentile is the value that’s one quarter of the way through the data. 
      #This is the value where 25% of the data is less than it (and 75% of the data is greater than it).

      #Similarly, the 75th percentile is three quarters of the way through the data. 
      #This is the value where 75% of the data is less than it (and 25% of the data is greater than it).
      #If we look at our ages again:
15, 16, 18, 19, 22, 24, 29, 30, 34 

      #We have 9 values, so 25% of the data would be approximately 2 datapoints. 
      #So the 3rd datapoint is greater than 25% of the data. 
      #Thus, the 25th percentile is 18 (the 3rd datapoint).
      #Similarly, 75% of the data is approximately 6 datapoints. 
      #So the 7th datapoint is greater than 75% of the data.
      #Thus, the 75th percentile is 29 (the 7th datapoint).

      #The full range of our data is between 15 and 34. 
      #The 25th and 75th percentiles tell us that half our data is between 18 and 29. 
      #This helps us gain understanding of how the data is distributed. 

      #If there is an even number of datapoints, to find the median (or 50th percentile), ü
      #you take the mean of the two values in the middle.
      
      #To take percentiles we do the following: 
      #25th Percentile: Total Numbers x 25% =9 x 25% =9 x (25/100) =9 x (0.25) =2.25 
      #This means that the numbers above 2nd position will be greater than 25% 
      #and the numbers below 3rd position will be less than 25%. 
      #This is why we will take the ceiling value (rounding the decimal to next whole number) for percentile. 
      #In this case, 25th percentile is the 3rd position. 
      #75th Percentile: Total Numbers x 75% =9 x 75% =9 x (75/100) =9 x (0.75) =6.75 
      #This means that the numbers above 6th position will be greater than 75% 
      #and the numbers below 7th position will be less than 75%. 
      #This is why we will take the ceiling value for percentile. 
      #In this case, 75th percentile is the 7th position.
      
      #For example, if you have 4 data points ( 1, 3, 5, 9 ), 
      #to find the 50th percentile you would need to add 3+5=8, 
      #then divide 8 by the number of data points used in the addition (2), 
      #and so 8÷2=4, so 4 becomes your median value, or 50th percentile.
      
      #50th Percentile -----> 1/2 of n; aka Median
      #25th Percentile -----> 1/4 of n; 
      #75th Percentile -----> 3/4 of n; 
      #where: n - represents the total number of values.
      
      #Each number in the list represents the number of kids in the family. 
      #Thus there is 1 family with 0 kids, 5 families with 1 kid, etc.
[0, 1, 1, 1, 1, 1, 2, 2, 2, 3, 6]

 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11 
      #The 25th percentile is 1. --> meaning that 25% of the people are 1 or younger.
      #The 50th percentile (aka median) is 1. --> meaning that 50% of the people are also 1 or younger.
      #The 75th percentile is 2. --> meaning that 75% of the people are 2 or younger.
      
      25% is (11+1)/4=3rd position 
      50% is 2(11+1)/4=6th position 
      75% is 3(11+1)/4=9th position
      
      #For the 11 datapoints: 25% is 1*11/4 = 2.75 
      #So 3-rd datapoint is greater than 25% 50%, ie median for odd number of datapoints, 
      #so 6-th datapoint 75% is 3*11/4 = 8.25 So 9-th datapoint is greater than 75%
ordered dataset = 0,1,1,1,1,1,2,2,2,3,6 
n = 11 
k = percentile k i = --- ( n + 1) 100 1. 25 i = --- ( 11 + 1 ) 100 i = 3 
      #Since i is an integer, we can now locate the value found in the 3rd position in the ordered dataset. 
  
      #https://en.m.wikipedia.org/wiki/Percentile
    
Standard Deviation & Variance
      #We can get a deeper understanding of the distribution of our data with the standard deviation and variance. 
      #The standard deviation and variance are measures of how dispersed or spread out the data is.
      #standard deviation is the square root of the variance. 
      
      #We measure how far each datapoint is from the mean.
      #Let's look at our group of ages again:
15, 16, 18, 19, 22, 24, 29, 30, 34
      #Recall that the mean is 23.
      #Let's calculate how far each value is from the mean. 15 is 8 away from the mean (since 23-15=8). 
      #Here's a list of all these distances:
8, 7, 5, 4, 1, 1, 6, 7, 11
      #We square these values and add them together.
64, 49, 25, 16, 1, 1, 36, 49, 121 = 362
      #We divide this value by the total number of values and that gives us the variance.
362 / 9 = 40.22 
      #To get the standard deviation, we just take the square root of this number and get: 6.34
      #If our data is normally distributed like the graph below, 
      #68% of the population is within one standard deviation of the mean. 
      #In the graph, we’ve highlighted the area within one standard deviation of the mean.
      #You can see that the shaded area is about two thirds (more precisely 68%) of the total area under the curve. 
      #If we assume that our data is normally distributed, 
      #we can say that 68% of the data is within 1 standard deviation of the mean.
population density
|
|       ---
|
|
|_____|___|___|_____
   mean mean mean
   -std      +std
    
       #In our age example, while the ages are likely not exactly normally distributed, 
       #we assume that we are and say that 
       #approximately 68% of the population has an age within one standard deviation of the mean. 
       #Since the mean is 23 and the standard deviation is 6.34, 
       #we can say that approximately 68% of the ages in our population are between 16.66 (23 minus 6.34) 
       #and 29.34 (23 plus 6.34). 
      
       #Even though data is never a perfect normal distribution, 
       #we can still use the standard deviation to gain insight about how the data is distributed.
        
       #68% is the population which exist between two ages which we calculate to add and minus the standard value in mean value.
       #16.66 to 29.34 We easily calculate it 29.34 is 79th percentile 
       #And 16.66 is almost 11th percentile And the 79-11=68% shaded area
      

      
      
        

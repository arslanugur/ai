In this exercise, we will build a simple recommendation system for an online shopping application where the users' purchase history is recorded 
and used to predict which products the user is likely to buy next.
We have data from six users. 
For each user, we have recorded their recent shopping history of four items and the item they bought after buying these four items:

|User       |           Shopping History                                                 |                Purchase           |
| :-------: | :------------------------------------------------------------------------: | :-------------------------------: |
|   Sanni   |         boxing gloves,	Moby Dick (novel),	headphones,	sunglasses             |                coffee beans       | 
|   Jouni   |         t-shirt,	coffee beans,	coffee maker,	coffee beans                   |                coffee beans       | 
|   Janina   |         sunglasses,	sneakers,	t-shirt,	sneakers,	ragg wool                  |                socks       | 
|  Henrik	   |         2001: A Space Odyssey (dvd),	headphones,	t-shirt,	boxing gloves    |                flip flops       | 
|   Ville	   |         t-shirt,	flip flops,	sunglasses,	Moby Dick (novel)	               |                sunscreen      | 
|   Teemu		   |         Moby Dick (novel),	coffee beans,	2001: A Space Odyssey (dvd),	headphones	 |      coffee beans      | 
	                                 	                            

The most recent purchase is the one in the rightmost column, so for example, after buying a t-shirt, flip flops, sunglasses, 
and Moby Dick (novel), Ville bought sunscreen. Our hypothesis is that after buying similar items, other users are also likely to buy sunscreen.

To apply the nearest neighbor method, we need to define what we mean by nearest. 
This can be done in many different ways, some of which work better than others. 
Let’s use the shopping history to define the similarity (“nearness”) by counting how many of the items have been purchased by both users.

For example, users Ville and Henrik have both bought a t-shirt, so their similarity is 
1. Note that flip flops doesn't count because we don't include the most recent purchase when calculating the similarity — it is reserved for another purpose.

Our task is to predict the next purchase of customer Travis who has bought the following products:

|User       |           Shopping History                                                 |                Purchase           |
| :-------: | :------------------------------------------------------------------------: | :-------------------------------: |
|   Travis  |         green tea,	t-shirt,	sunglasses,	flip flops             |                ?       | 

You can think of Travis being our test data, and the above six users make our training data.

Proceed as follows:
 - Calculate the similarity of Travis relative to the six users in the training data 
   (done by adding together the number of similar purchases by the users).
 - Having calculated the similarities, identify the user who is most similar to Travis by selecting the largest of the calculated similarities.
 - Predict what Travis is likely to purchase next by looking at the most recent purchase (the rightmost column in the table) of the most similar user from the previous step.
 
Who is the user most similar to Travis?  ---> Ville

When you calculate the similarities between Travis and all the other users,
Ville and Travis will have the largest similarity with a similarity of 3.

What is the predicted purchase for Travis? ---> sunscreen

Since Ville's latest purchase was sunscreen, we will recommend it also to Travis.

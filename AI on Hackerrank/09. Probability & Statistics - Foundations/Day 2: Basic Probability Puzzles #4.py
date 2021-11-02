# Challenge: https://www.hackerrank.com/challenges/basic-probability-puzzles-4

# Reference: https://en.wikipedia.org/wiki/Probability

# Combinations
# Bag1	Bag2	 Bag2
# black	black	 red
# black	red	   black
# red	  black	 black

# We have multiplied the possibilities
first_combination   = (5/9) * (7/10) * (3/9)
second_combination  = (5/9) * (3/10) * (7/9)
third_combination   = (4/9) * (7/10) * (6/9)

# Result = 0.4511111111111111 = 7/15
print (first_combination + second_combination + third_combination)


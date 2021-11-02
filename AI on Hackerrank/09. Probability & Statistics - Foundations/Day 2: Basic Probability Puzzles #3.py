# Challenge: https://www.hackerrank.com/challenges/basic-probability-puzzles-3

# Reference: https://en.wikipedia.org/wiki/Probability

# Combinations
#Urn X	Urn Y 	Urn Z
#red	  red	    black
#black	red	    red
#red	  black 	red

x_prob_red = 4/7
x_prob_black = 3/7

y_prob_red = 5/9
y_prob_black = 4/9

z_prob_red = 1/2
z_prob_black = 1/2

# We have multiplied the possibilities
first_combination   = x_prob_red * y_prob_red * z_prob_black
second_combination  = x_prob_black * y_prob_red * z_prob_red
third_combination   = x_prob_red * y_prob_black * z_prob_red

# Result = 0.40476190476190477 = 17/42
print (first_combination + second_combination + third_combination)


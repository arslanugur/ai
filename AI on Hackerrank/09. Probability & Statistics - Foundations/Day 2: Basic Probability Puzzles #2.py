# Challenge: https://www.hackerrank.com/challenges/basic-probability-puzzles-2

# Reference: https://en.wikipedia.org/wiki/Probability

probability = 1/6
values = 6
result = 0

# First dice
for i in range(1, values + 1):
    # Second dice
    for j in range(1, values + 1):
        # Verify if each die will be different and their sum is 6
        if i != j and (i + j) == 6:
            result += probability ** 2

# Final probability found
print (result)


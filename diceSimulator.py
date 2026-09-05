# Dice & Random Data Simulator
# Simulate 10,000 dice rolls
# Count how many times each number appears
# Calculate probability of each result
# Find the most frequent result
# Simulate two dice
# Calculate their sums
# Find the probability of getting a sum of 7
# Compare experimental probability with theoretical probability

import numpy as np
die1=np.random.randint(1, 7, size=10000)
counts = np.bincount(die1)[1:] #np.bincount counts the number of occurrences of each value in an array of non-negative ints
print(f"Counts of each integer = {counts}")
print(f"Probability of each number = {counts/len(die1)}")
die2=np.random.randint(1,7,size=10000)
sum=die1+die2
print(f"sum of two dice = {sum}")
exp_prov=np.mean(sum==7)
theort_pro= 6/36
print(f"probability of getting sum of 7 ={np.mean(sum==7)}")
difference= exp_prov-theort_pro
print(f"the difference in theoretical probabiliy and experemential probability= {difference}")
# 1. Student Grade Analyzer
# Store student marks in NumPy arrays.
# Calculate average, highest, lowest, median, and standard deviation.
# Find students who scored above the class average.
import numpy as np
name=np.array(['ram', 'shyam', 'hari', 'gita', 'sita', 'laxmi', 'krishna', 'radha', 'arjun', 'bhim'])
arr=np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
average = np.mean(arr)
highest= np.max(arr)
lowest=np.min(arr)
median=np.median(arr)
sd=np.std(arr)

print("-----Grade Analyzer-----")
print(f"Average = {average}")
print(f"Highest = {highest}")
print(f"lowest = {lowest}")
print(f"Median = {median}")
print(f"Standard Deviation = {sd:.2f}")

# Find students who scored above the class average
print(f"Students above average: {name[arr>average]} with marks:{arr[arr>average]}")
#  Temperature Analyzer
# Store daily temperatures in a NumPy array.
# Calculate weekly averages.
# Find the hottest and coldest days.
# Detect days above a chosen temperature.
import numpy as np
days=np.array(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
temperatures=np.array([25, 28, 30, 27, 29, 31, 26])
average= np.mean(temperatures)
print(f"Weekly temperaures = {average}")
hottest=np.max(temperatures)
coldest=np.min(temperatures)
print(f"Hottest day = {days[temperatures==hottest]} with temperature = {hottest}")
print(f"Coldest day = {days[temperatures==coldest]} with temperature = {coldest}")

x= float(input("Enter a temperture"))
print(f"day at temperature {x} = {days[temperatures==x]}")
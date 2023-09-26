'''

ELEC 326 - Group 48

Assignment 1 -> Question 2 🔥🔥🔥🔥💻🧠🤯

Sabrina Button, Luke Major, Julia Dyck, Abby Magno

'''

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load MATLAB files
RV1 = scipy.io.loadmat('C:\\Users\\lukep\\OneDrive\\Serious-Stuff\\3rd-year\\ELEC-326-Probability-and-Random-Processes\\probability_assignments\\assignment1\\\RV1.mat')
RV2 = scipy.io.loadmat('C:\\Users\\lukep\\OneDrive\\Serious-Stuff\\3rd-year\\ELEC-326-Probability-and-Random-Processes\\probability_assignments\\assignment1\\\RV2.mat')
RV3 = scipy.io.loadmat('C:\\Users\\lukep\\OneDrive\\Serious-Stuff\\3rd-year\\ELEC-326-Probability-and-Random-Processes\\probability_assignments\\assignment1\\\RV3.mat')

# Get the RVs from MATLAB files
RV1 = RV1['RV1']
RV2 = RV2['RV2']
RV3 = RV3['RV3']

# Calculate the mean of RVs
def mean(input):
    return np.sum(input)/len(input)

# Calculate the variance of RVs
def variance(input):
    return np.sum((input - mean(input))**2)/len(input)

print("Mean of RV1: ", mean(RV1[0]))
print("Mean of RV2: ", mean(RV2[0]))
print("Mean of RV3: ", mean(RV3[0]))

print("Variance of RV1: ", variance(RV1[0]))
print("Variance of RV2: ", variance(RV2[0]))
print("Variance of RV3: ", variance(RV3[0]))

# Count frequency of each value of RV
def counter(input, min=0, max=None):
    if max is None:
        max = np.max(input)
    H = np.zeros(max - min + 1)
    for i in input:
        H[i - min] += 1
    return H    

# Plot bar chart of RV
def plot(name, H):
    plt.figure()
    plt.bar(np.arange(len(H)), H)
    plt.title(name)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

# Estimate probability of RV landing between 10 and 40
def prob(H, min, max):
    return np.sum(H[min:max+1])/np.sum(H)

# ***** Get values and figures for question 2 using above funtions: *****

# Count frequency of each value of RV
H1 = counter(RV1[0])
H2 = counter(RV2[0])
H3 = counter(RV3[0])

plot("H1", H1)
print("Probability of RV1 between 10 and 40: ", prob(H1, 10, 40))

plot("H2", H2)
print("Probability of RV2 between 10 and 40: ", prob(H2, 10, 40))

plot("H3", H3)
print("Probability of RV3 between 10 and 40: ", prob(H3, 10, 40))
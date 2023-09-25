'''

ELEC 326 - Group 48

Assignment 1 -> Question 2 🔥🔥🔥🔥💻🧠🤯

Sabrina Button, Luke Major, Julia Dyck, Abby Magno

'''

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load MATLAB files
RV1 = scipy.io.loadmat('RV1.mat')
RV2 = scipy.io.loadmat('RV2.mat')
RV3 = scipy.io.loadmat('RV3.mat')

# Get the RVs from MATLAB files
RV1 = RV1['RV1']
RV2 = RV2['RV2']
RV3 = RV3['RV3']

# Count frequency of each value of RV
def counter(trial, outcomes=100, min=0, max=100):
        H = np.zeros(outcomes)
        for i in range(trial.size):
            H[trial[i] - (min + 1) ] += 1

        return H

# Plot bar chart of RV
def plot(name, input, outcomes=100, min=0, max=100):
    H = counter(input, outcomes, min, max)
    plt.figure()
    plt.bar(np.arange(outcomes), H, align='center')
    plt.title(name)
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
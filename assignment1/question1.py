'''

ELEC 326 - Group 48

Assignment 1 -> Question 1 🏎️🏎️🏋️‍♂️🦀🦀

Sabrina Button, Luke Major, Julia Dyck, Abby Magno

'''

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Declare the range of RVs
x = np.arange(1,7)
y = np.arange(3,19) # y is the RV sum of three dice rolls

# Print RVs as a test
print("RV x: ", x)
print("RV y: ", y)

# Function for quickly making plots
def plot(name, x, y, y_label):
    plt.figure()
    plt.bar(x, y, align='center')
    plt.title(name)
    plt.ylabel(y_label)
    plt.show()

# PMF of y
def PMF_of_y(y, num_rolls, num_sides=6):
    # Number of elements in PMF is cardinality of y
    pmf = np.zeros(y.size)
    denominator = num_sides**num_rolls
    print(denominator)

    for i in range(y.size):
        # Figure out how many ways we can get y[i] with num_rolls dice
        # This is the numerator of the PMF
        numerator = 0
        for j in range(1, num_sides+1):
            for k in range(1, num_sides+1):
                for l in range(1, num_sides+1):
                    if j+k+l == y[i]:
                        numerator += 1

        pmf[i] = numerator/denominator

    return pmf

# PMF for y
def PMF_of_x(x, num_sides=6):
    # Number of elements in PMF is cardinality of x
    pmf = np.zeros(x.size)
    
    for i in range(x.size):
        pmf[i] = 1/num_sides

    return pmf

# PMF for y
def CDF_of_y(y, num_rolls, num_sides=6):
    # Number of elements in CDF is cardinality of y
    cdf = np.zeros(y.size)
    denominator = num_sides**num_rolls

    # iterate through possible sums and find all methods of getting that sum
    for i in range(y.size):
        # Figure out how many ways we can get y[i] with num_rolls dice
        # This is the numerator of the CDF
        numerator = 0
        for j in range(1, num_sides+1):
            for k in range(1, num_sides+1):
                for l in range(1, num_sides+1):
                    if j+k+l <= y[i]:
                        # If this adds to our desired value, that means there's one more
                        # way to get that value, so increment numerator
                        numerator += 1

        cdf[i] = numerator/denominator

    return cdf

def CDF_of_x(x):
    # Number of elements in CDF is cardinality of x
    cdf = np.zeros(x.size)

    for i in range(x.size):
        cdf[i] = (i+1)/6

    return cdf

def do_trials(num):
    # Try 100 dice rolls for each
    rng = np.random.default_rng()
    x1 = rng.integers(low=1, high=7, size=(num))
    x2 = rng.integers(low=1, high=7, size=(num))
    x3 = rng.integers(low=1, high=7, size=(num))

    # Store sum of three rolls in y_out
    y_out = np.sum([x1, x2, x3], axis=0)

    # print all variables
    print("x1: ", x1)
    print("x2: ", x2)
    print("x3: ", x3)
    print("y: ", y_out)

    # Count frequency of each value of RV
    def counter(trial, outcomes=6, min=1, max=6):
        H = np.zeros(outcomes)
        for i in range(trial.size):
            H[trial[i] - (min) ] += 1

        return H

    # Count frequency of each value of RV
    H1 = counter(x1)
    H2 = counter(x2)
    H3 = counter(x3)

    # plot H1, H2, H3 on one bar chart
    plt.figure()
    plt.bar(np.arange(1,7), H1, align='center')
    plt.bar(np.arange(1,7), H2, align='center')
    plt.bar(np.arange(1,7), H3, align='center')
    plt.title("H1, H2, H3")
    plt.xlabel("x")
    plt.ylabel("Frequency")
    plt.show()

    # Try dividing H1 by N=100
    H1 = np.divide(H1, num)
    # plot H1/N as a bar chrt
    plot("H1/N", x, H1, "Probability")

    H = counter(y_out, outcomes=16, min=3, max=18)
    # plot H as bar chart
    plot("H", y, H, "Frequency")

# ***** Get values and figures for question 1 using above funtions: *****

# I) plot pmf of y as bar chart
plot("PMF of RV y", y, PMF_of_y(y, 3), "Probability")

# I) plot pmf of x as bar chart
plot("PMF of RV x", x, PMF_of_x(x), "Probability")

# II) plot cdf of y as bar chart
plot("CDF of RV y", y, CDF_of_y(y, 3), "Probability")

# II) plot cdf of x as bar chart
plot("CDF of RV x", x, CDF_of_x(x), "Probability")

# III-V) Do 100 trials
do_trials(100)

# V) Do 1000000 trials
do_trials(1000000)
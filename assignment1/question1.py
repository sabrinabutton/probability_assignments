import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Part a, find PMFs

x = np.arange(1,7)
y = np.arange(3,19) # y is the RV sum of three dice rolls

print("RV x: ", x)
print("RV y: ", y)

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

def PMF_of_x(x):
    # Number of elements in PMF is cardinality of x
    pmf = np.zeros(x.size)

    for i in range(x.size):
        pmf[i] = 1/6

    return pmf

# plot pmf of y as bar chart
plt.figure(1)
plt.bar(y, PMF_of_y(y, 3), align='center')
plt.title("PMF of RV y")
plt.xlabel("y")
plt.ylabel("Probability")
plt.show()

# plot pmf of x as bar graph
plt.figure(2)
plt.bar(x, PMF_of_x(x), align='center')
plt.title("PMF of RV x")
plt.xlabel("x")
plt.ylabel("Probability")
plt.show()

# Part b, now find the CDF of each var.

def CDF_of_y(y, num_rolls, num_sides=6):
    # Number of elements in CDF is cardinality of y
    cdf = np.zeros(y.size)
    denominator = num_sides**num_rolls

    for i in range(y.size):
        # Figure out how many ways we can get y[i] with num_rolls dice
        # This is the numerator of the CDF
        numerator = 0
        for j in range(1, num_sides+1):
            for k in range(1, num_sides+1):
                for l in range(1, num_sides+1):
                    if j+k+l <= y[i]:
                        numerator += 1

        cdf[i] = numerator/denominator

    return cdf

def CDF_of_x(x):
    # Number of elements in CDF is cardinality of x
    cdf = np.zeros(x.size)

    for i in range(x.size):
        cdf[i] = (i+1)/6

    return cdf

# plot cdf of y as bar chart
plt.figure(3)
plt.bar(y, CDF_of_y(y, 3), align='center')
plt.title("CDF of RV y")
plt.xlabel("y")
plt.ylabel("Probability")
plt.show()

# plot cdf of x as bar graph
plt.figure(4)
plt.bar(x, CDF_of_x(x), align='center')
plt.title("CDF of RV x")
plt.xlabel("x")
plt.ylabel("Probability")
plt.show()




def do_trials(num):
    # Try 100 dice rolls for each
    rng = np.random.default_rng()
    x1 = rng.integers(low=1, high=7, size=(num))
    x2 = rng.integers(low=1, high=7, size=(num))
    x3 = rng.integers(low=1, high=7, size=(num))

    y_out = np.sum([x1, x2, x3], axis=0)

    # print all variables
    print("x1: ", x1)
    print("x2: ", x2)
    print("x3: ", x3)
    print("y: ", y_out)

    def counter(trial, outcomes=6, min=1, max=6):
        H = np.zeros(outcomes)
        for i in range(trial.size):
            H[trial[i] - (min) ] += 1

        return H

    H1 = counter(x1)
    H2 = counter(x2)
    H3 = counter(x3)

    # plot H1, H2, H3 as bar charts
    plt.figure(5)
    plt.bar(np.arange(1,7), H1, align='center')
    plt.bar(np.arange(1,7), H2, align='center')
    plt.bar(np.arange(1,7), H3, align='center')
    plt.title("Histogram of RV H1, H2, H3")
    plt.xlabel("x1")
    plt.ylabel("Frequency")
    plt.show()

    # Try dividing H1 by N=100
    H1 = np.divide(H1, num)
    # plot this
    plt.figure(6)
    plt.bar(np.arange(1,7), H1, align='center')
    plt.title("Histogram of RV H1/N")
    plt.xlabel("x1")
    plt.ylabel("Probability")
    plt.show()

    H = counter(y_out, outcomes=16, min=3, max=18)
    # plot H as bar chart
    plt.figure(7)
    plt.bar(np.arange(3,19), H, align='center')
    plt.title("Histogram of RV H")
    plt.xlabel("y")
    plt.ylabel("Frequency")
    plt.show()

do_trials(1000000)
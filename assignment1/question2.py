import scipy.io
import numpy as np

# Load MATLAB file
RV1 = scipy.io.loadmat('RV1.mat')
RV2 = scipy.io.loadmat('RV2.mat')
RV3 = scipy.io.loadmat('RV3.mat')

# Get the RVs
RV1 = RV1['RV1']
RV2 = RV2['RV2']
RV3 = RV3['RV3']

# Print to test
print("RV1: ", RV1)

def counter(trial, outcomes=100, min=0, max=100):
        H = np.zeros(outcomes)
        for i in range(trial.size):
            H[trial[i] - (min + 1) ] += 1

        return H

H1 = counter(RV1[0])
H2 = counter(RV2[0])
H3 = counter(RV3[0])

# pLOT
import matplotlib.pyplot as plt
plt.figure(1)
plt.bar(np.arange(100), H1, align='center')
plt.title("H1")
plt.ylabel("Frequency")
plt.show()

plt.figure(2)
plt.bar(np.arange(100), H2, align='center')
plt.title("H2")
plt.ylabel("Frequency")
plt.show()

plt.figure(3)
plt.bar(np.arange(100), H3, align='center')
plt.title("H3")
plt.ylabel("Frequency")
plt.show()

# Estimate probability of RV landing between 10 and 40
def prob(H, min, max):
    return np.sum(H[min:max+1])/np.sum(H)

print("Probability of RV1 between 10 and 40: ", prob(H1, 10, 40))
print("Probability of RV2 between 10 and 40: ", prob(H2, 10, 40))
print("Probability of RV3 between 10 and 40: ", prob(H3, 10, 40))
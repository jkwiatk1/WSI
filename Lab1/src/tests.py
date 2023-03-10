'''
WSI Laboratorium 1
@author Jan Kwiatkowski
'''
import random
import time
import gc
import numpy as np
import matplotlib.pyplot as plt
from SteepestGradientDescent import stochastic_gradient_descent
from NewtonMethod import newtons_method

workTimes_SGD = []
workIters_SGD = []

workTimes_NM = []
workIters_NM = []

experimentSize = 25
Beta = 0.01
MaxIter = 100000
Eps = 1e-12

def SGD_timeCount(x0,y0):
    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()  # wyłącz odśmiecanie
    start = time.process_time()  # pobierz aktualny czas
    xminSGD, yminSGD, fminSGD, iterNumSGD = stochastic_gradient_descent(x0, y0, Beta, MaxIter, Eps)
    stop = time.process_time()
    time_list = stop-start
    if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
    return xminSGD, yminSGD, fminSGD, iterNumSGD, time_list

def SGD_timeCount(x0, y0):
    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()  # wyłącz odśmiecanie
    start = time.process_time()  # pobierz aktualny czas
    xminNM, yminNM, fminNM, iterNumNM = newtons_method(x0, y0, Beta, MaxIter, Eps)
    stop = time.process_time()
    time_list = stop-start
    if gc_old: gc.enable() # przywróć pierwotny stan odśmiecania
    return xminNM, yminNM, fminNM, iterNumNM, time_list


for i in range(experimentSize):
    x0 = random.uniform(-5, 5)
    y0 = random.uniform(-5, 5)
    xminSGD, yminSGD, fminSGD, iterNumSGD, timeSGD = SGD_timeCount(x0, y0)
    xminNM, yminNM, fminNM, iterNumNM, timeNM = SGD_timeCount(x0, y0)
    drawnPointsSGD = np.array([x0, y0])
    bestPointSGD = np.array([xminSGD, yminSGD])
    bestPoinsNM = np.array([xminNM, yminNM])
    workTimes_SGD.append(timeSGD)
    workIters_SGD.append(iterNumSGD)
    workTimes_NM.append(timeNM)
    workIters_NM.append(iterNumNM)
    print("------------------------------------------------------------------")
    print("TEST nb: ", i, end = " ")
    print("and starting points [x,y] = ", drawnPointsSGD)
    print()
    print("Stochastic gradient descent")
    print("Minimum at: ", bestPointSGD)
    print("Minimum value =", fminSGD)
    print("Number of iterations =", iterNumSGD)
    print("Counting time: ", timeSGD)
    print()
    print("Newton's Method")
    print("Minimum at: ", bestPoinsNM)
    print("Minimum value =", fminNM)
    print("Number of iterations =", iterNumNM)
    print("Counting time: ", timeNM)
    print()
    print()

plt.plot(range(experimentSize), workTimes_SGD,'*-r', label = "Stochastic gradient descent")
plt.plot(range(experimentSize), workTimes_NM,'*-g', label = "Newton's method")
plt.legend(loc="upper left")

plt.xlabel('Experiment number')
plt.ylabel('Time [s]')
plt.title('Working time of each method')

# Show the plot
plt.show()

plt.plot(range(experimentSize), workIters_SGD,'*-r', label = "Stochastic gradient descent")
plt.plot(range(experimentSize), workIters_NM,'*-g', label = "Newton's method")
plt.legend(loc="upper left")

plt.xlabel('Experiment number')
plt.ylabel('Number of iterations ')
plt.title('Number of iterantions for each method')

# Show the plot
plt.show()


# Add axis labels and a title
plt.hist(workTimes_SGD, bins=experimentSize, alpha=0.5, label="Stochastic gradient descent")
plt.hist(workTimes_NM, bins=experimentSize, alpha=0.5, label="Newton's method")
plt.legend(loc="upper left")
plt.xlabel('Working time of each method')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
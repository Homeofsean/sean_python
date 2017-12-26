# testing vs cde
"""
This is sean testing the vs code to get it to generate a graph out put

I made chanegs
"""
import numpy as np
import matplotlib.pyplot as plt

XAXIS = np.linspace(0, 2 * np.pi, 1000)
YAXIS = np.sin(XAXIS)
plt.plot(XAXIS, YAXIS)
plt.show()

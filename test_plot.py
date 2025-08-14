import matplotlib.pyplot as plt
import numpy as np


x_values = np.linspace(0, 5, 50)
y_values = x_values * x_values
plt.plot(x_values, y_values)
plt.show()

print("Script is now done")
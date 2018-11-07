import matplotlib.pyplot as plt
import pandas as pd

# Create a dataset:
x = range(-100,101)
y = [i*i*i for i in range(-100,101)]

df = pd.DataFrame({'x': x, 'y': y})

# plot
plt.plot('x', 'y', data=df, linestyle='none', marker='o')
plt.savefig('Visualization.png')

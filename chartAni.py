import matplotlib
matplotlib.use('TkAgg')  # Ensures GUI backend for PyCharm

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

# Data
subjects = ['Python', 'AI', 'UI/UX', 'Accounting', 'Business']
hours = [10, 8, 6, 4, 2]

# Bar positions and dimensions
x = np.arange(len(subjects)) * 1.2  # spacing between bars
y = np.zeros(len(subjects))         # dummy y-axis
z = np.zeros(len(subjects))         # base of bars
dx = np.ones(len(subjects))         # bar width
dy = np.ones(len(subjects))         # bar depth
colors = ['red', 'green', 'blue', 'orange', 'purple']

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Animation function
def update(frame):
    ax.clear()
    dz = [min(h, frame) for h in hours]  # grow each bar up to its target height

    # Draw bars
    ax.bar3d(x, y, z, dx, dy, dz, color=colors)

    # Label axes and title
    ax.set_xticks(x)
    ax.set_xticklabels(subjects)
    ax.set_xlabel('Subjects')
    ax.set_ylabel('Y (dummy)')
    ax.set_zlabel('Study Hours')
    ax.set_title('Animated 3D Bar Chart of Weekly Study Hours')

# Run animation slowly (500ms per frame)
ani = FuncAnimation(fig, update, frames=range(0, max(hours)+1), interval=500)
plt.show()


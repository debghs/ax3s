import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to simulate the data stream
def get_data_stream():
    # Replace this with your data stream reading logic
    while True:
        vx = np.random.random() * 2 - 1  # random velocity between -1 and 1
        vy = np.random.random() * 2 - 1
        vz = np.random.random() * 2 - 1
        ax = np.random.random() * 2 - 1  # random acceleration between -1 and 1
        ay = np.random.random() * 2 - 1
        az = np.random.random() * 2 - 1
        yield vx, vy, vz, ax, ay, az

# Initialize data lists
x_data, y_data, z_data = [0], [0], [0]  # Starting at the origin
vx, vy, vz = 0, 0, 0  # Initial velocities
dt = 0.1  # Time step

# Create the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.ion()
fig.show()

# Flag to control the loop
running = True

# Function to handle the window close event
def on_close(event):
    global running
    running = False

# Connect the figure to the close event
fig.canvas.mpl_connect('close_event', on_close)

try:
    for vx_new, vy_new, vz_new, ax_val, ay_val, az_val in get_data_stream():
        if not running:
            break
        # Update velocities
        vx += ax_val * dt
        vy += ay_val * dt
        vz += az_val * dt

        # Update positions
        x_data.append(x_data[-1] + vx * dt)
        y_data.append(y_data[-1] + vy * dt)
        z_data.append(z_data[-1] + vz * dt)

        ax.clear()
        ax.plot(x_data, y_data, z_data)
        plt.draw()
        plt.pause(3)
except KeyboardInterrupt:
    pass
finally:
    plt.ioff()
    plt.show()

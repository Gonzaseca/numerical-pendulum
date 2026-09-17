import numpy as np
from src.pendulum import Pendulum
from src.solvers import euler, euler_cromer, solve_with_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

pendulum = Pendulum(np.pi / 6, 0, 9.8, 1, 1)
time = np.linspace(0,20,1000)

angle, angular_velocity = solve_with_ivp(pendulum, time)

x_coordinate = pendulum.length * np.sin(angle)
y_coordinate = -pendulum.length *np.cos(angle)

fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 0.2)
pendulum_string, =ax.plot([], [])
pendulum_bob, =ax.plot([], [], 'o')
pendulum_trayectory, =ax.plot([], [])
time_display = ax.text(-1, 0, "")
def update(i):
    pendulum_string.set_data([0, x_coordinate[i]], [0, y_coordinate[i]])
    pendulum_bob.set_data([x_coordinate[i]], [y_coordinate[i]])
    pendulum_trayectory.set_data([x_coordinate[:i]], [y_coordinate[:i]])
    time_display.set_text(f"Time = {time[i]:.2f} s")
animation = FuncAnimation(
    fig,
    update,
    frames = (len(x_coordinate)),
    interval = 20
)

animation.save("animations/pendulum_animation.gif", writer = PillowWriter(fps=30))
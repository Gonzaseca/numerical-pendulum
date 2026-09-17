import numpy as np 
from src.pendulum import Pendulum
from src.solvers import euler_cromer, euler, solve_with_ivp
import matplotlib.pyplot as plt

pendulum = Pendulum(np.pi/6, 0, 9.8, 1, 1)
time = np.linspace(0, 20, 1000)

euler_angle, euler_angular_velocity = euler(pendulum, time)
euler_cromer_angle, euler_cromer_angular_velocity = euler_cromer(pendulum, time)
ivp_angle, ivp_angular_velocity = solve_with_ivp(pendulum, time)

fig, ax = plt.subplots()
ax.plot(time, euler_angle, label = "Euler")
ax.plot(time, euler_cromer_angle, label = "Euler-Cromer")
ax.plot(time, ivp_angle, label = "IVP")
ax.legend()
ax.set_xlabel("Time (s)")
ax.set_ylabel("Angle (rad)")
ax.set_title("Pendulum angle: solver comparison")
ax.grid()
fig.tight_layout()
fig.savefig("figures/angle_comparison.png")
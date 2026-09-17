import numpy as np 
from src.pendulum import Pendulum
from src.solvers import euler_cromer, euler, solve_with_ivp
import matplotlib.pyplot as plt

pendulum = Pendulum(np.pi/6, 0, 9.8, 1, 1)
time = np.linspace(0, 20, 1000)

euler_angle, euler_angular_velocity = euler(pendulum, time)
euler_cromer_angle, euler_cromer_angular_velocity = euler_cromer(pendulum, time)
ivp_angle, ivp_angular_velocity = solve_with_ivp(pendulum, time)

euler_energy = [] 
euler_cromer_energy = []
ivp_energy = []

#Computes the mechanical energy at each time step
for i in range(len(time)):
    energy = pendulum.energy(euler_angle[i], euler_angular_velocity[i])
    euler_energy.append(energy)

    energy = pendulum.energy(euler_cromer_angle[i], euler_cromer_angular_velocity[i])
    euler_cromer_energy.append(energy)

    energy = pendulum.energy(ivp_angle[i], ivp_angular_velocity[i])
    ivp_energy.append(energy)

fig, ax = plt.subplots()
ax.plot(time, euler_energy, label = "Euler")
ax.plot(time, euler_cromer_energy, label = "Euler-Cromer")
ax.plot(time, ivp_energy, label = "IVP")
ax.legend()
ax.set_xlabel("Time (s)")
ax.set_ylabel("Energy (J)")
ax.set_title("Pendulum energy: solver comparison")
ax.grid()
fig.tight_layout()
fig.savefig("figures/energy_comparison.png")

fig, ax = plt.subplots()
ax.plot(time, euler_energy, label = "Euler")
ax.plot(time, euler_cromer_energy, label = "Euler-Cromer")
ax.plot(time, ivp_energy, label = "IVP")
ax.set_xlim(0, 2)
ax.set_ylim(1.2, 1.5)
ax.legend()
ax.set_xlabel("Time (s)")
ax.set_ylabel("Energy (J)")
ax.set_title("Pendulum energy: solver comparison")
ax.grid()
fig.tight_layout()
fig.savefig("figures/energy_comparison_detail.png")



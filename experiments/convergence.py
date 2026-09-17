import numpy as np
from src.pendulum import Pendulum
from src.solvers import euler, euler_cromer, solve_with_ivp
import matplotlib.pyplot as plt

pendulum = Pendulum(np.pi/6, 0, 9.8, 1, 1)
number_of_steps = [100, 500, 1000, 5000, 10000]
dt_list = []
euler_rms_errors = []
euler_cromer_rms_errors = []

for i in number_of_steps:
    time = np.linspace(0, 20, i+1)
    dt = time[1] - time[0]
    dt_list.append(dt)

    euler_angle, euler_angular_velocity = euler(pendulum, time)
    euler_cromer_angle, euler_cromer_angular_velocity = euler_cromer(pendulum, time)
    ivp_angle, ivp_angular_velocity = solve_with_ivp(pendulum, time)

    euler_rms_error = np.sqrt((1/len(time))*np.sum((euler_angle-ivp_angle)**2))
    euler_cromer_rms_error = np.sqrt((1/len(time))*np.sum((euler_cromer_angle-ivp_angle)**2))
    euler_rms_errors.append(euler_rms_error)
    euler_cromer_rms_errors.append(euler_cromer_rms_error)

euler_orders = []
euler_cromer_orders = []

for i in range((len(dt_list)-1)):
    p_euler = np.log(
        euler_rms_errors[i] / euler_rms_errors[i+1]
    ) / np.log(dt_list[i] / dt_list[i+1]
    )

    euler_orders.append(p_euler)

    p_euler_cromer = np.log(
            euler_cromer_rms_errors[i] / euler_cromer_rms_errors[i+1]
        ) / np.log(dt_list[i] / dt_list[i+1]
        )

    euler_cromer_orders.append(p_euler_cromer)

reference_dt = np.array(dt_list)

euler_cromer_reference_constant = euler_cromer_rms_errors[0] / dt_list[0]
euler_cromer_reference_error = euler_cromer_reference_constant * reference_dt

fig, ax = plt.subplots()
ax.loglog(dt_list, euler_rms_errors, marker = "o", label = "Euler RMS")
ax.loglog(dt_list, euler_cromer_rms_errors, marker = "o", label = "Euler-Cromer RMS")
ax.loglog(reference_dt, euler_cromer_reference_error, linestyle = "--", label = "Reference: p = 1")
ax.set_xlabel("Time step (dt)")
ax.set_ylabel("RMS Error")
ax.set_title("RMS error vs Time steps")
ax.grid()
ax.legend()
fig.savefig("figures/error_comparative.png")
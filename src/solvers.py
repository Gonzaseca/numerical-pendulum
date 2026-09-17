import numpy as np
from src.pendulum import Pendulum
from scipy.integrate import solve_ivp

def euler_cromer(pendulum,time):
    angle = [pendulum.initial_angle]
    angular_velocity = [pendulum.initial_angular_velocity]
    dt = time[1] - time[0]
    for i in range(len(time)-1):
        angle_derivative, angular_velocity_derivative = pendulum.derivatives(angle[i], angular_velocity[i])
        new_angular_velocity = angular_velocity[i] + angular_velocity_derivative*dt
        angular_velocity.append(new_angular_velocity)
        new_angle = angle[i] + new_angular_velocity*dt
        angle.append(new_angle)

    return angle, angular_velocity

def euler(pendulum,time):
    angle = [pendulum.initial_angle]
    angular_velocity = [pendulum.initial_angular_velocity]
    dt = time[1] - time[0]
    for i in range(len(time)-1):
        angle_derivative, angular_velocity_derivative = pendulum.derivatives(angle[i], angular_velocity[i])
        new_angular_velocity = angular_velocity[i] + angular_velocity_derivative*dt
        angular_velocity.append(new_angular_velocity)
        new_angle = angle[i] + angular_velocity[i]*dt
        angle.append(new_angle)

    return angle, angular_velocity

def solve_with_ivp(pendulum,time):

    y0 = pendulum.initial_angle, pendulum.initial_angular_velocity

    def derivatives_for_ivp(t,y):
        angle = y[0]
        angular_velocity = y[1]

        return pendulum.derivatives(angle, angular_velocity)

    #Use strict tolerances to obtain an accurate reference solution
    sol = solve_ivp(
        derivatives_for_ivp,
        (time[0],time[-1]),
        y0,
        t_eval = time,
        rtol = 1e-10,
        atol = 1e-12

    )
    angle = sol.y[0]
    angular_velocity = sol.y[1]

    return angle, angular_velocity
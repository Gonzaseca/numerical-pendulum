import numpy as np 
from src.pendulum import Pendulum
from src.solvers import euler_cromer, euler, solve_with_ivp

pendulum = Pendulum(np.pi / 6, 0, 9.8, 1, 1)
time = np.linspace(0,20,1000)

#The following functions check the correct behaviour of pendulum model and solvers using pytest
def test_euler():
    euler_angle, euler_angular_velocity = euler(pendulum, time)

    assert euler_angle[0] == pendulum.initial_angle
    assert euler_angular_velocity[0] == pendulum.initial_angular_velocity

    assert len(euler_angle) == len(time)
    assert len(euler_angular_velocity) == len(time)

def test_euler_cromer():
    euler_cromer_angle, euler_cromer_angular_velocity = euler_cromer(pendulum, time)

    assert euler_cromer_angle[0] == pendulum.initial_angle
    assert euler_cromer_angular_velocity[0] == pendulum.initial_angular_velocity

    assert len(euler_cromer_angle) == len(time)
    assert len(euler_cromer_angular_velocity) == len(time)

def test_derivatives():
    angle_derivative,angular_velocity_derivative = pendulum.derivatives(
    pendulum.initial_angle,
    pendulum.initial_angular_velocity
    )
    assert np.isclose(angle_derivative, pendulum.initial_angular_velocity)
    assert np.isclose(angular_velocity_derivative, -(pendulum.gravity/pendulum.length*np.sin(pendulum.initial_angle)))

def test_energy():
    initial_energy = pendulum.energy(
    pendulum.initial_angle,
    pendulum.initial_angular_velocity
    )

    expected_energy = ((1/2)*pendulum.mass*(pendulum.length*pendulum.initial_angular_velocity)**2  
                    + pendulum.mass*pendulum.gravity*pendulum.length
                    * (1 - np.cos(pendulum.initial_angle)))
    assert np.isclose(initial_energy, expected_energy)

def test_solve_with_ivp():
    solve_with_ivp_angle, solve_with_ivp_angular_velocity = solve_with_ivp(pendulum, time)
    
    assert solve_with_ivp_angle[0] == pendulum.initial_angle
    assert solve_with_ivp_angular_velocity[0] == pendulum.initial_angular_velocity
    
    assert len(solve_with_ivp_angle) == len(time)
    assert len(solve_with_ivp_angular_velocity) == len(time)

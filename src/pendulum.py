import numpy as np 

class Pendulum:
    def __init__(self, initial_angle, initial_angular_velocity, gravity, length,mass):
        self.initial_angle = initial_angle
        self.initial_angular_velocity = initial_angular_velocity
        self.gravity = gravity
        self.length = length
        self.mass=mass

    def derivatives(self, angle, angular_velocity):
        dtheta_dt=angular_velocity
        domega_dt=-(self.gravity/self.length*np.sin(angle))

        return dtheta_dt,domega_dt
    def energy(self, angle,angular_velocity):
        energy = (
            (1 / 2) * self.mass * (self.length*angular_velocity)**2 + self.mass * self.gravity * self.length * (1-np.cos(angle))
        )

        return energy
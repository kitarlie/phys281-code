"""

Contains the Particle class on which every body is modelled.

"""

import numpy as np

class Particle:
    """

    Models a body moving under a variable gravitational force as a particle.

        Attributes:
            name (str): The name of the body.

            mass (float): The mass of the body.

            radius (float): The radius of the body.

            position (list-like): The current 3-position of the body relative to the coordinate origin.

            velocity (list-like): The current 3-velocity of the body.

            acceleration (list-like): The current 3-acceleration of the body.

            colour (str): The colour of the body as a hexadecimal code.

            G (float): The gravitational constant.

        Methods:
            algorithm_choice(deltaT, system, algorithm): Activates one of the approximation algorithms based on the user choice.

            euler(deltaT): Updates the position and velocity using the Euler method.

            euler_cromer(deltaT): Updates the position and velocity using the Euler-Cromer method.

            euler_richardson(deltaT, system): Updates the position and velocity using the Euler-Richardson method.

            update_gravitational_acceleration(system): Updates the gravitational acceleration

            calculate_kinetic_energy(): Calculates and returns the current kinetic energy.

            calculate_potential_energy(): Calculates and returns the current gravitational potential energy.

            calculate_linear_momentum(): Calculates and returns the current linear momentum.

            calculate_angular_momentum(): Calculates and returns the current angular momentum.


    """

    def __init__(
        self,
        name = 'Ball',
        mass = 1.0,
        radius = 0.0,
        position = np.array([0, 0, 0], dtype=float),
        velocity = np.array([0, 0, 0], dtype=float),
        acceleration = np.array([0, 0, 0], dtype=float),
        colour =  'ffffff',
    ):

        """

        Initialises a new Particle instance.

        """

        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = np.array(position.copy(), dtype = float)
        self.velocity = np.array(velocity.copy(), dtype = float)
        self.acceleration = np.array(acceleration.copy(), dtype = float)
        self.colour = colour
        self.G = 6.67408E-11

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass,self.position, self.velocity, self.acceleration
            )

    def algorithm_choice(self, deltaT, system, algorithm):
        """

        Activates one of the approximation algorithms based on the user choice.

            Parameters:
                deltaT (int/float): The time interval across which the particle moves.

                system(list-like): Contains all Particle instances defined for the system.

                algorithm (int): A numerical representation of which approximation algorithm is used.


        """
        if algorithm == 1:
            self.euler(deltaT)

        elif algorithm == 2:
            self.euler_cromer(deltaT)

        elif algorithm == 3:
            self.euler_richardson(deltaT, system)


    def euler(self, deltaT):
        """
        
        Updates the position and velocity of the particle using the Euler algorithm.

            Parameters:
                deltaT (int/float): The time interval across which the particle moves.

        """
        self.position += self.velocity * deltaT
        self.velocity += self.acceleration * deltaT
    
    def euler_cromer(self, deltaT):
        """
        
        Updates the position and velocity of the particle using the Euler-Cromer algorithm.

            Parameters:
                deltaT (int/float): The time interval across which the particle moves.

        """
        self.position += self.velocity * deltaT
        self.velocity += self.acceleration * deltaT

    def euler_richardson(self, deltaT, system):
        """
        
        Updates the position and velocity of the particle using a modified Euler-Richardson algorithm.

            Parameters:
                deltaT (int/float): The time interval across which the particle moves.

        """

        #Estimates the midpoint velocity and position
        v_mid = self.velocity + 0.5*(self.acceleration * deltaT)
        r_mid = self.position + 0.5*(self.velocity * deltaT)

        #Calulates the midpoint acceleration

        #The set of the accelerations due to each body.
        a_mid = 0

        #Loops across all bodies in the system
        for body in system:
            #Removes the mass currently being considered from the total acceleration
            if body.name == self.name:
                pass

            else:
                #The vector displacement between the two bodies
                vectorDisplacement = body.position - r_mid

                #The magnitude of the displacement
                scalarDisplacement = np.linalg.norm(vectorDisplacement)

                #Adds the acceleration due to the body
                a_mid += (self.G * body.mass * vectorDisplacement / (scalarDisplacement**3))


        self.velocity += a_mid * deltaT
        self.position += v_mid * deltaT

    def update_gravitational_acceleration(self, system):
        """
        
        Calculates the acceleration of the particle by superposing the accelerations due to all bodies in the system.

            Parameters:
                system(list-like): Contains all Particle instances defined for the system.

        """
        #The sum of the accelerations due to each body.
        self.acceleration = 0

        #Loops across all bodies in the system
        for body in system:
            #Removes the mass currently being considered from the total acceleration
            if body.name == self.name:
                pass

            else:
                #The vector displacement between the two bodies
                vectorDisplacement = body.position - self.position
                #The magnitude of the displacement
                scalarDisplacement = np.sqrt(np.sum(vectorDisplacement**2))

                #Adds the acceleration due to the body
                self.acceleration += (self.G * body.mass * vectorDisplacement / (scalarDisplacement**3))


    def calculate_kinetic_energy(self):
        """

        Calculates the kinetic energy of the particle.

            Returns:
                kineticEnergy (float): The kinetic energy of the particle.

        """
        return(0.5 * self.mass * (np.sum(self.velocity**2)))

    
    def calculate_potential_energy(self, system):
        """

        Calculates the potential energy of the particle.

            Parameters:
                system (list-like): 

        """

        potentialEnergy = 0

        for body in system:
            if self.name != body.name:
                potentialEnergy += (self.G * self.mass * body.mass)/(np.linalg.norm(self.position - body.position))

        return potetialEnergy


    def calculate_linear_momentum(self):
        """

        Calculates the angular momentum of the particle as a vector.

            Returns:
                angularMomentum (list-like): The angular momentum of the particle as a 3-vector.

        """
        return(self.mass * self.velocity)

    def calculate_angular_momentum(self):
        """

        Calculates the angular momentum of the particle as a vector.

            Returns:
                angularMomentum (list-like): The angular momentum of the particle as a 3-vector.

        """
        return(self.mass * np.cross(self.position, self.velocity))
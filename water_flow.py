

def water_column_height(tower_height, tank_height):

    """  
    h = t + 3w/4
    where
    h is height of the water column
    t is the height of the tower
    w is the height of the walls of the tank that is on top of the tower
    """

def pressure_gain_from_water_height(height):
    """
    P = ρgh/1000

    where
    P is the pressure in kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
    g is the acceleration from Earths gravity (9.80665 meter / second2)
    h is the height of the water column in meters
    """


def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    
    """
    P = -(f*L*p*v**2)/2000*d

    where
    P is the lost pressure in kilopascals
    f is the pipe’s friction factor
    L is the length of the pipe in meters
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second
    d is the diameter of the pipe in meters
    """

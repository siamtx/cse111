
# Calculate the water column height with this formula
# h = t + (3*w/4)
# h is height of the water column
# t is the height of the tower
# w is the height of the walls of the tank that is on 
# top of the tower
def water_column_height(tower_height, tank_height):
    height = tower_height + 3*tank_height/4

    return height

 
# Calculates pressure gain useing the following info
#     P = ρgh/1000
# P is the pressure in kilopascals
# ρ is the density of water (998.2 kilogram / meter3)
# g is the acceleration from Earths gravity (9.80665 meter / second2)
# h is the height of the water column in meters
def pressure_gain_from_water_height(height):    
    d = 998.2
    g = 9.80665

    pressure = d*g*height/1000

    return pressure
 
# Calculates pressure loss
# P is the lost pressure in kilopascals
# f is the pipe’s friction factor
# L is the length of the pipe in meters
# ρ is the density of water (998.2 kilogram / meter3)
# v is the velocity of the water flowing through the pipe in meters / second
# d is the diameter of the pipe in meters
def pressure_loss_from_pipe(pipe_diameter,
    pipe_length, friction_factor, fluid_velocity):

    pressure_loss = (-friction_factor * pipe_length * 998.2 * fluid_velocity**2) / (2000 * pipe_diameter)

    return pressure_loss
    

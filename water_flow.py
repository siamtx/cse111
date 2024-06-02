import water_constants as const

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
def pressure_gain_from_water_height(height, ):    
   
    return (height * const.WATER_DENSITY * const.EARTH_ACCELERATION_OF_GRAVITY / 1000)
 
# Calculates pressure loss
# P is the lost pressure in kilopascals
# f is the pipe’s friction factor
# L is the length of the pipe in meters
# ρ is the density of water (998.2 kilogram / meter3)
# v is the velocity of the water flowing through the pipe in meters / second
# d is the diameter of the pipe in meters
def pressure_loss_from_pipe(diameter, length1, friction, velocity):

    loss = -(friction * length1 * const.WATER_DENSITY * velocity**2) / (2000 * diameter)

    return loss

"""
Write a function named pressure_loss_from_fittings that calculates
the water pressure lost because of fittings such as 45° and 90° 
bends that are in a pipeline.

P = -(0.04*p*v**2*n)/2000
where
P is the lost pressure in kilopascals
ρ is the density of water (998.2 kilogram / meter3)
v is the velocity of the water flowing through the pipe in meters / second
n is the quantity of fittings

"""
def pressure_loss_from_fittings(velocity, quantity_angles):
    loss = (-0.04 * const.WATER_DENSITY * velocity**2 * quantity_angles)/2000

    return loss

"""
R = ρdv/μ
where
R is the Reynolds number
ρ is the density of water (998.2 kilogram / meter3)
d is the hydraulic diameter of a pipe in meters. For a round pipe, the 
    hydraulic diameter is the same as the pipe’s inner diameter.
v is the velocity of the water flowing through the pipe in meters / second
μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
"""

def reynolds_number(diameter, velocity):
    reynolds = (const.WATER_DENSITY*diameter*velocity)/0.0010016

    return reynolds

"""
k = (0.1 + (50/reynolds_number))*((larger_diameter/smaller_diameter)**4-1)
P = (-k*998.2*fluid_velocity**2)/2000

where
k is a constant computed by the first formula and used in the second formula
R is the Reynolds number that corresponds to the pipe with the larger diameter
D is the diameter of the larger pipe in meters
d is the diameter of the smaller pipe in meters
P is the lost pressure kilopascals
ρ is the density of water (998.2 kilogram / meter3)
v is the velocity of the water flowing through the larger diameter pipe in meters / second

"""
def pressure_loss_from_pipe_reduction(diameter,
        velocity, reynolds, HDPE_SDR11_INNER_DIAMETER):
    k = (0.1 + (50/reynolds))*((diameter/HDPE_SDR11_INNER_DIAMETER)**4-1)

    loss = (-k*const.WATER_DENSITY*velocity**2)/2000

    return loss

def conversion(pressure):
    psi = pressure * 0.145038

    return psi


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    psi = conversion(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi:.1f} pounds per square inchds")


if __name__ == "__main__":
    main()
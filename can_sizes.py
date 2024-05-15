"""
volume = π radius2 height
surface_area = 2π radius (radius + height)
"""

import math

def main():

    ["#1 Picnic"	"6.83"	"10.16"	"$0.28"]
    volume = compute_volume(6.83, 10.16)
    input



# Computes the volume of a tin can.
def compute_volume(radius, height):
    volume = math.pi * radius**2 * height

    return volume

# Computes the surface area of a tin can.
def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)

    return surface_area

# Computes storage efficency of the can.
def compute_efficency(volume, surface_area):
    storage_efficency = volume / surface_area
    
    return storage_efficency

# Prints the output
def print_metrics(radius, height)
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    efficency = compute_efficency(volume, surface)

    print
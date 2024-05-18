"""
volume = π radius2 height
surface_area = 2π radius (radius + height)
"""

import math

def main():


#1 Picnic	6.83	10.16	$0.28
#1 Tall	    7.78	11.91	$0.43
#2	        8.73	11.59	$0.45
#2.5	    10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	        13.02	14.29	$0.83
#6Z	        5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	        15.72	17.78	$1.53
#211	    6.83	12.38	$0.34
#300	    7.62	11.27	$0.38
#303	    8.10	11.11	$0.42



    volume = compute_volume(6.83, 10.16)
    surface_area = compute_surface_area(6.83, 10.16)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.28)
    metrics = print_metrics("#1 Picnic", 6.83, 10.16, cost_effic)
    

    volume = compute_volume(7.78, 11.91)
    surface_area = compute_surface_area(7.78, 11.91)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.43)
    metrics = print_metrics("#1 Tall", 7.78, 11.91, cost_effic)
    

    volume = compute_volume(8.73, 11.59)
    surface_area = compute_surface_area(8.73, 11.59)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.45)
    metrics = print_metrics("#2",8.73, 11.59, cost_effic)
    

    volume = compute_volume(10.32, 11.91)                            
    surface_area = compute_surface_area(10.32, 11.91)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.61)
    metrics = print_metrics("#2.5",10.32, 11.91, cost_effic)
    

    volume = compute_volume(10.79, 17.78)
    surface_area = compute_surface_area(10.79, 17.78)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.86)
    metrics = print_metrics("#3 Cylinder", 10.79, 17.78, cost_effic)
    

    volume = compute_volume(13.02, 14.29)
    surface_area = compute_surface_area(13.02, 14.29)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.83)
    metrics = print_metrics("#5", 13.02, 14.29, cost_effic)
    

    volume = compute_volume(5.40, 8.89)
    surface_area = compute_surface_area(5.40, 8.89)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.22)
    metrics = print_metrics("#6Z", 5.40, 8.89, cost_effic)
    
        
    volume = compute_volume(6.83, 7.62)
    surface_area = compute_surface_area(6.83, 7.62)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.26)
    metrics = print_metrics("#8Z short", 6.83, 7.62, cost_effic)
    

    volume = compute_volume(15.72, 17.78)
    surface_area = compute_surface_area(15.72, 17.78)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 1.53)
    metrics = print_metrics("#10", 15.72, 17.78, cost_effic)
    

    volume = compute_volume(6.83, 12.38)
    surface_area = compute_surface_area(6.83, 12.38)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.34)
    metrics = print_metrics("#211", 6.83, 12.38, cost_effic)
    

    volume = compute_volume(7.62, 11.27)
    surface_area = compute_surface_area(7.62, 11.27)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.38)
    metrics = print_metrics("#300", 7.62, 11.27, cost_effic)
    

    volume = compute_volume(8.10, 11.11)
    surface_area = compute_surface_area(8.10, 11.11)
    efficency = compute_efficency(volume, surface_area)
    cost_effic = compute_cost_efficency(volume, 0.42)
    metrics = print_metrics("#303", 8.10, 11.11, cost_effic)
    


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

def compute_cost_efficency(volume, cost):
    cost_efficency = volume / cost
    
    return cost_efficency

# Prints the output
def print_metrics(can, radius, height, cost_effic):
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    efficency = compute_efficency(volume, surface)

    print(f"{can} {efficency:.2f} ${cost_effic:.2f}")



main()

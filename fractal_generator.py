"""
Assignment 2: Fractal Generator

Author: Louise Hedegård Madsen

Description:
This script generates fractal patterns using recursive functions and geometric transformations.
"""

# Importing libraries and stuff
import matplotlib.pyplot as plt
import math

# Base case: when the depth of the recursive function is zero, it will stop running
def base_case (depth):
    return depth <= 0

# drawing branch
def draw_tree_branch(ax, start_point, length, angle):
    # finding the end point of a branch
    end_point = (
            start_point[0] + length * math.cos(angle),   # the square brackets extract the 0th object of the start point aka the x-coordinate.
            start_point[1] + length * math.sin(angle)
    )

    # drawing the branch
    ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]])

    return end_point # returing end_point so that the new starting point is the previous end point

# Recursive case
def recursive_case(ax, start_point, length, angle, depth, branches=3):
    # if base_case if true then stopping
    if base_case(depth):
        return
    
    # drawing the first branch
    end_point = draw_tree_branch(ax, start_point, length, angle)

    # recursive branching
    length_multiplier = 0.5 
    new_length = length * length_multiplier     # shorting each new branch depth with the length_multiplier
    
    angle_offset = math.radians(20)             # the angle new branch will have to the previous branch

    for i in range(branches):
        new_angle = angle - (branches - 1) * angle_offset / 2 + i * angle_offset    # calculating the new angle for each new branch
        recursive_case(ax, end_point, new_length, new_angle, depth - 1) 

# plotting the fractal tree
fig, ax = plt.subplots()
ax.axis("off")

# initial parameters
start_point = (0,0)
initial_length = 10
initial_angle = math.radians(90)
depth = 4

# call the recursive function
recursive_case(ax, start_point = start_point, length = initial_length, angle = initial_angle, depth = depth)

plt.show()
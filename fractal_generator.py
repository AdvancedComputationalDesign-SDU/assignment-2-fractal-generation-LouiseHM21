"""
Assignment 2: Fractal Generator

Author: Louise Hedegård Madsen

Description:
This script generates fractal patterns using recursive functions and geometric transformations.
"""

# Importing libraries and stuff
import matplotlib.pyplot as plt
import matplotlib.cm as cm          # for colormapping
import math
import random

# Base case: when the depth of the recursive function is zero, it will stop running
def base_case (depth):
    return depth <= 0

# drawing branch
def draw_tree_branch(ax, start_point, length, angle, color):
    # finding the end point of a branch
    end_point = (
            start_point[0] + length * math.cos(angle),   # the square brackets extract the 0th object of the start point aka the x-coordinate.
            start_point[1] + length * math.sin(angle)
    )

    # drawing the branch
    ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], color = color)

    return end_point # returing end_point so that the new starting point is the previous end point

# Recursive case
def recursive_case(ax, start_point, length, angle, depth, max_depth, branches=2):
    # if base_case if true then stopping
    if base_case(depth):
        return
    
    # color gradient according to the depth
    color = cm.viridis(depth / max_depth)       # the depth is normalized according to the max_depth

    # drawing the first branch
    end_point = draw_tree_branch(ax, start_point, length, angle, color)

    # recursive branching
    for i in range(branches):
        length_multiplier = random.uniform(0.6,0.9)         # making the length_multiplier random
        new_length = length * length_multiplier
        
        random_angle_offset = random.uniform(0,90)
        angle_offset = math.radians(random_angle_offset)    # making the angles of the branches random

        new_angle = angle - (branches - 1) * angle_offset / 2 + i * angle_offset    # calculating the new angle for each new branch
        recursive_case(ax, end_point, new_length, new_angle, depth - 1, max_depth) 

# plotting the fractal tree
fig, ax = plt.subplots()
ax.axis("off")

# initial parameters
start_point = (0,0)
initial_length = 1
initial_angle = math.radians(90)
max_depth = 6

# call the recursive function
recursive_case(ax, start_point = start_point, length = initial_length, angle = initial_angle, depth = max_depth, max_depth = max_depth)

plt.show()

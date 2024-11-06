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

# plotting the fractal tree
fig, ax = plt.subplots()

# call the recursive function
draw_tree_branch(ax, [0,0], 10, 20)

plt.show()
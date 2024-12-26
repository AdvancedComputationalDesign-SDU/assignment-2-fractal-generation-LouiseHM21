# Importing libraries
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from shapely.geometry import LineString, Point
from shapely.affinity import rotate, scale, translate

# Base case: when the depth of the recursive function is zero, it will stop running
def base_case(depth):
    return depth <= 0

# Drawing branch using Shapely
def draw_tree_branch(ax, start_point, length, angle, color, line_width):
    # Create the initial branch as a line segment
    branch = LineString([
        start_point,
        (start_point[0] + length, start_point[1])  # Horizontal line initially
    ])

    # Rotate the branch to match the desired angle
    branch = rotate(branch, angle, origin=start_point, use_radians=True)

    # Plot the branch
    x, y = branch.xy
    ax.plot(x, y, color=color, lw=line_width)

    return branch.coords[-1]  # Return the endpoint of the branch

# Recursive case
def recursive_case(ax, start_point, length, angle, depth, max_depth, branches=3):
    # If base case is met, stop recursion
    if base_case(depth):
        return

    # Calculate line width based on depth
    line_width = max(1, 8 * depth / max_depth)

    # Assign color gradient based on depth
    color = cm.viridis(depth / max_depth)

    # Draw the main branch and get its endpoint
    end_point = draw_tree_branch(ax, start_point, length, angle, color, line_width)

    # Recursive branching
    for i in range(branches):
        # Randomize length and angle for natural variation
        new_length = length * random.uniform(0.6, 1.0)
        angle_offset = random.uniform(0, 45)  # Random angle offset in degrees
        new_angle = angle - (branches - 1) * angle_offset / 2 + i * angle_offset

        # Recursive call with updated parameters
        recursive_case(ax, end_point, new_length, new_angle, depth - 1, max_depth)

# Plotting the fractal tree
fig, ax = plt.subplots()
ax.axis("off")

# Input parameters
start_point = (0, 0)  # Starting coordinates
initial_length = 1  # Initial branch length
initial_angle = 90  # Initial angle in degrees
max_depth = 4  # Maximum recursion depth

# Call the recursive function
recursive_case(
    ax,
    start_point=start_point,
    length=initial_length,
    angle=initial_angle,
    depth=max_depth,
    max_depth=max_depth
)

plt.show()

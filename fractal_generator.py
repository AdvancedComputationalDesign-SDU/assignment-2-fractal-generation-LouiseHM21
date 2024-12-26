# Importing libraries
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
from shapely.geometry import LineString, Point
from shapely.affinity import rotate, scale, translate

# Base case: when the depth of the recursive function is zero, it will stop running
def base_case(depth):
    return depth <= 0  # Terminates recursion when the depth reaches zero

# Drawing branch using Shapely
def draw_tree_branch(ax, start_point, length, angle, color, line_width):
    # Create the initial branch as a horizontal line segment
    branch = LineString([
        start_point,
        (start_point[0] + length, start_point[1])  # Define end point horizontally from start point
    ])

    # Rotate the branch around the start point to match the desired angle
    branch = rotate(branch, angle, origin=start_point, use_radians=True)

    # Extract the coordinates and plot the branch on the axis
    x, y = branch.xy
    ax.plot(x, y, color=color, lw=line_width)

    # Return the end point of the branch for further recursive branching
    return branch.coords[-1]

# Recursive case
def recursive_case(ax, start_point, length, angle, depth, max_depth, branches=3):
    # If base case is met, stop recursion
    if base_case(depth):
        return

    # Calculate line width based on current depth for visual effect
    line_width = max(1, 8 * depth / max_depth)

    # Assign a color based on the recursion depth using a gradient colormap
    color = cm.viridis(depth / max_depth)

    # Draw the main branch and get its endpoint for further branching
    end_point = draw_tree_branch(ax, start_point, length, angle, color, line_width)

    # Generate child branches recursively
    for i in range(branches):
        # Randomize the length of the new branch for natural variation
        new_length = length * random.uniform(0.6, 1.0)

        # Randomize the angle offset to create different branching patterns
        angle_offset = random.uniform(0, 45)  # Offset in degrees
        new_angle = angle - (branches - 1) * angle_offset / 2 + i * angle_offset

        # Recursive call with updated parameters
        recursive_case(ax, end_point, new_length, new_angle, depth - 1, max_depth)

# Plotting the fractal tree
fig, ax = plt.subplots()
ax.axis("off")  # Hide axes for a cleaner visualization

# Input parameters for the fractal tree
start_point = (0, 0)  # Starting coordinates for the tree trunk
initial_length = 1  # Length of the initial branch
initial_angle = 90  # Starting angle in degrees (90 for vertical trunk)
max_depth = 4  # Maximum recursion depth

# Call the recursive function to generate the fractal tree
recursive_case(
    ax,
    start_point=start_point,
    length=initial_length,
    angle=initial_angle,
    depth=max_depth,
    max_depth=max_depth
)

plt.show()  # Display the generated fractal tree

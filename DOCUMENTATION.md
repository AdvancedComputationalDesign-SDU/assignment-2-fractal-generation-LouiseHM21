# Assignment 2: Fractal Generation Documentation

## Table of Contents

- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Results](#results)
- [Challenges and Solutions](#challenges-and-solutions)
- [References](#references)

---

## Pseudo-Code

1. **Base Case Function: `base_case(depth)`**
   - **Inputs**:
     - `depth`: Current recursion depth.
   - **Process**:
     - **If** `depth` ≤ 0:
       - Return `True` (end recursion).
     - Else:
       - Return `False` (continue recursion).

2. **Draw Tree Branch Function: `draw_tree_branch(ax, start_point, length, angle, color, line_width)`**
   - **Inputs**:
     - `ax`: Plotting axis for drawing.
     - `start_point`: Tuple (x, y) representing the branch's starting point.
     - `length`: Length of the branch.
     - `angle`: Angle in radians.
     - `color`: Branch color (gradient mapped to recursion depth).
     - `line_width`: Width of the branch line.
   - **Process**:
     - Calculate `end_point`:
       - `end_x = start_x + length * cos(angle)`
       - `end_y = start_y + length * sin(angle)`
     - Draw line from `start_point` to `end_point` on the plotting axis `ax`.
     - Return `end_point` as the new starting point for subsequent branches.

3. **Recursive Case Function: `recursive_case(ax, start_point, length, angle, depth, max_depth, branches=3)`**
   - **Inputs**:
     - `ax`: Plotting axis for drawing.
     - `start_point`: Tuple (x, y) representing the branch's starting point.
     - `length`: Length of the current branch.
     - `angle`: Angle in radians of the current branch.
     - `depth`: Current recursion depth.
     - `max_depth`: Maximum allowed recursion depth.
     - `branches`: Number of branches splitting from each node.
   - **Process**:
     - **If** `base_case(depth)` is `True`:
       - Return (end recursion).
     - Calculate `line_width` based on depth:
       - `line_width = max(1, 8 * depth / max_depth)`
     - Map `depth` to a color gradient using colormap:
       - `color = cm.viridis(depth / max_depth)`
     - Draw the main branch:
       - Call `draw_tree_branch(ax, start_point, length, angle, color, line_width)`.
     - **For** each branch (from 0 to `branches - 1`):
       - Calculate new branch properties:
         - `new_length = length * random.uniform(0.6, 1.0)`
         - `angle_offset = radians(random.uniform(0, 45))`
         - `new_angle = angle - (branches - 1) * angle_offset / 2 + i * angle_offset`
       - Recursive call with updated parameters:
         - `recursive_case(ax, end_point, new_length, new_angle, depth - 1, max_depth)`

4. **Set Up Plot**
   - Create a plotting figure:
     - `fig, ax = plt.subplots()`
   - Hide the axes:
     - `ax.axis('off')`

5. **Define Starting Parameters**
   - Set the starting point:
     - `start_point = (0, 0)`
   - Set initial branch length:
     - `initial_length = 1`
   - Set initial angle in radians:
     - `initial_angle = radians(90)`
   - Define the maximum recursion depth:
     - `max_depth = 3`

6. **Call Recursive Function**
   - Call the `recursive_case` function:
     - `recursive_case(ax, start_point, initial_length, initial_angle, max_depth, max_depth)`

7. **Display the Plot**
   - Render the fractal tree:
     - `plt.show()`

---

### Highlights of Refinements
- Explicitly defined inputs, outputs, and processes for each function.
- Clearly structured steps for recursive calculations and plotting.
- Detailed explanations for each branch's recursive properties (length, angle, color, line width).
---

## Technical Explanation

*(Provide a concise explanation of your code, focusing on recursion and geometric manipulations. Discuss how your approach generates the final fractal pattern and the mathematical principles involved.)*

Example:

In my implementation, the `generate_fractal` function recursively draws line segments representing branches of a fractal tree. The function calculates the end point of each line using trigonometric functions based on the current angle and length.

At each recursion step, the function:

- Decreases the `length` by multiplying it with `length_scaling_factor`.
- Adjusts the `angle` by adding or subtracting `angle_change` to create branching.
- Calls itself recursively for each branch until the `recursion_depth` reaches zero.

This approach creates a self-similar pattern characteristic of fractals, where each branch splits into smaller branches in a consistent manner.

---

## Results

*(Include images of your generated fractal patterns, and discuss any observations or interesting findings.)*

Example:

### Fractal Pattern 1: Basic Fractal Tree

![Fractal Tree](images/example.png)

- **Parameters**:
  - `angle_change`: 30°
  - `length_scaling_factor`: 0.7
  - `recursion_depth`: 5
- **Observations**:
  - The fractal tree exhibits symmetry and balance.
  - As the recursion depth increases, the level of detail in the branches increases.

*(Repeat for other fractal patterns.)*

---

## Challenges and Solutions

*(Discuss any challenges you faced during the assignment and how you overcame them.)*

Example:

- **Challenge**: Managing the growing number of line segments and ensuring they are correctly plotted.
  - **Solution**: Stored all line segments in a list and plotted them after the recursion completed.

- **Challenge**: Implementing randomness without losing the overall structure.
  - **Solution**: Introduced randomness within controlled bounds for angles and lengths.

---

## References

*(List any resources you used or found helpful during the assignment.)*

- **Shapely Manual**: [https://shapely.readthedocs.io/en/stable/manual.html](https://shapely.readthedocs.io/en/stable/manual.html)
- **Matplotlib Pyplot Tutorial**: [https://matplotlib.org/stable/tutorials/introductory/pyplot.html](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

---

*(Feel free to expand upon these sections to fully capture your work and learning process.)*
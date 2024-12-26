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

## Technical Explanation

In this implementation, the `recursive_case` function is the core component for generating fractal patterns through recursive branching. The function emulates the process of tree growth by drawing branches that split and decrease in size at each recursion step.

**Key Steps in the Recursive Process:**
1. **Base Case**:  
   The recursion stops when the `depth` reaches zero (`base_case(depth)`), ensuring the function terminates.

2. **Branch Creation**:  
   At each step, the function:
   - Calculates the `end_point` of the branch using trigonometric functions (`cos` and `sin`), based on the `start_point`, `length`, and `angle`.
   - Draws the branch using `ax.plot()`, with visual attributes (color and line width) mapped to the current depth. The line width decreases with depth, and the color gradient is computed using the Viridis colormap.

3. **Recursive Splitting**:  
   Each branch generates a specified number of smaller branches (`branches`). For each new branch:
   - The `length` is scaled down by a random factor, introducing variation in branch lengths.
   - The `angle` is adjusted by an offset, calculated using a random spread to simulate natural branching angles.
   - The function calls itself recursively with the updated parameters (`new_length`, `new_angle`, `depth - 1`).

4. **Visualization**:  
   The recursive calls progressively add branches to the plot, creating a self-similar fractal pattern. The visual effect is enhanced by the colormap and varying line widths, providing a sense of depth and complexity.

This recursive approach mirrors the principles of fractals, where each part resembles the whole. By combining randomness in angles and lengths with controlled recursion, the algorithm generates visually appealing and natural-looking fractal trees. This flexibility allows customization of parameters such as branch count, maximum depth, and randomness to explore a variety of fractal patterns.

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
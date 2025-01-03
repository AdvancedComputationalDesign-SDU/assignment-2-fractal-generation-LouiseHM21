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
     - `angle`: Angle in degrees.
     - `color`: Branch color (gradient mapped to recursion depth).
     - `line_width`: Width of the branch line.
   - **Process**:
     - Create a `LineString` from `start_point` to `(start_point[0] + length, start_point[1])`.
     - Rotate the line by `angle` around `start_point`.
     - Draw the line using `ax.plot()`.
     - Return the `end_point` of the branch for subsequent recursion.

3. **Recursive Case Function: `recursive_case(ax, start_point, length, angle, depth, max_depth, branches=3)`**
   - **Inputs**:
     - `ax`: Plotting axis for drawing.
     - `start_point`: Tuple (x, y) representing the branch's starting point.
     - `length`: Length of the current branch.
     - `angle`: Angle in degrees of the current branch.
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
         - `angle_offset = random.uniform(0, 45)`
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
   - Set initial angle in degrees:
     - `initial_angle = 90`
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
   - Creates a branch as a `LineString` object from the `start_point` using Shapely.
   - Rotates the branch by the specified `angle` around the `start_point`.
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

### **Fractal Variation 1**  
**Parameters**:  
- `angle_offset`: 30°  
- `length_multiplier`: 0.5  
- `branches`: 3  
- `depth`: 4  

**Observations**:  
- Showcasing the initial 2D fractal tree.  
- Symmetry in the tree structure is evident.  
- Lacks natural appearance and fullness.  
- Appears very geometric and artificial.

![Fractal Image 1](images/2D_FractalTree1.png)

### **Fractal Variation 2**  
**Parameters**:  
- `angle_offset`: 30°  
- `length_multiplier`: 0.5  
- `branches`: 3  
- `depth`: 4  

**Observations**:  
- Same fractal structure as Image 1, but a color gradient is added based on recursion depth.  
- Color adds visual interest but doesn’t affect the overall structure or natural appearance.

![Fractal Image 2](images/2D_FractalTree2.png)

### **Fractal Variation 3**  
**Parameters**:  
- `angle_offset`: 45°  
- `length_multiplier`: 0.8  
- `branches`: 2  
- `depth`: 6  

**Observations**:  
- Wider and fuller fractal tree due to the increased angle.  
- Appears more natural than previous iterations.  
- Symmetry still makes the tree look artificial.

![Fractal Image 3](images/2D_FractalTree3.png)

### **Fractal Variation 4**  
**Parameters**:  
- `angle_offset`: Random within [-50, 50]  
- `length_multiplier`: 0.8  
- `branches`: 2  
- `depth`: 6  

**Observations**:  
- Randomized angles remove the strict symmetry of the tree.  
- Tree still appears unnatural and lacks fullness.

![Fractal Image 4](images/2D_FractalTree4.png)

### **Fractal Variation 5**  
**Parameters**:  
- `angle_offset`: Random within [0, 30]  
- `length_multiplier`: 0.8  
- `branches`: 2  
- `depth`: 6  

**Observations**:  
- Adjusted angle randomness improves the natural look.  
- Fractal tree still lacks fullness in its structure.

![Fractal Image 5](images/2D_FractalTree5.png)

### **Fractal Variation 6**  
**Parameters**:  
- `angle_offset`: Random within [0, 45]  
- `length_multiplier`: Random within [0.6, 0.8]  
- `branches`: 2  
- `depth`: 6  

**Observations**:  
- Randomization in both angle and length increases the natural appearance.  
- Still looks sparse and could use more fullness.

![Fractal Image 6](images/2D_FractalTree6.png)

### **Fractal Variation 7**  
**Parameters**:  
- `angle_offset`: Random within [0, 60]  
- `length_multiplier`: Random within [0.5, 0.8]  
- `branches`: 2  
- `depth`: 6  
- `line_width`: 10  

**Observations**:  
- Varying branch thickness based on depth adds realism.  
- Wider angle range makes the tree appear unnaturally wide.

![Fractal Image 7](images/2D_FractalTree7.png)

### **Fractal Variation 8**  
**Parameters**:  
- `angle_offset`: Random within [0, 30]  
- `length_multiplier`: Random within [0.7, 0.8]  
- `branches`: 2  
- `depth`: 10  
- `line_width`: 8  

**Observations**:  
- Increased recursion depth enhances the natural appearance.  
- The tree appears tall and narrow relative to its width.

![Fractal Image 8](images/2D_FractalTree8.png)

### **Fractal Variation 9**  
**Parameters**:  
- `angle_offset`: Random within [0, 30]  
- `length_multiplier`: Random within [0.8, 0.9]  
- `branches`: 3  
- `depth`: 8  
- `line_width`: 8  

**Observations**:  
- Increased branches create a fuller, wider tree.  
- Looks more natural than previous iterations.

![Fractal Image 9](images/2D_FractalTree9.png)

### **Fractal Variation 10**  
**Parameters**:  
- `angle_offset`: Random within [0, 30]  
- `length_multiplier`: Random within [0.6, 0.9]  
- `branches`: 4  
- `depth`: 7  
- `line_width`: 10  

**Observations**:  
- Increased number of branches results in a much fuller, wider tree.  
- However, the added branches make the tree look less natural and overly dense.  

![Fractal Image 10](images/2D_FractalTree10.png)

---

## Challenges and Solutions

### **Challenge 1: Symmetry in Fractal Tree**
- **Problem**: Early versions of the fractal tree appeared overly symmetrical, making the structure look unnatural and artificial.  
- **Solution**: Introduced randomness in both branch angles and lengths. By using `random.uniform()` to create variability within specified ranges, the fractal tree achieved a more organic and less predictable appearance.

### **Challenge 2: Sparse and Bare Tree Structure**
- **Problem**: The fractal tree often looked sparse and lacked fullness, especially at lower recursion depths.  
- **Solution**: Increased the recursion depth and allowed more branches (`branches`) to spawn at each iteration. Additionally, adjusting `angle_offset` and `length_multiplier` helped create fuller and more interconnected branches.

### **Challenge 3: Handling Visual Complexity**
- **Problem**: At higher recursion depths, the large number of branches made it difficult to maintain clarity in visualization.  
- **Solution**: Adjusted line widths based on depth using `line_width = max(1, 8 * depth / max_depth)`. Thicker lines near the base and thinner lines at higher levels improved visual balance.

### **Challenge 4: Visualizing Depth**
- **Problem**: Without visual cues, it was difficult to distinguish between different levels of recursion.  
- **Solution**: Applied a colormap (`cm.viridis`) to assign colors based on depth. This provided a gradient effect, making it easier to identify deeper branches.

### **Challenge 5: Maintaining Code Flexibility**
- **Problem**: Hardcoded parameters made experimenting with different tree styles and structures tedious.  
- **Solution**: Encapsulated key parameters like `branches`, `angle_offset`, `length_multiplier`, and `depth` into function inputs. This modular approach made it easy to adjust values and experiment dynamically. 

---

## References

- **Matplotlib Pyplot**: [https://matplotlib.org/stable/api/pyplot_summary.html]  
  *(Used for plotting and visualizing the fractal tree.)*

- **Matplotlib Colormap**: [https://matplotlib.org/stable/api/cm_api.html]  
  *(Used for applying color gradients based on recursion depth.)*

- **Pseudo-random Numbers**: [https://docs.python.org/3/library/random.html#random.uniform]  
  *(Used for introducing randomness in branch angles and lengths to enhance natural appearance.)*

- **Shapely Library**: [https://shapely.readthedocs.io/en/stable/manual.html]  
  *(Used for geometric transformations such as rotation and line creation.)*

- **Mathematical Functions**: [https://docs.python.org/3/library/math.html]  
  *(Used for trigonometric calculations of branch endpoints and angle adjustments.)*

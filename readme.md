# Knight Shortest Path Solver

This Python script solves the problem of finding the shortest path for a knight on a chessboard from a given starting position to a target position. It implements a breadth-first search algorithm to explore all possible paths and identify the shortest one.

## Features

-   Shortest Path Calculation: Computes the shortest path for a knight from a given starting position to a target position on a chessboard.
-   Graph Visualization: Generates a graph visualization (in Graphviz/DOT format) of all possible shortest paths.
-   Chessboard Visualization: Visualizes the shortest path on a chessboard using Matplotlib, providing an intuitive representation of the knight's movements.

##  Usage

### Prerequisites
        - Python 3.x
        - Matplotlib
        - Graphviz (for generating graph visualizations)
        - deque
        - numpy
        - argparse

### Running the Script
        run the script as follows:
            ```
            python3 knight_solution.py A1 H8
            ```
            Replace A1 and H8 with your desired starting and ending positions in algebraic chess notation.
### Output
After running the script, the following outputs will be generated:

- **Console Output**: Displays all minimum-length sequences of moves from the starting to the ending position.

- **Graph Visualization**: Saves a Graphviz/DOT file (`shortest_paths_graph.dot`) representing the shortest paths graph.

- **Chessboard Visualization**: Saves a PNG image (`shortest_path_knight.png`) showing the chessboard with the shortest path plotted.
    ![chessboard](https://github.com/aleenababy/knight_shortest_path/blob/main/shortest_path_knight.png)
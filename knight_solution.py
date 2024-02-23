
import argparse
from collections import deque
import graphviz
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

class Chessboard:
    """
    Represents a chessboard.

    Attributes:
        row (int): The number of rows on the chessboard.
        col (int): The number of columns on the chessboard.

    Methods:
        build(w, h): Constructs a square-shaped chessboard of size w x h.
    """

    def __init__(self, w, h):
        """
        Initializes a Chessboard instance with the specified dimensions.

        Args:
            w (int): The number of rows on the chessboard.
            h (int): The number of columns on the chessboard.
        """
        self.row = w
        self.col = h

    def build(w, h):
        """
        Constructs a square-shaped chessboard of size w x h.

        Args:
            w (int): The number of rows and columns for the chessboard.
            h (int): The number of rows and columns for the chessboard.

        Returns:
            numpy.ndarray: A 2D array representing the square-shaped chessboard.

        Raises:
            ValueError: If w and h are not equal, indicating a non-square-shaped board.
        """
        if w != h:
            raise ValueError('It is not a square shaped board!')
        re = np.r_[w * [0, 1]]
        ro = np.r_[w * [1, 0]]
        chessboard = np.row_stack(h * (re, ro))
        return chessboard

class Knight:
    """
    Represents a knight on a chessboard.

    Attributes:
        row (int): The row position of the knight.
        col (int): The column position of the knight.

    Methods:
        can_move(cls, row, col): Determines if the knight can move to the given position.
    """
    def __init__(self, row, col):
        """
        Initializes a Knight instance with the specified row and column positions.

        Args:
            row (int): The row position of the knight.
            col (int): The column position of the knight.
        """
        self.row = row
        self.col = col
    @classmethod
    def can_move(cls, row, col):
        """
        Determines if the knight can move to the given position.

        Args:
            row (int): The row position to check.
            col (int): The column position to check.

        Returns:
            bool: True if the knight can move to the given position, False otherwise.
        """
        return 0 <= row < 8 and 0 <= col < 8 #True

def get_possible_moves(position):
    """
    Gets the possible moves for a knight from the given position.

    Args:
        position (tuple): A tuple containing the row and column positions.

    Returns:
        list of tuples: A list of tuples representing the possible moves.
    """
    x, y = position
    possible_moves = [
        (x + 1, y + 2), (x + 1, y - 2), 
        (x - 1, y + 2), (x - 1, y - 2), 
        (x + 2, y + 1), (x + 2, y - 1), 
        (x - 2, y + 1), (x - 2, y - 1)
    ]
    return [(a, b) for a, b in possible_moves if Knight.can_move(a, b)]

def shortest_path(start, end):
    """
    Finds all shortest paths from the start position to the end position on a chessboard.

    Args:
        start (tuple): A tuple representing the starting position (row, column).
        end (tuple): A tuple representing the ending position (row, column).

    Returns:
        list of lists: A list containing all minimum-length sequences of moves from the start to the end position.
    """
    start = tuple(start)
    end = tuple(end)
    queue = deque([[start]])  # Initialize queue with the start position
    visited = set([start])  # Initialize set to store visited positions
    all_sequences = []  # Initialize list to store all sequences

    # Perform breadth-first search
    while queue:
        path = queue.popleft()  # Get the first path in the queue
        current_position = path[-1]  # Get the current position from the path

        if current_position == end:  # Check if the current position is the end position
            all_sequences.append(path)  # Add the path to the list of sequences
            continue

        # Iterate over possible moves from the current position
        for next_position in get_possible_moves(current_position):
            if next_position not in visited:  # Check if the next position has not been visited
                queue.append(path + [next_position])  # Add the new path to the queue
                visited.add(next_position)  # Mark the next position as visited

    return all_sequences  # Return all minimum-length sequences


def generate_graphviz(start, end, all_sequences):
    """
    Generate a Graphviz representation of the shortest path from start to end.

    Args:
        start (tuple): A tuple representing the starting position (row, column).
        end (tuple): A tuple representing the ending position (row, column).
        all_sequences (list of lists): A list containing all minimum-length sequences of moves.

    Returns:
        None
    """
    dot = graphviz.Digraph()

    # Add edges for all sequences
    for seq in all_sequences:
        for i in range(len(seq) - 1):
            x1, y1 = seq[i]
            x2, y2 = seq[i + 1]
            dot.edge(get_position_name(x1, y1), get_position_name(x2, y2), color = 'blue')

    # Set attributes for the graph
    dot.attr(label = f"Shortest path from {get_position_name(*start)} to {get_position_name(*end)}")
    dot.attr(fontsize = '14')
    dot.attr(size = '8, 8')

    # Render the graph to both dot and png formats
    dot.render('shortest_paths_graph', format = 'png', cleanup = True)
    dot.render('all_shortest_path', format = 'dot', cleanup = True)

def get_position_name(row, col):
    """
    Convert row and column indices to chessboard notation.

    Args:
        row (int): The row index.
        col (int): The column index.

    Returns:
        str: The position in chessboard notation (e.g., 'A1').
    """
    letter = chr(col + 65)
    number = row + 1 
    return letter + str(number)


# Convert chess notation to position
def chess_notation_to_position(chess_notation):
    """
    Convert chess notation to position.

    Args:
        chess_notation (str): The chess notation string (e.g., 'A1').

    Returns:
        tuple: A tuple representing the position (row, column).
    """
    letter, number = chess_notation[0], chess_notation[1]
    col = ord(letter) - ord('A')
    row = int(number) - 1
    return (row, col)

def main(start, end):
    """
    Main function to execute the knight's shortest path program.

    Prompts the user to input starting and ending positions in chess notation, 
    calculates the shortest path between them, generates a graph visualizing the
    paths, and displays the results including the minimum-length sequences, 
    chessboard with paths, and the generated graph.

    Raises:
        ValueError: If the starting or ending point is not within the valid range.

    """
    #start = input("Enter the starting position (e.g., 'A1'): ").upper()
    #end = input("Enter the ending position (e.g., 'H8'): ").upper()
    # Convert chess notation to position
    start = chess_notation_to_position(start)
    end = chess_notation_to_position(end)
    # Check if start and end are within the valid range
    if not all(0 <= value < 8 for value in start):
        raise ValueError("starting point is not within the valid range")
    if not all(0 <= value < 8 for value in end):
        raise ValueError("end is not within the valid range")
    
    # Find the shortest path from all possible path
    all_sequences = shortest_path(start, end)
    # Generate graph visualization
    generate_graphviz(start, end, all_sequences)
    
    # Print minimum-length sequences
    print("All minimum-length sequences:")
    for seq in all_sequences:
        print([get_position_name(x, y) for x, y in seq])
        
    # addition to the dot file, display chessboard and graph
    # side by side with custom tick parameters, column names, 
    # and lower left corner as (0, 0) point
    fig, ( ax1, ax2) = plt.subplots(1, 2)
    chessboard = Chessboard.build(4, 4)
    chessboard = np.transpose(chessboard)
    colors = ['white', 'black', 'blue']
    custom_colormap = ListedColormap(colors)
    for x, y in all_sequences[0]:
        chessboard[x][y] = 2
    ax1.imshow(chessboard, cmap = custom_colormap)
    #ax1.axis('off')
    ax1.set_xticks(np.arange(8))
    ax1.set_xticklabels([])
    ax1.set_yticks(np.arange(8))
    ax1.set_yticklabels([])

    # Set the origin at the lower left corner and limit the extent to match
    ax1.invert_yaxis()
    ax1.set_xlim(-0.5, 7.5)
    ax1.set_ylim(-0.5, 7.5)
    
    for i in range(8):
        ax1.text(i, -1.1, chr(65 + i), ha = 'center', va = 'center', fontsize = 12)
        ax1.text( -1.1, i , i +1, ha = 'center', va = 'center', fontsize = 12)
    ax2.imshow(plt.imread('shortest_paths_graph.png'))
    ax2.axis('off')
    plt.savefig('./shortest_path_knight.png')
    plt.show()

if __name__ == "__main__":
    """
    Entry point of the program.
    
    If this script is executed directly, it parses command-line arguments
    using the argparse module to handle input from the user. The script then finds all 
    shortest paths from the start position to the end position on a chessboard for knight.

    Parameters:
        start (str): Starting position in algebraic chess notation (e.g., 'A1').
        end (str): Ending position in algebraic chess notation (e.g., 'H8').

    Returns:
        None. This function invokes the main function to run the knight's
        shortest path program.
    """
    parser = argparse.ArgumentParser(description = 'Knight Shortest Path Program')
    parser.add_argument('start', type = str, help = 'Starting position in algebraic chess notation')
    parser.add_argument('end', type = str, help = 'Ending position in algebraic chess notation')
    args = parser.parse_args()
    main(args.start, args.end)


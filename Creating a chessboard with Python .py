import numpy as np
import matplotlib.pyplot as plt

def create_chessboard(rows, cols, square_size=30, light_color='white', dark_color='black'):
    # Calculate the size of the chessboard grid
    width = cols * square_size
    height = rows * square_size

    # Create a numpy array representing the chessboard
    chessboard = np.zeros((rows, cols), dtype=int)

    # Fill the chessboard with alternating 1s and 0s to represent light and dark squares
    chessboard[1::2, ::2] = 1
    chessboard[::2, 1::2] = 1

    # Create the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    for row in range(rows):
        for col in range(cols):
            color = light_color if chessboard[row, col] else dark_color
            square = plt.Rectangle((col * square_size, row * square_size), square_size, square_size, facecolor=color)
            ax.add_patch(square)

    ax.set_aspect('equal', 'box')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    rows = 8
    cols = 8
    square_size = 50
    light_color = 'white'
    dark_color = 'black'
    create_chessboard(rows, cols, square_size, light_color, dark_color)

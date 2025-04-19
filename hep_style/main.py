from style import setup_style

setup_style()

import numpy as np
import matplotlib.pyplot as plt

def plot_example():
    # Generate some data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a plot
    plt.figure()
    plt.plot(x, y, label='Sine Wave')
    plt.title('Example Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_example()


import matplotlib.pyplot as plt
import numpy as np

width = 6

# Configure matplotlib to use the 'pgf' backend for LaTeX rendering
plt.rcParams.update({
    "text.usetex": True,  # Enable LaTeX for all text
    "font.family": "serif",  # Use a serif font (default LaTeX font family)
    "font.serif": [],  # Leave it to default LaTeX font (Computer Modern)
    "text.color": "black",        # text color
    "axes.labelcolor": "black",   # axis label color
    "axes.edgecolor": "black",    # Axis edge color
    "axes.titlecolor": "black",   # Title color
    "xtick.color": "black",       # x axis tick color
    "ytick.color": "black",       # y axis tick color
    "text.antialiased": False,
    "lines.antialiased": False,
    "pgf.texsystem": "pdflatex",  # Or use 'xelatex' or 'lualatex' depending on your setup
    "pgf.preamble": r"\usepackage{amsmath}",  # Optional: Add any LaTeX packages you want
    "text.usetex": True,  # Enable LaTeX rendering for text in the plot
    "figure.figsize": (width, 0.618*width),  # Set the figure size (in inches)
    "xtick.labelsize": 22,  # Increase font size for x-axis numbers
    "ytick.labelsize": 22,  # Increase font size for y-axis numbers
    "axes.labelsize":  22,   # Adjust font size for axis labels (optional)
    "axes.titlesize":  22,   # Adjust font size for the title (optional)
})

# Example data
x = np.linspace(0, 10, 100000)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.xlabel(r"Tiempo (s)")
plt.ylabel(r"Altura (\%)")
plt.title(r"Señal de referencia")
plt.grid()
plt.tight_layout()
# Save the plot as a PDF with the pgf backend
plt.savefig("plot.pdf", backend="pgf")  # Saves as a PDF using LaTeX rendering

# Display the plot (optional)
plt.show()


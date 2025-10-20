import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep = ',', header = 0)

    # Create scatter plot
    x = df['Year'] 
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(x, y)

    x_extended = np.arange(x.min(), 2051)
    plt.plot(x_extended, intercept + slope*x_extended, 'r', label='Best fit line (all time)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year'] 
    y_recent = df_recent['CSIRO Adjusted Sea Level']

    slope2, intercept2, _, _, _ = linregress(x_recent, y_recent)

    x2_extended = np.arange(2000, 2051)
    plt.plot(x2_extended, intercept2 + slope2*x2_extended, 'g', label = 'Best fit line (2000 onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
        
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

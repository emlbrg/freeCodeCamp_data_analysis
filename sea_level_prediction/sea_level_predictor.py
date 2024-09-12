import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    # matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit.
    # Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    start = df['Year'].min()
    # print(start)
    end = 2050
    best_fit = {
        'Year': [],
        'y': []}

    for year in range(start, end):
        best_fit['Year'] = [year for year in range(start, end + 1)]
        best_fit['y'] = [result.slope * year + result.intercept for year in range(start, end + 1)]
    
    # Create first line of best fit
    plt.plot(best_fit['Year'], best_fit['y'], 'm')

    # Create second line of best fit  from year 2000 through the most recent year in the dataset.
    # Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    start = 2000
    end = 2050
    result = linregress(df.loc[df["Year"] >= start]['Year'], df.loc[df['Year'] >= start]['CSIRO Adjusted Sea Level'])

    for year in range(start, end):
        best_fit['Year'] = [year for year in range(start, end + 1)]
        best_fit['y'] = [result.slope * year + result.intercept for year in range(start, end + 1)]

    plt.plot(best_fit['Year'], best_fit['y'], 'g')

    # Add labels and title
    # The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
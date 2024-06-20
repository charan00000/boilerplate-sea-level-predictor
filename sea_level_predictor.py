import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    df['Year']=df['Year'].astype(int)

    # Create scatter plot
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=df)
    plt.show()

    # Create first line of best fit
    total_info=linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    info2000=linregress(df[df['Year']>=2000]['Year'], 
                        df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    next_year=df.iloc[-1]['Year'].astype(int)+1
    guess_df=pd.DataFrame({
        'Year': [i for i in range(next_year, 2051)],
        'CSIRO Adjusted Sea Level': [None for i in range(next_year, 2051)],
        'Lower Error Bound': [None for i in range(next_year, 2051)],
        'Upper Error Bound': [None for i in range(next_year, 2051)],
        'NOAA Adjusted Sea Level': [None for i in range(next_year, 2051)]
    })
    df=pd.concat([df,guess_df])
    plt.plot(df['Year'], (df['Year']*total_info.slope)+total_info.intercept)
    # Create second line of best fit
    plt.plot(df[df['Year']>=2000]['Year'], 
             (df[df['Year']>=2000]['Year']*info2000.slope)+info2000.intercept)    

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 06:45:35 2023

@author: Masud Rana
        ID: 21091274
        MSc in Data Science
        Univerisity of Hertfordshire
"""


# import modules
import pandas as pd
import matplotlib.pyplot as plt


# creating a function for lineplot
def lineplot(df, headers):
    """ This fuction will create a lineplot.
        It will take two arguments. A dataframe and a list
        containing the headers of the columns to plot.
    """

    plt.figure()

    # Plotting
    for head in headers:
        plt.plot(df["Year"], df[head], label=head)

    # labelling
    plt.xlabel("Year")
    plt.ylabel("GDP per capita")
    
    # removing white space from left and right using pandas min and max function
    plt.xlim(min(df["Year"]), df["Year"].max())

    # set Title
    plt.title('Evolution of GDP per head for USA and Asian countries')
    
    # save as png
    plt.savefig("line plot.png")
    
    # set legend
    plt.legend()


    plt.show()

    return  # Function finishes with return


# create a function for pieplot
def pieplot(df, headers):
    """
    This function will create a pie plot. It will take dataframe
        and the values of Country Name column as arguments.
    """

    plt.figure()

    # plotting
    for head in headers:
        plt.pie(df['GDP'], labels=headers)
        
    # set title
    plt.title('GDP ' + str(df['Time'][1]))

    # save as png
    plt.savefig("pie plot.png")

    plt.show()

    return  # function finishes with return


# create a function for bar stack plot
def bar_stack_plot(bang_pop):
    """ This function will make a bar stack plot for us. It will take a dataframe as an argument. 
    """

    # Stacking Bars

    plt.figure()
    
    plt.bar(bang_pop['Time'], bang_pop['Rural Population (millions)'],
            label="Rural")

    plt.bar(bang_pop['Time'], bang_pop['Urban Population (millions)'],
            bottom=bang_pop['Rural Population (millions)'], label="Urban")
    
    # set title
    plt.title("Population of Bangladesh")

    # labeling
    plt.xlabel("Year")
    plt.ylabel("Population (millions)")

    # set legend
    plt.legend()

    # save as png
    plt.savefig("bar stack plot.png")

    plt.show()

    return # Function finishes with return


# read dataset for line plot
gdp = pd.read_csv("gdp_per_capita.csv")


# change the name of the columns of gdp dataframe
gdp = gdp.rename(columns={'Time': 'Year', 'Bangladesh [BGD]': 'Bangladesh',
                          'China [CHN]': 'China', 'India [IND]': 'India', 'Pakistan [PAK]': 'Pakistan',
                          'Myanmar [MMR]': 'Myanmar', 'Sri Lanka [LKA]': 'Sri Lanka',
                          'United States [USA]': 'United States'})

# Call lineplot function and pass gdp dataframe and list of columns as arguments
lineplot(gdp, list(gdp.columns)[1:])


# read dataset for pie plot
gdp_2020 = pd.read_csv('gdp_2020.csv')
gdp_1980 = pd.read_csv('gdp_1980.csv')


# Call pieplot function and send dataframes as arguments
pieplot(gdp_2020, list(gdp_2020['Country Name']))
pieplot(gdp_1980, list(gdp_1980['Country Name']))


# read dataset for bar stack plot plot
bang_pop = pd.read_csv('bangladesh_population.csv')

# calculate population in million in bang_pop dataframe
bang_pop['Rural Population (millions)'] = bang_pop['Rural population'] / 10e6
bang_pop['Urban Population (millions)'] = bang_pop['Urban population'] / 10e6

# call bar_stack_plot function and send bang_pop dataframe as arguments
bar_stack_plot(bang_pop)

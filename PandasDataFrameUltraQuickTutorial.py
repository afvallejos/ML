#!/usr/bin/python3
# NumpyUltraQuickTutorial by Google
# https://colab.research.google.com/github/google/eng-edu/blob/master/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb
#
import numpy as np
import pandas as pd
#
# Create and populate a 5x2 NumPy array
my_data = np.array([[0,3],[10,7],[20,9],[30,14],[40,15]])
#
# Create a Python list that holds the names of the two columns.
my_column_names = ['temperature','activity']
#
# Create a data frame
my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)
#
# Print the entire DataFrame
print(my_dataframe)
#
# Create a new column named adjusted, values of activity + 2
my_dataframe["adjusted"] = my_dataframe["activity"] + 2
print(my_dataframe)
#
# Pandas provides multiple ways to isolate specific rows, columns, slices or cells in a DataFrame
print("Rows #0, #1, and #2:")
print(my_dataframe.head(3), '\n')
#
print("Row #2:")
print(my_dataframe.iloc[[2]],'\n')
#
print("Rows #1, #2, and #3:")
print(my_dataframe[1:4], '\n')
#
print("Column 'temperature':")
print(my_dataframe['temperature'])
#
# Task 1: Create a DataFrame
# Create a 3x4 pandas DataFrame in which thee columns are named Eleanor, Chidi, Tahani, and Jason.
# Populate each of the cells in the DataFrame with a random integer between 0 and 100, inclusive.
# Output the following: - The entire DataFrame
#                       - The value of the cell of row #1 of the Eleanor column 
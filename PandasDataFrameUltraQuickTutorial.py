#!/home/adams/xvalad/ML/venv/bin/python
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
#
names_columns = ['Eleanor', 'Chidi','Tahani','Jason']
#
names_data = np.random.randint(low=0, high=101,size=(3,4))
#
names_dataframe = pd.DataFrame(data=names_data , columns = names_columns,)
#
# Output the following: - The entire DataFrame
#
print(names_dataframe)
#
#                       - The value of the cell of row #1 of the Eleanor column 
#
print("Row #1 in Eleanor is:")
#
print(names_dataframe['Eleanor'].iloc[1],'\n')
#
# Create a fifth column named Janet, which is populated with the row-by-row sums of Tahani and Jason.
#
names_dataframe["Janet"] = names_dataframe["Tahani"]+names_dataframe["Jason"]
#
print("Added column Janet = Tahani + Jason:")
print(names_dataframe,'\n')
# # Copying a DataFrame
#
# Create a reference by assigning my dataframe to a new variable.
print("Experiment with reference:")
reference_to_df = names_dataframe
#
# Print tje starting value of a particular cell.
print(" Starting value of dataframe: %d" % names_dataframe['Jason'][1])
print("  Starting value of reference_to_df: %d\n" % reference_to_df['Jason'][1])
#
# Modify a cell in df.
names_dataframe.at[1,'Jason'] = names_dataframe['Jason'][1] + 5
print("  Updated dataframe: %d" % names_dataframe['Jason'][1])
print("  Updated reference_to_df: %d\n\n" % reference_to_df['Jason'][1])
#
# Create a true copy of names_dataframe
print("Experiment with a true copy.")
copy_names_dataframe = names_dataframe
#
# Print the starting value of a particular cell.
print("  Starting value of my_dataframe: %d" % names_dataframe['Jason'][1])
print("  Starting value of copy_of_my_dataframe: %d\n" % copy_names_dataframe['Jason'][1])
#
# Modify a cell in df.
names_dataframe.at[1,'Jason'] = names_dataframe['Jason'][1] + 5
print("  Updated my_dataframe: %d" % names_dataframe['Jason'][1])
print("  copy_of_my_dataframe does not get updated: %d" % copy_names_dataframe['Jason'][1])
# Verify output in last example last example
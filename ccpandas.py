'''
Pandas crash course
'''
import pandas as pd

# read csv file in a dataframe
# you can think of dataframes as excel spread sheets

df = pd.read_csv('csv_for_pandas.csv')
print(df)

# print a specific column
print(df['Trial 1'])

# print multiple columns
print(df[['Trial 1', 'Trial 2']])

# return max value in a specific column
print(df['Trial 1'].max()) 

# statistical information about the dataframe
print(df.describe())

# boolean masking, finding values that meet a conditions
filter = df['Trial 1'] > 3 
print(df[filter]) # This is similar to -> df[df['Trial 1'] > 3]

# convert a dataframe to a matrix
mat = df.as_matrix()     # In future updates this method will be replaced with -> df.values()
print(mat)
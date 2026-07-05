import pandas as pd     # import pandas library to work with Dataframes and Seried

# CREATING, READING, AND WRITING

df = pd.DataFrame({'column': ['value']})    # Create a dataFrame with parameters in form of a python dictionary (where key = column and values are list of values)
df = pd.DataFrame({'column': ['value']}, index='index_name')    # (where index= allows to create a list of index value/names for each row)
df = pd.DataFrame({'column': ['value']}, name='dataframe_name')    # (where name= allows to give a specific name to your dataset)

s = pd.Series(["data"]) # Series is similar to dataframe instead its single dimensional so a list of data would represent a column

df = pd.read_csv("file_name.csv")   # will read a CSV file (tabular form) and store it in a variable name df(dataframe)
df = pd.read_csv("file_name.csv", index_col=0)   # index_col=0 allows you to to create an index column in the start instead of a default unnamed column

df.head()   # print the first 5 rows of the DataFrame or Dataset

df.to_csv("file_name.csv", index=False)  # to save a DataFrame as a CSV file locally without the index column (True by default)

# SELECTING, INDEXING(SLICING), ASSIGNING

col_name = df['column_name']    # to select a specific whole column
col_name = df.column_name   # similar to the above one

col_name = df['column_name'][0]    # to select a specific index in a column
col_name = df['column_name'][0:10]    # to select a specific series of index of a column
col_name = df.column_name.iloc[0]   # similar as above

# iloc is used for indexing and index-based selection
row_name = df.iloc[0]   # to select the first row
row_name = df.iloc[0:10]   # to select a series of consecutive rows
row_name = df.iloc[[0, 2, 4, 6, 8]]   # to select specific rows
row_name = df.iloc[0:10, 0:10]  # first parameter/slicing/index is for selecting rows and the other is for columns

# loc is used for label-based selection as well as index based
row_name = df.loc[0:10, ["column_name"]]

# another difference between iloc and loc is the inclusion and exclusion of the right-most indexing
# df.iloc[0:100]    here 100 is not inclusive so it will print 0-99 (100 rows)
# df.loc[0:99]  here 99 is inclusive so it will print 0-99 (100 rows)

# we can also perform conditional filtering/selection
variable_name = df[df.column_name >= 10]    # this will filter only those rows where the column value is greater or equal to 10
# similarly we can use multiple condition too but we need to make sure the parenthesis are correct
# logical operators: & (and), | (or)
# all comparison operators: >, <, ==, <=, >=, != etc

# some useful pandas functions
variable_name = df[df.column_name.isin(['value1', 'value2'])]   # .isin([]) will filter out only those rows which have the given values in column

# SUMMARY (STATS), FUNCTIONS, MAPPING
df.describe()   # this will describe the dataframe and the columns with their statistics (like NULL values, total rows, shape etc)
df.column_name.describe()   # this will describe a specific column
# similarly we can find individual stastistical values instead of a whole
df.column_name.value_counts()   # this will provide us the counts for each unique value in that column
df.column_name.unique()   # this will provide us the unique values in that column
df.column_name.mean()
df.column_name.median() # similarly any mathematical stats like std deviation, variance, max, min etc
df.column_name.idxmax() # returns the index of the row/col having the maximum value (idxmin() for minimum)

# we can even use mapping to filter or select data (most useful when we need to loop the dataset)
variable_name = df.column_name.map(lambda x: x * 2) # this will multiply each value in that column known as x by its multiple of 2
variable_name = df.column_name.map(lambda x: 'value' in x).sum() # this will fetch only those rows or column with that specific value and count their frequency

# we can also make functions to modify the data instead of mapping

def func(column_name):
    return (column_name * 2)

variable_name = df.column_name.apply(func)  # this will call the function and pass the column_name and modify each row value for that column

# GROUPING AND SORTING
df.groupby('column_name').column_name.count()   # this will print the dataset by grouping the column along with their counts (similar to .value_counts())
df.groupby(['column_1', 'column_2']).apply(lambda df: df.loc[df.column_name.idxmax()])   # this will group the 2 columns together along with all the columns having the maximum value in column_name 

# another important method of groupby() is agg([]) which prints the statistical values like length, max, min etc
df.groupby('column_name').column_1.agg([len, max, min]) # so this will group the data by column_name and print the length max and min for column_1 along with the grouped column

df.reset_index()
# or
variable_name.reset_index() # this will replace current row index with the default integer index (0,1,2,....n)

variable_name.sort_index()   # this will sort the dataset by index values (ascending default)

variable_name = df.sort_values(by='column_name') # this will sort the dataset by column_name (ascending=True by default)
variable_name = df.sort_values(by='column_name', ascending=False) # this will sort the dataset by column_name in descending order
variable_name = df.sort_values(by=['column_1', 'column_2']) # we can also sort by multiple columns

# Note: All these methods such as mapping, apply, groupby, and sort_values() do not make changes in the original dataset instead it makes a copy
# so we can name that copy to a variable or just print directly using df.method_name()
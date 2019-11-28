import pandas as pd

# create dataframe from CSV File
df = pd.read_csv(r'C:/Users/301/Desktop/University.csv', names=['Name', 'University', 'GPA', 'AGE'], header=0)

# selecting Only specific Columns
df1 = df[['University', 'GPA']]

###
#### Merge Two Dataframes
df4 = df['Name']
df1['New_Name'] = df4
print(df1)

# selecting Only specific Columns  with where condition
df1 = df[['University', 'GPA']]
print('-------------------------------------------------------------')
df1 = df[['University', 'GPA']].loc[df['University'] == 'UG']
print(df1)
print('-------------------------------------------------------------')
# Where Condition
df2 = df1.loc[df1['University'] == 'UG']

print(df2)

# Group By Functions
# df3=df.groupby(['University','GPA', 'AGE']).size().reset_index().groupby('AGE').sum();
df3 = df.groupby(['University', 'AGE']).mean()
print(df3)

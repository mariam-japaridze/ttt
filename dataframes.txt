import pandas as pd
df = pd.read_csv(r'D:/csv/University.csv', names=['Name', 'University', 'GPA', 'AGE'], header=0)

print(df)

#selecting Only specific Columns
df1=df[['University','GPA' ]]
print(df1)

#### Merge Two Dataframes
df4=df['Name']
df1['New_Name']=df4


df3=df.groupby(['University','AGE']).mean()
print(df3)

df3=df.groupby(['University']).mean()
print(df3)

dfc=pd.read_csv(r'D:/csv/Country.csv', names=['Country', 'University'], header=0)
print(dfc)

df5=df.join(dfc, lsuffix='University', rsuffix='University')
print(df5)

df6=pd.merge(df, dfc, left_on='University', right_on='University')
print(df6)
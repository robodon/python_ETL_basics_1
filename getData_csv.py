import pandas as pd

column_names = ['movie_id', 'ratings', 'rating', 'number']


data_csv = pd.read_csv('/home/robin/Downloads/ml-100k/u.data', header=None, delimiter='\t', names=column_names)

df = pd.DataFrame(data_csv)
df['Absolute_Rating'] = df['ratings'] * df['rating']
#df = df.apply(lambda row: row['A'] + 2 * row['B'],axis=1)

print(data_csv.head())
print('---------------------------')
print(df)
print(df.columns)

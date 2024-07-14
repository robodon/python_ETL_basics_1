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

#-------------------------------------------------------------------------------------------
#JSON data load
path = '/home/robin/Downloads/genome_2021/movie_dataset_public_final/raw/ratings.json'

data_json = pd.read_json(path, lines=True)

dfjson = pd.DataFrame(data_json)

print(dfjson.info())
print(dfjson.columns)
print(dfjson.describe())
print(dfjson)

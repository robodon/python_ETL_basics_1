import pandas as pd

path = '/home/robin/Downloads/genome_2021/movie_dataset_public_final/raw/ratings.json'

data_json = pd.read_json(path, lines=True)

dfjson = pd.DataFrame(data_json)

print(dfjson.info())
print(dfjson.columns)
print(dfjson.describe())
print(dfjson)

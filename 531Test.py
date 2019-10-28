import pandas as pd


# Step 1
df1 = pd.read_csv('movies.csv')
df2 = pd.read_csv('ratings.csv')
df3 = pd.merge(df1, df2, on = 'movieId')
df3.set_index('movieId', inplace = True)

df3.to_csv('movieplusratings.csv')


# step 2
df1 = pd.read_csv('links.csv')
df2 = pd.read_csv('tmdb_movies_data.csv')

df3 = pd.merge(df1, df2, on = 'tmdbId')
df3.set_index('tmdbId', inplace = True)

df3.to_csv('linksAndTmdb.csv')

# step 3
df = pd.read_csv('imdb.csv')
cols_to_check = ['imdbId']
df[cols_to_check] = df[cols_to_check].replace({'tt':''}, regex=True)
df.to_csv('formattedImdb.csv', mode = 'w', index=False)


# step 4
df1 = pd.read_csv('linksAndTmdb.csv')
df2 = pd.read_csv('formattedImdb.csv')
df3 = pd.merge(df1, df2, on = 'imdbId')
df3.set_index('imdbId', inplace = True)

df3.to_csv('linksAndTmdbAndImdb.csv')


# step 5
df1 = pd.read_csv('linksAndTmdbAndImdb.csv')
df2 = pd.read_csv('movieplusratings.csv')

df3 = pd.merge(df1, df2, on = 'movieId')
df3.set_index('movieId', inplace = True)

df3.to_csv('MovieLensAndImdbAndTmdb.csv')
import pandas as pd

s = pd.read_csv('./pandas-workout-data/nyc-temps.txt').squeeze('columns')

df = pd.DataFrame({'temp': s,
                  'hour': [0, 3, 6, 9, 12, 15, 18, 21] * 91
                  })

print("Original df:")
print(df.head(20))
# update values in temp column so that any value less than 0 is set to 0

df.loc[df['temp'] < 0, 'temp'] = 0

print("Update df:")
print(df.head(20))


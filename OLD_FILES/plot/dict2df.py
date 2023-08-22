import pandas as pd
import ast

file = open("iterations_400.txt", "r")

contents = file.read()
dictionary = ast.literal_eval(contents)

file.close()

print(type(dictionary))


df = pd.DataFrame(data=dictionary)
print(df)

df_csv = df.to_csv(index=False)
path = '/Users/apanova/OneDrive/Documents/ConLab/MorphComplexity/morph-complexity/plot/phonetic_data.txt'
f = open (path, 'w', encoding = 'utf-8')
f.write (df_csv)
f.close

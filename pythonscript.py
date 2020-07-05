import json
import pandas as pd
import re

#turn the json data into a dataframe
import pandas as pd
df1 = pd.read_json (r'recipes.json', lines=True)
df1.head()

#use regex to get all the versions of "chilies"
df2 = df1[df1['ingredients'].str.contains(r'chil(?!$)')]
df2 = pd.DataFrame(df2)

#using regex to extract only the numerical data
df2['PTIME'] = df2['prepTime'].str.extract('(\d)', expand=True)
df2['CTIME'] = df2['cookTime'].str.extract('(\d)', expand=True)

#combine the times to get a total
df2['totalt'] = df2['PTIME'] + df2['CTIME']

#drop rows with NaN as not applicable

df2.dropna(inplace=True)

#change the type to int in order to use in function

df2['totalt'].astype('int')

#creating the difficulty field using a function

def get_time(x):
    if int(x) > 60:
        return "Hard"
    elif int(x) >=30 and int(x) <= 60:
        return "Medium"
    elif int(x) < 30:
        return "Easy"
    else:
        return "Unknown"
    return tag
df2['difficulty'] = df2['totalt'].apply(lambda x : get_time(x))

#Write to csv
df2.to_csv('hellofresh.csv')


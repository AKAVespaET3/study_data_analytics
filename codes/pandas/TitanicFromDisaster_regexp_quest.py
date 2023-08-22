import pandas as pd

df_TiTanic = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
df_TiTanic

df_Name = df_TiTanic['Name']
df_Name = pd.DataFrame(df_Name)
print(df_Name)

pattern = r'^([A-Za-z]+)'
df_Name['FirstName'] = df_Name['Name'].str.extract(pattern)

print(df_Name['FirstName'])

             
# 0       Braund
# 1      Cumings
# 2    Heikkinen
# 3     Futrelle
# 4        Allen
# ..         ...
# 886   Montvila
# 887     Graham
# 888   Johnston
# 889       Behr
# 890     Dooley

df_Name_extract.isnull().sum()

# 결혼여부

pattern_1 = r', ([A-Za-z]+)\.'
df_Name['Married'] = df_Name['Name'].str.extract(pattern_1)

print(df_Name['Married'])

df_Name['Married'].value_counts()

# Mr          517
# Miss        182
# Mrs         125
# Master       40
# Dr            7
# Rev           6
# Col           2
# Major         2
# Mlle          2
# Capt          1
# Don           1
# Jonkheer      1
# Lady          1
# Mme           1
# Ms            1
# Sir           1
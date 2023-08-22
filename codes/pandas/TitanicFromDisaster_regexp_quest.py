import pandas as pd

df_TiTanic = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
df_TiTanic

df_Name = df_TiTanic['Name']
df_Name = pd.DataFrame(df_Name)
print(df_Name)

pattern = r'^([A-Za-z]+)'
df_Name['FirstName'] = df_Name['Name'].str.extract(pattern).copy()

print(df_Name['FirstName'])

# 결혼여부

pattern_1 = r'(Mrs?)'
df_Name['Married'] = df_Name['Name'].str.extract(pattern_1).copy()
print(df_Name['Married'])
df_Name.dropna()
df_Name
#                                                   Name FirstName Married
# 0                              Braund, Mr. Owen Harris    Braund      Mr
# 1    Cumings, Mrs. John Bradley (Florence Briggs Th...   Cumings     Mrs
# 3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  Futrelle     Mrs
# 4                             Allen, Mr. William Henry     Allen      Mr
# 5                                     Moran, Mr. James     Moran      Mr
# ..                                                 ...       ...     ...
# 883                      Banfield, Mr. Frederick James  Banfield      Mr
# 884                             Sutehall, Mr. Henry Jr  Sutehall      Mr
# 885               Rice, Mrs. William (Margaret Norton)      Rice     Mrs
# 889                              Behr, Mr. Karl Howell      Behr      Mr
# 890                                Dooley, Mr. Patrick    Dooley      Mr

# [647 rows x 3 columns]


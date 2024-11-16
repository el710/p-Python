# импорт пакетов
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib

plt.style.use('ggplot')

from matplotlib.pyplot import figure

# %matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

# чтение данных
df = pd.read_csv('D:\EL710\p-Python\sberbank.csv')

# shape and data types of the data
print(f"Shape: {df.shape}")
print(f"Data types: \n{df.dtypes}\n")

# отбор числовых колонок
df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values
print(f"Numeric data: \n {numeric_cols}\n")

# отбор нечисловых колонок
df_non_numeric = df.select_dtypes(exclude=[np.number])
non_numeric_cols = df_non_numeric.columns.values
print(f"Context data: \n {non_numeric_cols}")

input()
###############################################################

cols = df.columns[:30] # первые 30 колонок
# определяем цвета
# зеленый - пропущенные данные, синий - не пропущенные
colours = ['#000099', '#1aff12']
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))

input()
###############################################################

for col in df.columns:
  missed = np.mean(df[col].isnull())
  print(f"{col}: {missed:.02f} ({round(missed * 100)}%)")


input()
###############################################################

for col in df.columns:
    missing = df[col].isnull()
    num_missing = np.sum(missing)

    if num_missing > 0:
        print('created missing indicator for: {}'.format(col))
        df['{}_ismissing'.format(col)] = missing

ismissing_cols = [col for col in df.columns if 'ismissing' in col]
df['num_missing'] = df[ismissing_cols].sum(axis=1)

  # Создание DataFrame для гистограммы
num_missing_counts = df['num_missing'].value_counts().reset_index()
num_missing_counts.columns = ['num_missing_values', 'count']
num_missing_counts = num_missing_counts.sort_values(by='num_missing_values')

  # Вывод таблицы с пропущенными значениями
missing_table = df.isnull().sum().reset_index()
missing_table.columns = ['column', 'num_missing']
missing_table = missing_table[missing_table['num_missing'] > 0]
print("Таблица c количеством пропущенных значений в каждом столбце:")
print(missing_table)

  # Построение гистограммы
plt.figure(figsize=(10, 6))
plt.bar(num_missing_counts['num_missing_values'], num_missing_counts['count'], color='skyblue')
plt.xlabel('Number of Missing Values per Row')
plt.ylabel('Number of Rows')
plt.title('Histogram of Missing Values per Row')
plt.xticks(num_missing_counts['num_missing_values'])  # Установить метки по оси X для всех значений
plt.show()

input()
###############################################################

ind_missing = df[df['num_missing'] > 35].index
df_less_missing_rows = df.drop(ind_missing, axis=0)

cols_to_drop = ['hospital_beds_raion']
df_less_hos_beds_raion = df.drop(cols_to_drop, axis=1)

med = df['life_sq'].median()
print(med)
df['life_sq'] = df['life_sq'].fillna(med)

df['life_sq']

df_numeric = df.select_dtypes(include=[np.number])
numeric_cols = df_numeric.columns.values

for col in numeric_cols:
    missing = df[col].isnull()
    num_missing = np.sum(missing)

    if num_missing > 0:  # only do the imputation for the columns that have missing values.
        print('imputing missing values for: {}'.format(col))
        df['{}_ismissing'.format(col)] = missing
        med = df[col].median()
        df[col] = df[col].fillna(med)


# категориальные признаки
df['sub_area'] = df['sub_area'].fillna('_MISSING_')

# численные признаки
df['life_sq'] = df['life_sq'].fillna(-999)

df['life_sq'].hist(bins=100)

df.boxplot(column=['life_sq'])

df['life_sq'].describe()

df['ecology'].value_counts().plot.bar()

input()
###############################################################

num_rows = len(df.index)
low_information_cols = []

for col in df.columns:
    cnts = df[col].value_counts(dropna=False)
    top_pct = (cnts/num_rows).iloc[0]

    if top_pct > 0.95:
        low_information_cols.append(col)
        print('{0}: {1:.5f}%'.format(col, top_pct*100))
        print(cnts)
        print()

# отбрасываем неуникальные строки
df_dedupped = df.drop('id', axis=1).drop_duplicates()

# сравниваем формы старого и нового наборов
print(df.shape)
print(df_dedupped.shape)

key = ['timestamp', 'full_sq', 'life_sq', 'floor', 'build_year', 'num_room']
df.fillna(-999).groupby(key)['id'].count().sort_values(ascending=False).head(20)

key = ['timestamp', 'full_sq', 'life_sq', 'floor', 'build_year', 'num_room']
df_dedupped2 = df.drop_duplicates(subset=key)

print(df.shape)
print(df_dedupped2.shape)

input()
###############################################################
df['sub_area'].value_counts(dropna=False)

df['sub_area_lower'] = df['sub_area'].str.lower()
df['sub_area_lower'].value_counts(dropna=False)

print (df['timestamp'])

df['timestamp_dt'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d')
df['year'] = df['timestamp_dt'].dt.year
df['month'] = df['timestamp_dt'].dt.month
df['weekday'] = df['timestamp_dt'].dt.weekday

print(df['year'].value_counts(dropna=False))
print()
print(df['month'].value_counts(dropna=False))

input()
###############################################################

from nltk.metrics import edit_distance

df_city_ex = pd.DataFrame(data={'city': ['torontoo', 'toronto', 'tronto', 'vancouver', 'vancover', 'vancouvr', 'montreal', 'calgary']})

df_city_ex['city_distance_toronto'] = df_city_ex['city'].map(lambda x: edit_distance(x, 'toronto'))
df_city_ex['city_distance_vancouver'] = df_city_ex['city'].map(lambda x: edit_distance(x, 'vancouver'))
df_city_ex

msk = df_city_ex['city_distance_toronto'] <= 2
df_city_ex.loc[msk, 'city'] = 'toronto'

msk = df_city_ex['city_distance_vancouver'] <= 2
df_city_ex.loc[msk, 'city'] = 'vancouver'

df_city_ex

input()
###############################################################
df_add_ex = pd.DataFrame(['123 MAIN St Apartment 15', '123 Main Street Apt 12   ', '543 FirSt Av', '  876 FIRst Ave.'], columns=['address'])
df_add_ex

df_add_ex['address_std'] = df_add_ex['address'].str.lower()
df_add_ex['address_std'] = df_add_ex['address_std'].str.strip()
df_add_ex['address_std'] = df_add_ex['address_std'].str.replace('\\.', '')
df_add_ex['address_std'] = df_add_ex['address_std'].str.replace('\\bstreet\\b', 'st')
df_add_ex['address_std'] = df_add_ex['address_std'].str.replace('\\bapartment\\b', 'apt')
df_add_ex['address_std'] = df_add_ex['address_std'].str.replace('\\bav\\b', 'ave')

df_add_ex
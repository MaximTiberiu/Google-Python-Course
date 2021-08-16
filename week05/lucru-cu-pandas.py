import pandas as pd
import matplotlib.pyplot as plt

# print(pd.__version__)

# pd.Series
# a = [1, 7, 2]
# variabila = pd.Series(a, index=['x', 'y', 'z'])
# print(variabila)

# pd.DataFrame
# data = {
#     "key1": [0, 1, 2],
#     "key2": [3, 4, 5]
# }
#
# variabila = pd.DataFrame(data, index=['linie1', 'linie2', 'linie3'])
# print(variabila.loc[['linie1', 'linie2']])
# print(variabila['key2']['linie1'])

# pd.read_csv
# df = pd.read_csv("EXEMPLU.csv")
# print(df)

# df = pd.read_csv("test.csv")
# print(df)

# # inlocuire Nan cu 0
# df2 = df.fillna(0) # in alt dataframe
# print(df2)

# df.fillna(0, inplace=True)
# print(df)  # in acelasi dataframe

# afisarea primelor n inregistrari (default = 5)
# print(df.head(3))
#
# afisarea ultimelor n inregistrari (default = 5)
# print(df.tail(3))

# update pe inregistrare
# df.loc[7, "AL"] = 45
# print(df)

# df.replace(': ', 999, inplace=True)
# df.replace(':', 999, inplace=True)
# print(df)

# transpunerea setului de date
# print(df.transpose())

# salvare in CSV
# df.to_csv("new_test.csv")

# redefinire nume coloane
# df.rename(columns={"AL": "Col_1"}, inplace=True)
# print(df)

# redefinire index
# df.rename(index={0: "linie1"}, inplace=True)
# print(df)

# adaugare coloane
# df['CV'] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(df)

# descriere
# print(df.describe())

# calculul mediei
# print(df.mean())

# ---------------- plotare grafice ------------------------
# histograma
# df['AT'].plot(kind='hist')
# plt.show()

# grafic puncte
# df.plot(kind='scatter', x='AT', y='BE')
# plt.show()

# afisare valori de corelatie
# print(df.corr())

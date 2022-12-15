import pandas as pd

df = pd.read_csv("Negara.csv")
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Data Frame:")
print(df, "\n")

print("Data Mean:")
print(mean, "\n")

print("Data Standard Deviation:")
print(std, "\n")

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandardDeviation.csv')

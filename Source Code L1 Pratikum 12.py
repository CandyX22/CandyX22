import pandas as pd

data= pd.read_csv("negara.csv")

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print(data)
print(mean)
print(std)

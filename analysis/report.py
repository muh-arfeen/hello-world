import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("output/dataset.csv")
print(data.head(3))
print(data.shape)
##fig = data.age.plot.hist().get_figure()
##fig.savefig("output/descriptive.png")
##fig2=data.age.plot.pie().get_figure()
##fig2.savefig("output/descriptive2.png")
import seaborn as sns
sns.set_theme()
patid = data
print(patid.head(10))
fig=sns.scatterplot(data=patid, x='age', y='patient_id', hue='sex').get_figure()
fig.savefig("output/descriptive3.png")
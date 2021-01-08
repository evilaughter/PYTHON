import csv 
import pandas as p
import plotly.figure_factory as ff
 
df=p.read_csv("data108.csv")
f=ff.create_distplot([df['Avg Rating'].tolist()],['Avg'])
f.show()

import pandas as pd 
import csv 
import plotly.figure_factory as ff

df = pd.read_csv ("Mdata.csv")
fig = ff.create_distplot ([df["Mobile Brand"].tolist()],["Mobile"],show_hist=False) 
fig.show()
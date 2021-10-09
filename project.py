import pandas as pd
import plotly.express as pe
df = pd.read_csv("Covid.csv")
graph = pe.line(df,x="date",y="cases",color="country")
graph.show()

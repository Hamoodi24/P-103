import pandas as pd
import plotly.express as px

ds = pd.read_csv('project103.csv')

segment = px.scatter(ds, x = 'date', y = 'cases', color = 'Country' )


segment.show()
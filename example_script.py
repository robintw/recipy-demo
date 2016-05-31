import recipy
import pandas as pd
from matplotlib.pyplot import *

data = pd.read_csv('data.csv')

data.plot(x='year', y='temperature')
savefig('graph.png')

data.temperature = data.temperature + 12345
data.to_csv('output.csv')

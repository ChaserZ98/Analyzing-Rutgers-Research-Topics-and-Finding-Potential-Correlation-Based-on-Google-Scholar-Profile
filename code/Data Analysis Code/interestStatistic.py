import numpy as np
import pandas as pd
import json
import plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import scipy

a2iData = json.load(open("Data/googlescholars.json", encoding='utf-8'))[3]['data']
interestData = json.load(open("Data/googlescholars.json", encoding='utf-8'))[5]['data']

interestDict = {}
for element in a2iData:
	if str(element['Aid']) in interestDict.keys():
		interestDict[element['Aid']].append(interestData[int(element['Iid']) - 1].get('name'))
	else:
		if interestData[int(element['Iid']) - 1].get('name') == '':
			continue
		interestDict[element['Aid']] = [interestData[int(element['Iid']) - 1].get('name')]
# print(interestDict)
dataset = []
for key, value in interestDict.items():
	dataset.append(value)

dataset = [len(element) for element in dataset]
a = 0
for element in dataset:
	a += element
print(a)
print(len(dataset))
median = np.median(dataset)
mean = np.mean(dataset)
sd = np.std(dataset)
maximum = np.max(dataset)
minimum = np.min(dataset)
print("Mean: %.2f" % mean)
print("Median: %.2f" % median)
print("Standard Deviation: %.4f" % sd)
print("Maximum: %d" % maximum)
print("Minimum: %d" % minimum)
exit()
trace = go.Box(
	y=dataset,
	name = 'Box Plot',
	boxpoints='all',
	jitter=0.3,
	marker = dict(color = 'rgb(64, 70, 110)',),
	)
layout = go.Layout(
	width=500,
	yaxis=dict(
		title='Interest Number per Researcher',
		zeroline=False
		)
	)
data = [trace]
fig = go.Figure(data=data, layout=layout)
py.offline.iplot(fig, filename='Interest-box-plot')
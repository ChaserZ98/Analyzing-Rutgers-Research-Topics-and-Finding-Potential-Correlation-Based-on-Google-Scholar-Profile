import numpy as np
import pandas as pd
import json
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import os
import matplotlib.pyplot as plt
# from pandas.table.plotting import table

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

dataset_1 = [element for element in dataset if len(element)==1]
# print(len(dataset_1))
dataset_2 = [element for element in dataset if len(element)>1]
# print(len(dataset_2))
# print(dataset_2)
def aprioriAlgorithm(dataset, min_support):
	te = TransactionEncoder()
	te_ary = te.fit(dataset).transform(dataset_2)
	df = pd.DataFrame(te_ary, columns=te.columns_)
	# print(df)
	frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
	frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
	return frequent_itemsets

# frequent_items = aprioriAlgorithm(dataset, 0.0015)
# print(frequent_items[frequent_items['length'] == 1])

frequent_itemsets = aprioriAlgorithm(dataset_2, 0.0014)
frequent_itemsets['support'] = frequent_itemsets['support'] * 2001
# print(frequent_itemsets)
print(frequent_itemsets[frequent_itemsets['length'] == 2].sort_values(by=['support'], ascending=False).head(20))
# ax = plt.subplot(111, frame_on=False)
# ax.xaxis.set_visible(False)
# ax.yaxis.set_visible(False)
# table(ax, frequent_itemsets[frequent_itemsets['length'] == 2].sort_values(by=['support'], ascending=False).head(20))
# plt.savefig('frequent_itemsets.')
# frequent_itemsets.to_json(r'Data/frequent_itemsets.json')
import pandas as pd
from color import Color
data = pd.read_csv('dataset.csv')
if(data.columns[-1] != 'class'):
    data.rename(columns={data.columns[-1]: 'class'}, inplace=True)
tupleX = dict()
print('Enter the following details for unseen data to predict the output')
for column in data.columns[:-1]:
    tupleX[column] = input('Enter value for {} {}: '.format(column, data[column].unique()))

clas =  list(data['class'].unique())

prob_class = dict()
for _ in clas:
    prob_class[_] = round(data.loc[data['class'] == _]['class'].count() / data['class'].count(), 2)

# print('\n Probability of each class of traininig tuple: ',prob_class)
prob_attribute = dict()
for i in tupleX:
    for j in clas:
        prob_attribute[i, j] = round(data.loc[data[i] == tupleX[i]].loc[data['class'] == j][i].count() / data.loc[data['class'] == j]['class'].count(), 2)
# print('\n Conditional probability of each attributes: ', prob_attribute)

prob_tuple_class = dict()
for k in clas:
    init_prob = 1
    for m in prob_attribute:
        if(k in m):
            init_prob = init_prob * prob_attribute[m]
    prob_tuple_class[k] = round(init_prob, 3)
# print('\n Probability of tuple w.r.t class: ', prob_tuple_class)

max_prob=dict()
for m,n in prob_class.items():
    if(m in prob_tuple_class):
        max_prob_value = prob_class[m] * prob_tuple_class[m]
        max_prob[m] = max_prob_value
# print('\n Maximizing Probability: ', max_prob)
v = list(max_prob.values())
k = list(max_prob.keys())
print("\n{:-^60s}".format(" Output ")) 
print(Color.WARNING + '\n The probability class for given unseen data is: ' + Color.BOLD + Color.UNDERLINE + '{}'.format(k[v.index(max(v))]) + Color.ENDC)
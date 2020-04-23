import dataset, datafreeze

from datafreeze import freeze

#database initialization
db = dataset.connect('sqlite:///index.db')
table = db['resp_table']

result = db['resp_table'].all()
datafreeze.freeze(result, format='csv', filename='export.csv')
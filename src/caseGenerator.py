import pandas as pd
import copy
from random import randint

model = pd.read_csv('../data/model.csv')
col = model.columns
values = model.values.tolist() 

newValues = []
print(col)
for i in range(5000):
    #print(randint(0, len(values)))
    #print(values[randint(0, len(values) - 1)])
    temp = copy.deepcopy(values[randint(0, len(values) - 1)])
    for i in range(len(temp) - 1):
        if randint(1, 10) > 10:
            if temp[i] == 0:
                temp[i] = 1
            else:
                temp[i] = 0
    newValues.append(temp)

output = pd.DataFrame(newValues, columns =col)
print(output)
output.to_csv('../data/test1.csv')
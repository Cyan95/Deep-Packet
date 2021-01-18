from pathlib import Path
# import csv
from config import *
#
# csv_file = str(flow_path + "/" + "nm.csv")
#
# with open(csv_file, 'r') as f:
#     writer = csv.writer(f)
#     next(writer)
#     # print(type(reader))
#     for flow in writer:
#         print("original", flow)
#         flow[7, -1] = flow[7, -1]*0.5
#         print("modified", flow)
#         writer.writerow()
# # for i in flows:
# #    print(i, ':', flows[i])

import pandas as pd
import numpy as np
'''
data = pd.read_csv(test_path + "/" + "xx.csv")
print(type(data))
data.replace(0, -1, True)
print(data)
'''
# data = pd.read_csv(test_path + "/" + "nm.csv")
# print(data.columns[-1])
# print(data.columns[7:])

# max=2

maxDict={}


for csv_file in sorted(Path(flow_path).iterdir()):
    print(csv_file)
    data = pd.read_csv(csv_file)
    data.replace(np.NAN, -1, True)
    data.replace("Infinity", -2, True)
    data.replace(np.inf, -2, True)
    data.replace("inf", -2, True)
    for column in data.columns[7:-1]:
        tmp = data[column].max()
        if (not maxDict.__contains__(column)) or tmp > maxDict[column]:
            maxDict[column] = tmp
            print("maxDict[%s] = "%column, maxDict[column])
            # data[column]=data[column]/max

for k in maxDict:
    if maxDict[k] == 0:
        maxDict[k] = 1

print(maxDict)
header=maxDict.keys()
value=maxDict.values()

# maxDict.to_csv(test_path + "/"+'max.csv', index=False, encoding='utf-8')
with open(test_path + "/"+'max.csv', 'w') as f:
    for h in header:
        f.write(h+",")
    f.write("\n")
    for v in value:
        f.write(str(v)+",")
    # f.write(header + "\n" + value)
    # [f.write('{0},{1}\n'.format(key, value)) for key, value in maxDict.items()]


# data.to_csv(test_path + "/"+'nmd.csv', index=False, encoding='utf-8')
# data[u'buy_place'] = data[u'buy_place'].astype(str)
# data[u'buy_place'] = data[u'buy_place'].apply(lambda x :x.split(' ')[-1])
# data.to_csv('price.csv',index=False, encoding='utf-8')

# import re
#
# str = "ftps_down_1a_00000_20150501223705.pcap" + '_Flow.csv'
# str = re.sub(r"_00.*\.pcap", ".pcap", str)
# print(str)


from config import *
import pandas as pd
import numpy as np

limit = pd.read_csv(test_path+"/max.csv").values[0][:-1]
print(limit)
print(np.shape(limit))
print(limit[-1])
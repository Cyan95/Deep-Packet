import csv

dict={}

with open('../csv/email1a.pcap_Flow.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
    next(reader)
    for row in reader:
        print(row[1:5])
        quintuple=""
        for i in row[1:5]:
            quintuple+=i+","
        quintuple=quintuple[:-1]
        print(quintuple)
        if quintuple in dict:
            dict[quintuple]+=1
        else:
            dict[quintuple]=1

for i in dict:
    print(i,':',dict[i])
import os
import sys
import csv
myDict =  {
    'CompanyName' : 'SAP',
    'Market Cap' : '123',
    'Volume' : '123',
    'Total Revenue 2020' : '123',
    'Total Revenue 2019' : '123',
    'Total Revenue 2018' : '123',
    'Total Revenue 2017' : '123',
    'grossProfit 2020' : '123',
    'grossProfit 2019' : '123',
    'grossProfit 2018' : '123',
    'grossProfit 2017' : '123',
    'Total ESG' : '123',
    'eScore' : '5',
    'sScore' : '5',
    'gScore' : '5',
    'esgLevel' : '5',
    'esgPercent' : 'Med'
}
# indicator = []
new_list = list(myDict.keys())
new_list2 = list(myDict.values())

print(new_list)

with open('sample.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(new_list)
    write.writerow(new_list2)


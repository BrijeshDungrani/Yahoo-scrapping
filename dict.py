myText = '''Products and Activities Significant Involvement
Alcoholic Beverages No
Adult Entertainment Yes
Gambling No
Tobacco Products No
Animal Testing No
Fur and Specialty Leather No
Controversial Weapons No
Small Arms No
Catholic Values
No
GMO No
Military Contracting No
Pesticides No
Thermal Coal No
Palm Oil No '''
myDict = {
    
}
all = myText.split()
NoIndex = []
YesIndex = []
allIndex = []
factor = []
tempList = []
tempstr = ""
start = 5
lastIndex = "Yes"
for index,each in enumerate(all):
    
    if each == 'No':
        NoIndex.append(index)
        allIndex.append(index)
        tempList = all[start:index]
        tempstr = ' '.join(tempList)
        factor.append(tempstr)
        tempstr =  ''
        tempList = []
        lastIndex = 'No'
        start = index
       

    if each == "Yes" :
        YesIndex.append(index)
        allIndex.append(index)
        tempList = all[start:index]
        tempstr = ' '.join(tempList)
        factor.append(tempstr)
        tempstr =  ''
        tempList = []
        lastIndex = 'Yes'
        start = index

factor.append(lastIndex)

keyList = []
valList = []
for ff in factor:
    if not 'No' in ff and not 'Yes' in ff:
        keyList.append(ff)
    elif 'No' in ff:
        valList.append("No")
        ff = ff[3:]
        keyList.append(ff)
    elif 'Yes' in ff:
        valList.append("Yes")
        ff = ff[4:]
        keyList.append(ff)
    
keyList.pop()  

zip_iterator = zip(keyList,valList)
myDict = dict(zip_iterator)

print(myDict)




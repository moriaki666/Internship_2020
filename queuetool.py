import pandas as pd
import numpy as np

# The only thing needed for the tool to function is to specify the .csv file in the read_csv function.
# This can done by writing read_csv(r'/pathtothedata/) as shown below
#tool_data = pd.read_csv(r'C:\Users\manas\Downloads\tooldatafinal.csv')
tool_data = pd.read_csv(r'tooldatafinal.csv')
tool_data.set_index('INOUTSEQ', inplace=True)
tool_data = tool_data.drop(['SEQ'], axis=1)
# print(tool_data)
col_names = tool_data.columns.values
# print(col_names)

# The following lines of code help clean the data a little bit and helps read some specific column and row data.
tool_data['CURRENTPOS'] = tool_data['CURRENTPOS'].replace(np.nan, 0)
# print(tool_data)
tool_data = tool_data.drop(['TRUCK_IN', 'ADDRESS_TRUCKERIN'], axis=1)
td = tool_data.loc[tool_data['CURRENTPOS'] != 0]
td.sort_values(by=['INDATE'], ascending=True)
td['CURRENTPOS'].astype(str)
td1 = td['CURRENTPOS'].values
x = len(td1)
# print(td1)

p1_list = pd.DataFrame()
p2_list = pd.DataFrame()

# Create a priority list for ADR containers by identifying which containers are ADR and where they are stacked.

print("Priority List for ADR Containers")
for i in range(x):
    if td1[i] <= '27':
        if td1[i].endswith('.1') or td1[i].endswith('.2'):
            p1_list = p1_list.append(td.loc[td['CURRENTPOS'] == td1[i]])
p1_list.sort_values(['CURRENTPOS', 'INDATE'], inplace=True, ascending=True)
print(p1_list.to_string())

# Create a priority list for non-ADR containers by identifying which containers are ADR and where they are stacked.

print("Priority List for non-ADR containers")
for i in range(x):
    if td1[i] >= '27':
        if td1[i].endswith('.1') or td1[i].endswith('.2'):
            p2_list = p2_list.append(td.loc[td['CURRENTPOS'] == td1[i]])
p2_list.sort_values(['CURRENTPOS', 'INDATE'], inplace=True, ascending=True)
print(p2_list.to_string())

# print(tool_data.to_string())
# This is used to generate the csv files for the priority lists that can be used later on
# p1_list.to_csv('adrprioiritylist.csv')
# p2_list.to_csv('nonadrprioritylist.csv')

import pandas as pd

df = pd.read_csv(r'C:\Users\manas\Downloads\CStock.csv')
df = df.drop(df[df.CNTRSTATUS == 'PLANNED'].index)
df.set_index('UNIT_IN', inplace=True)
col_names = df.columns.to_list()
df = df.drop(['OUTDATE', 'UNIT_OUT', 'VOYTERM_OUT', 'ADDRESS_TRUCKEROUT', 'INOUTSEQ'], axis=1)
# print(df.columns.to_list())
# print(df)

df2 = pd.read_csv(r'C:\Users\manas\Downloads\CDet.csv')
df2 = df2.dropna()
df2.set_index('UNIT_IN', inplace=True)
# print(df2)
# print(df2['CURRENTPOS'])
df_final = pd.merge(left=df, right=df2, how='left', left_on='UNIT_IN', right_on='UNIT_IN')
# print(df_final)
df_list = [df_final.columns.values.tolist()] + df_final.values.tolist()
# print(df_list)
p = len(df_list[1])
# print(p)
q = df_list[10][16]
q = list(q.split("."))


# print(q)
# print(type(q))


def convert_list(string: str) -> list:
    l_p = list(string.split("."))
    return l_p


i = 1
for i in range(1, len(df_list)):
    df_list[i][16] = str(df_list[i][16])
    df_list[i][16] = list(df_list[i][16].split("."))
    i = i + 1

print("Queue - Ready to be Shipped ")
df_list.pop(0)
#print(df_list)
#print(df_final)
print(df_final.to_string())




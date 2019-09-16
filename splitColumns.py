#Created by pablo.lopez
#Global Variables#
import pandas as pd
df = pd.read_excel("file.xlsx",sheet_name='Sheet1')
export_file = "export.xlsx"
ldfa1 = []
ldfa3 = []
ldfb4 = []
lista =[]
lista2 =[]
lista3 = []
ldf4 = []
a = []
# end of global variables #
# Columns Name #
COL1 = 'COL_NAME_TO_SPLIT'
COL2 = 'COL_NAME_TO_SPLIT_2'
#if more columns need to be added, add here the name of the column to split

# End of Columns #
# start of split columns #
#first column
dfa1 = df[COL1].str.split(',',expand=True)
for i in range(len(dfa1.columns)):
    i = str(i+1)
    ldfa1.append(COL1+i)

dfa1.columns = [ldfa1]
ldfa1 = a
# second column
ldfa2 = []
dfa2 = df[COL2].str.split(',',expand=True)
for i in range(len(dfa2.columns)):
    i = str(i+1)
    ldfa2.append(COL2+i)

dfa2.columns = [ldfa2]
ldfa2 = a
#end of spliting columns #

# Concat columns end export #
#union of df, if you have more columns, just replicate the second column with the name of the column from the excel
df_concat= pd.concat([dfa1,dfa2], axis = 1, sort = False)

#excel export
df_concat.to_excel(export_file,index=False)
print("Export complete, file exported: "+export_file)

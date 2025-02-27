import pandas as pd

df1=pd.read_excel("oc1.xlsx")
df2=pd.read_excel("oc2.xlsx")

df_result = pd.concat([df1, df2], ignore_index=True)

df_result.to_excel("tabela_resultado.xlsx")
import pandas as pd
a=pd.read_excel("C:/Users/m.han/Downloads/C1822002_LG생활건강_화장품.xlrd")
b=pd.read_excel("C:/Users/m.han/Downloads/C1822034_LG생활건강_더페이스샵.xlrd")
c=pd.read_excel("C:/Users/m.han/Downloads/C3642001_씨앤피코스메틱스.xlrd")
d=pd.read_excel("C:/Users/m.han/Downloads/C5323001_(주)더페이스샵.xlrd")
data = pd.concat([a,b,c,d])
data.to_excel("C:/Users/m.han/Downloads/2020-01-31.xlsx",index=False,header = None)
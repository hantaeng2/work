#Pycharm에서는 경로 지정시 C드라이브 주소를 써야함
import pandas as pd
a=pd.read_excel("C:/Users/m.han/Downloads/Myeong-dong_Sinsegae_En__2020-01-31.xls")
b=pd.read_excel("C:/Users/m.han/Downloads/Myeong-dong_Sinsegae_Ja__2020-01-31.xls")
c=pd.read_excel("C:/Users/m.han/Downloads/Myeong-dong_Sinsegae_Ko__2020-01-31.xls")
d=pd.read_excel("C:/Users/m.han/Downloads/Myeong-dong_Sinsegae_Zh__2020-01-31.xls")
data = pd.concat([a,b,c,d])
data.to_excel("C:/Users/m.han/Downloads/2020-01-31.xlsx",index=False,header = None)
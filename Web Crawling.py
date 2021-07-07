# cmd에서 먼저 pip install requests beautifulsoup4

"""from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.weather.go.kr/weather/climate/past_cal.jsp")
bsObject = BeautifulSoup(html, "html.parser")

a = print(bsObject.find_all('td',class_='align_left'))


import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('http://www.weather.go.kr/weather/climate/past_cal.jsp')
html = response.text
soup = BeautifulSoup(html,'html.parser')

for tag in soup.select('td[class=align_left]'):
    print(tag.text)"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.weather.go.kr/weather/climate/past_cal.jsp')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
temperatures = soup.find_all('td',class_='align_left')
for temperature in temperatures :
    if len(temperature) >= 2:
        result1 = temperature.get_text()
        print(result1)


    #else:
     #   result2 = temperature.get_text()
     #  print(result2)
#a = pd.DataFrame({'기온':result1})
#a.to_excel("C:Downloads/자료")
#b = pd.concat[result1,result2]
#print(a)
#a = temperature.get_text()
#a.to_txt("C:/Downloads/save.txt")

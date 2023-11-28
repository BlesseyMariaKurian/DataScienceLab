print("Register no:SJC22MCA-2019 \n:Name:Blessey Maria Kurian \n:Batch:S3 MCA \n*****************\n")
import requests
from bs4 import BeautifulSoup
def getdata(url):
   r=requests.get(url)
   return r.content
htmldata=getdata("https://www.w3schools.blog/android-tutorial")
soup=BeautifulSoup(htmldata,"html.parser")
data=''
pr=len(soup.find_all('p'))
print("P tag: ",pr)
for data in  soup.find_all('p'):
   print(data.get_text())




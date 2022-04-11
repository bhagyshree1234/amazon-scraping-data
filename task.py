import csv
import requests
from bs4 import BeautifulSoup
import json
file = open("Amazon Scraping.csv")

a=type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
header
rows = []
for row in csvreader:
    rows.append(row)

i=0
rowse=rows[2:3]
while i<len(rowse):
    a1=rowse[i][2:5]

    a=a1[0]
    b=a1[1]
    link="https://www.amazon.{b}/dp/{a}".format(a=a1[0],b=a1[1])

    values=[]
    headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0","Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    res = requests.get(link,headers=headers)
    statuscode1=res.status_code
    if statuscode1==200:
        soup=BeautifulSoup(res.content,"html.parser")
    
        title=soup.find(id="productTitle").get_text()
        # price=soup.find()
        print(title)
        values.append(title)
    else:
        print("api not found")
    list=[]
    dictionary={}
    keys=["title"]
    for i in range(len(keys)):
        dictionary[keys[i]]=values[i]
        list.append(dictionary)
    with open ("task.json","w") as file:
        json.dump(list,file,indent=2)
    i+=1
file.close




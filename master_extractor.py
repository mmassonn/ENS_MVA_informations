#Extraction dataset
#Import module
import os
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

#create list of urls
urls=[]

#importer les urls des pages regroupant l'ensemble des avis de radiothérapie
url1 = "https://www.master-mva.com/cours-1er-semestre/"
url2 = "https://www.master-mva.com/cours-2nd-semestre/"

urls.append(url1)
urls.append(url2)
print(urls)

#importer les codes html des pages regroupant l'ensemble des avis de radiothérapie
all_soup=[]

for url in urls:
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    all_soup.append(soup)

print(all_soup)

#importer les urls des sous-pages regroupant l'ensemble des avis de radiothérapie
urls3= []

for i in all_soup : 
    for h in i.find_all("div", {"class": "cours-info"}):
        a = h.find('a')
        urls3.append(a.attrs['href'])
    
print(urls3)

#importer les informations (titre, date, loc , descri , grade) des sous-pages regroupant l'ensemble des avis de radiothérapie
all_soup2=[]

for i in urls3 : 
    resp = requests.get(i)
    soup = BeautifulSoup(resp.text, 'lxml')
    all_soup2.append(soup)

print(all_soup2[2])   

#liste de titres, prè-requis, objectifs
list_titre=[]
list_prerequis=[]
list_objectif=[]

#extraction des titres, prè-requis, objectifs
for i in all_soup2 :
    titre = i.find("div", {"id": "cours-cover-title"}).text
    prerequis = i.find("section", {"class": "cours-section cours-prerequis"}).text
    obj = i.find("section", {"id": "cours-objectif"}).text
    
    list_titre.append(titre)
    list_prerequis.append(prerequis)
    list_objectif.append(obj)


df = pd.DataFrame({"Titre": list_titre, "Prerequis": list_prerequis, "Objectif": list_objectif})
df.to_excel(r'df.xlsx')
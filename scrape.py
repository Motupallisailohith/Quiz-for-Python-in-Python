#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd

#%%
url = "https://www.sanfoundry.com/python-mcqs-basic-operators/"
r = requests.get(url)



#%%

soup = BeautifulSoup(r.content, 'html5lib')

#%%
queswithops = soup.find_all("p")
for i in range(3):
    queswithops.pop()

del queswithops[0]

#%%
final = queswithops[2].getText().replace("View Answer", "").split("\n")
final.pop()
for i in range(0, len(final)):
    final[i] = final[i][3:]

print(final)



#%%

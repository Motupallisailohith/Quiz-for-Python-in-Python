# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pickle

# %%
url = "https://www.cppbuzz.com/python/python-objective-questions"
r = requests.get(url)


# %%

soup = BeautifulSoup(r.content, 'html5lib')

# %%
queswithops = soup.find_all("p")
for i in range(3):
    queswithops.pop()

del queswithops[0]

answers = soup.find_all("div", {"class": "collapseomatic_content"})


# %%
questionss = []
for i in range(0, 10):
    if i >= 6:
        print("did nothing!")
    else:
        switcher = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        answer = switcher.get(answers[i].getText()[8])
        final = queswithops[i].getText().replace("View Answer", "").split("\n")
        final.pop()
        for i in range(0, len(final)):
            final[i] = final[i][3:]
        que = {"question": final[0], "options": (
            final[1], final[2], final[3], final[4]), "answer": answer}
        questionss.append(que)


# %%
db_write = open("Mixed Type.pickle", "wb")
pickle.dump(questionss, db_write)
db_write.close()
# %%
questionss= []
a = soup.findAll('div',{"class":"left_box"})
x = soup.findAll('div', {"class": "TenpxPaddingLeft"})

for i in range(0,46):
    switcher = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    que= {}
    que['question'] = a[i].findAll('textarea')[0].getText()
    z = x[0].getText().replace(" ForumBeginner other[Posted by: Admin |  Chicago, USA]", "").replace("(A) ","").replace("(B)","~~").replace("(C)","~~").replace("(D)","~~").replace("Ans:","~~").replace(" ", "")
    y = z.split("~~")
    que['options'] = (y[0],y[1],y[2],y[3])
    que['answer'] = switcher.get(y[4])
    questionss.append(que)

# %%
questionss[0]

# %%

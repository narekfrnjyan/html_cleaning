import requests
from bs4 import BeautifulSoup
import sys 
import unicodedata
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
req = requests.get("https://httpstatuses.com/")
document = req.content.decode("utf-8")
soup = BeautifulSoup(document,"html.parser")
text_list=[text.text for text in soup.find_all(['p','title','li','h1','h2','a']) ]
text_list

tbl=dict.fromkeys(i for i in range(sys.maxunicode)
                 if unicodedata.category(chr(i)).startswith('P'))
def remove_punct(text):
    return text.translate(tbl)
string=remove_punct(soup.get_text())

words=word_tokenize(string.lower())


stopwords=stopwords.words("english")
tokenized=[i for i in words if i not in stopwords]
print(words)
print(string)
print(tokenized)
porter=PorterStemmer()
m=[porter.stem(word) for word in tokenized]
s=set(m)
cleaned_lsit=list(s)
print(cleaned_lsit)



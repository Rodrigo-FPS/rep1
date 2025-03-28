import requests
from bs4 import BeautifulSoup, Comment
import re

url = "http://127.0.0.1:8000/victima.html"   
response = requests.get(url)  
soup = BeautifulSoup(response.text, "html.parser")

links =[a["href"] for a in soup.find_all("a", href=True)]  
print("Enlaces:")
print(links)

coments = [comment for comment in soup.find_all(string=lambda text: isinstance(text, Comment) )]
print("\nComentarios:")
print(coments) 
correo_re = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+'  
correos = re.findall(correo_re, response.text )
print("\nCorreos:")
print(correos)  



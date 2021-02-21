from bs4 import BeautifulSoup
from FunctionPL import pluemfunction as pl

pl.friend_creat()

soup = BeautifulSoup(data,'html.parser')
find_word = soup.find_all('a',)


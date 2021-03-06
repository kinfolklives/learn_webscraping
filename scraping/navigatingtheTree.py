from bs4 import BeautifulSoup
import requests

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')

# res = requests.get('https://movie.naver.com/movie/point/af/list.nhn')
# soup = BeautifulSoup(res.content, features="lxml")

#Going down - .children
bodychildren = soup.body.children
print(type(bodychildren), len(list(bodychildren)))

body_tag = soup.body
for child in body_tag.children:   #child 사용자 정의 변수 
    print(type(child), repr(child))  # returns a printable representation; debug console 에서 repr(child)

# Going up - .parent and .parents
title_tag = soup.title
print(title_tag.parent, title_tag.string.parent)
link = soup.a
print(type(link.parents), len(list(link.parents)))

for parent in link.parents:  # parent 사용자 정의 변수 
    print(type(parent.name), parent.name)



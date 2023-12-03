import requests
from bs4 import BeautifulSoup

종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']
리스트 = []

def 현재가(구멍):
    데이터 = requests.get(f'https://finance.naver.com/item/sise.naver?code={구멍}')
    soup = BeautifulSoup(데이터.content, 'html.parser')
    nowsoup = soup.find_all('strong', id="_nowVal")[0].text
    # print(soup.find_all('span', class_="tah")[5].text )
    # return soup.find_all('strong', id="_nowVal")[0].text
    리스트.append(soup.find_all('strong', id="_nowVal")[0].text)

현재가('005930')
print(리스트)

# for i in 종목들:
#     현재가(i)
#     f = open('a.txt', 'w')
#     f.write(리스트[i])
#     f.close()

# print('a.txt')


# print(soup.select('.f_up em')[1].text)
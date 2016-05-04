# encode: utf8
import requests
import bs4

#교보문고 베스트 셀러 목록 입수
response = requests.get( 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf' )
soup = bs4.BeautifulSoup(response.text)
book_page_urls = [a.attrs.get('href') for a in soup.select('div.title a[href^="http://www.kyobobook.co.kr/product/detailViewKor.laf"]')]

for book_page_url in book_page_urls:
    response = requests.get( book_page_url )
    soup = bs4.BeautifulSoup(response.text)

    title = soup.select( 'h1.title strong' )[0].get_text().strip()
    author = soup.select( 'span.name  a' )[0].get_text()
    print (title + '/' + author)




import requests
from bs4 import BeautifulSoup

# 웹사이트 URL 리스트
urls = [
    "https://nhuf.molit.go.kr/FP/FP05/FP0502/FP05020301.jsp",
    "https://obank.kbstar.com/quics?page=C103544#loading",
    "https://www.kakaobank.com/products/leaseLoan",
    "https://www.lh.or.kr/contents/cont.do?sCode=user&mId=234&mPid=231"
]

# 각 URL에 대해 데이터를 크롤링하는 함수
def crawl_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    else:
        print(f"Error {response.status_code}: Unable to fetch data from {url}")
        return None

def get_data_list():
    data_list = []
    for url in urls:
        data = crawl_data(url)
        if data:
            data_list.append(data)
    return data_list

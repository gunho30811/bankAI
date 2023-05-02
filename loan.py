from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

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
        soup = BeautifulSoup(response.content, "html.parser")
        # 원하는 데이터를 찾아서 반환합니다.
        # 예를 들어, 페이지의 모든 텍스트를 가져오고 싶다면 아래와 같이 작성할 수 있습니다.
        return soup.get_text()
    else:
        print(f"Error {response.status_code}: Unable to fetch data from {url}")
        return None

# # 각 URL에서 데이터를 가져옵니다.
# for url in urls:
#     data = crawl_data(url)
#     if data:
#         # 데이터를 처리하거나 저장합니다.
#         print(data)

# # 결과 리스트를 순서대로 출력합니다.
# for index, result in enumerate(results):
#     print(f"URL {index + 1}:")
#     print(result)
#     print("=" * 80)

@app.route('/')
def index():
    results = []
    for url in urls:
        data = crawl_data(url)
        if data:
            results.append(data)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)    
import requests
import json
import pandas as pd

# 헤더를 설정한다.
headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2ODMxNzY1NjMsImV4cCI6MTY4MzE4NzM2M30.1mj111p-0LdlHPnp2Yy447ivGKrH-yED-EcP2zUhtnc",
    "Host": "new.land.naver.com",
    "Referer": "https://new.land.naver.com/complexes/139296?ms=37.4984278,127.0352626,16&a=OPST:OBYG:PRE&b=B1&e=RETAIL&f=12000&g=30000",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

# articleNo를 뽑아온다.
def get_articles(page):
    search_url = "https://new.land.naver.com/api/articles/complex/139296?realEstateType=OPST%3AOBYG%3APRE&tradeType=B1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=12000&priceMax=30000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={}&complexNo=139296&buildingNos=&areaNos=&type=list&order=rank".format(page)
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        return response.json()["articleList"]
    else:
        print("Failed to fetch data:", response.status_code)
        return []

page = 1
all_article_nos = []

while True:
    articles = get_articles(page)
    if not articles:
        break

    for article in articles:
        all_article_nos.append(article["articleNo"])
    
    page += 1

print("Found articleNos:", all_article_nos)
print(len(all_article_nos))

urls = [f"https://new.land.naver.com/api/articles/{article_no}?complexNo=" for article_no in all_article_nos]

for url in urls:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # 공인중개사 담당자
        print(data['articleRealtor']['representativeName'])
        # 공인중개사 위치
        print(data['articleRealtor']['address'])
        # 중개인 핸드폰 번호
        print(data['articleRealtor']['cellPhoneNo'])
        # 전세 금액
        print(data['articleAddition']['dealOrWarrantPrc'])
        # 오피스텔 이름
        print(data['articleDetail']['articleName'])
        # 오피스텔 위치
        print(data['articleDetail']['exposureAddress'])
        # 집 종류
        print(data['articleAddition']['articleRealEstateTypeName'])        
        #핵심 키워드
        print(data['articleAddition']['tagList'])
        #집 총 층수
        print(data['articleAddition']['floorInfo'])
        #현재 이 집 관리비
        print('관리비 정보: ' + str(data['articleDetail']['monthlyManagementCost']))
        #현재 이 집 융자
        print('융자 정보: ' + str(data['articlePrice']['financePrice']))
        #매물 설명
        print(data['articleDetail']['detailDescription'])    
        # print(data)
    else:
        print("Failed to fetch data:", response.status_code)





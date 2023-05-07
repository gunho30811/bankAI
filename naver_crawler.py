import requests
import json
import pandas as pd

def get_sido_info():
    down_url = 'https://new.land.naver.com/api/regions/list?cortarNo='
    r = requests.get(down_url,data={"sameAddressGroup":"false"},headers={
        "Accept-Encoding": "gzip",
        "Host": "new.land.naver.com",
        "Referer": "https://new.land.naver.com/complexes/102378?ms=37.5018495,127.0438028,16&a=APT&b=A1&e=RETAIL",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    })
    r.encoding = "utf-8-sig"
    temp=json.loads(r.text)
    city_list = [(city["cortarNo"], city["cortarName"]) for city in temp["regionList"]]
    return city_list
def get_gungu_info(sido_code):
    down_url = 'https://new.land.naver.com/api/regions/list?cortarNo='+sido_code
    r = requests.get(down_url,data={"sameAddressGroup":"false"},headers={
        "Accept-Encoding": "gzip",
        "Host": "new.land.naver.com",
        "Referer": "https://new.land.naver.com/complexes/102378?ms=37.5018495,127.0438028,16&a=APT&b=A1&e=RETAIL",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    })
    r.encoding = "utf-8-sig"
    temp=json.loads(r.text)
    gungu_list = [(region['cortarNo'], region['cortarName']) for region in temp['regionList']]
    return gungu_list
def get_dong_info(gungu_code):
    down_url = 'https://new.land.naver.com/api/regions/list?cortarNo='+gungu_code
    r = requests.get(down_url,data={"sameAddressGroup":"false"},headers={
        "Accept-Encoding": "gzip",
        "Host": "new.land.naver.com",
        "Referer": "https://new.land.naver.com/complexes/102378?ms=37.5018495,127.0438028,16&a=APT&b=A1&e=RETAIL",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    })
    r.encoding = "utf-8-sig"
    temp=json.loads(r.text)
    dong_list = [(region['cortarNo'], region['cortarName']) for region in temp['regionList']]
    return dong_list
def get_apt_list(dong_code):
    down_url = 'https://new.land.naver.com/api/regions/complexes?cortarNo='+dong_code+'&realEstateType=APT&order='
    r = requests.get(down_url,data={"sameAddressGroup":"false"},headers={
        "Accept-Encoding": "gzip",
        "Host": "new.land.naver.com",
        "Referer": "https://new.land.naver.com/complexes/102378?ms=37.5018495,127.0438028,16&a=APT&b=A1&e=RETAIL",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    })
    r.encoding = "utf-8-sig"
    temp=json.loads(r.text)
    try:
        temp=list(pd.DataFrame(temp['complexList'])["complexNo"])
    except:
        temp=[]
    return temp

def get_officetel_list(dong_code):
    down_url = f'https://new.land.naver.com/api/regions/complexes?cortarNo={dong_code}&realEstateType=OPST&order='
    r = requests.get(down_url, headers={
    "Accept-Encoding": "gzip",
    "Host": "new.land.naver.com",
    "Referer": "https://new.land.naver.com/complexes/102378?ms=37.5018495,127.0438028,16&a=APT&b=A1&e=RETAIL",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    })
    r.encoding = "utf-8-sig"
    temp = json.loads(r.text)
    result = []
    try:
        complex_df = pd.DataFrame(temp['complexList'])
        for index, row in complex_df.iterrows():
            result.append((row['complexNo'], row['complexName']))
    except:
        result = []
    return result

def get_officetel_info(complex_no):
    url = f"https://new.land.naver.com/api/complexes/overview/{complex_no}?complexNo={complex_no}&isClickedMarker=true"
    headers = {
        "Accept-Encoding": "gzip",
        "Host": "new.land.naver.com",
        "Referer": "https://new.land.naver.com/complexes/102378?ms=37.5018495,127.0438028,16&a=APT&b=A1&e=RETAIL",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8-sig"
    data = json.loads(response.text)
    
    return data["maxPriceByLetter"]

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
def get_articles(complexNo, page, min_price, max_price):
    # search_url 수정
    search_url = "https://new.land.naver.com/api/articles/complex/{0}?realEstateType=OPST&tradeType=B1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin={1}&priceMax={2}&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={3}&buildingNos=&areaNos=&type=list&order=rank".format(complexNo, min_price, max_price, page)
    
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        try:
            return response.json()["articleList"]
        except json.decoder.JSONDecodeError:
            print(f"JSONDecodeError occurred for complexNo: {complexNo}, page: {page}, min_price: {min_price}, max_price: {max_price}")
            return []
    else:
        print("Failed to fetch data:", response.status_code)
        return []

def get_all_articles(dong_code, page, min_price, max_price):
    complex_nos = get_officetel_list(dong_code)
    all_articles = []
    for complexNo, _ in complex_nos:
        articles = get_articles(complexNo, page, min_price, max_price)
        all_articles.extend(articles)

    return all_articles

def search_properties(complexNo, min_price, max_price):
    page = 1
    all_article_nos = []

    while True:
        articles = get_articles(complexNo, page, min_price, max_price)
        if not articles:
            break

        for article in articles:
            all_article_nos.append(article["articleNo"])

        page += 1

    properties = []
    urls = [f"https://new.land.naver.com/api/articles/{article_no}?complexNo=" for article_no in all_article_nos]

    for url in urls:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            property_info = {
                "representativeName": data['articleRealtor']['representativeName'],
                "address": data['articleRealtor']['address'],
                "cellPhoneNo": data['articleRealtor']['cellPhoneNo'],
                "dealOrWarrantPrc": data['articleAddition']['dealOrWarrantPrc'],
                "articleName": data['articleDetail']['articleName'],
                "exposureAddress": data['articleDetail']['exposureAddress'],
                "articleRealEstateTypeName": data['articleAddition']['articleRealEstateTypeName'],
                "tagList": data['articleAddition']['tagList'],
                "floorInfo": data['articleAddition']['floorInfo'],
                "monthlyManagementCost": data['articleDetail']['monthlyManagementCost'],
                "financePrice": data['articlePrice']['financePrice']
            }
            properties.append(property_info)
        else:
            print("Failed to fetch data:", response.status_code)

    return properties

complexNo = "17833"  # 임시 동 코드
dong_code = "1168010100"
page = 1
min_price = 0
max_price = 10000
articles = get_all_articles(dong_code, page, min_price, max_price)
print(articles)
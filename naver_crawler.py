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
    temp=list(pd.DataFrame(temp["regionList"])["cortarNo"])
    return temp
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
    temp=list(pd.DataFrame(temp['regionList'])["cortarNo"])
    return temp
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
    temp=list(pd.DataFrame(temp['regionList'])["cortarNo"])
    return temp
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

# 위에서 제공한 함수들을 사용하여 서울특별시, 강남구, 역삼동의 코드를 얻습니다.
sido_codes = get_sido_info()
print("sido codes: " + str(sido_codes[0]))

gungu_codes = get_gungu_info(sido_codes[0])  # 서울특별시의 코드
print("gungu codes: " + str(gungu_codes[0]))

dong_codes = get_dong_info(gungu_codes[0])   # 강남구의 코드
print("dong_code: " + str(dong_codes[9]))
# 역삼동 코드를 찾습니다.

# 역삼동에 있는 오피스텔 정보를 가져옵니다.
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

officetel_list = get_officetel_list(dong_codes[9])
print("역삼동 오피스텔 목록:", officetel_list)

complex_no = 105174  # 유니온 오피스텔의 complexNo
max_price_by_letter = get_officetel_info(complex_no)

print("Max price by letter:", max_price_by_letter)

complex_no = 9461  # 목화밀리트 오피스텔의 complex_no

url = "https://new.land.naver.com/api/articles/2317807256?complexNo="
url1 = "https://new.land.naver.com/api/articles/2318945001?complexNo="
url2 = "https://new.land.naver.com/api/articles/2317394523?complexNo="

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

response = requests.get(url1, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to fetch data:", response.status_code)

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

def get_article_data(article_no):
    url = f"https://new.land.naver.com/api/articles/{article_no}?complexNo="
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        lease_price = data.get("dealOrWarrantPrc", "Unknown")
        realtor_name = data.get("realtorName", "Unknown")
        
        return {
            "lease_price": lease_price,
            "realtor_name": realtor_name
        }
    else:
        print("Failed to fetch data for articleNo:", article_no)
        return None

articles_data = []
    
for article_no in all_article_nos:
    article_data = get_article_data(article_no)
    if article_data:
        articles_data.append(article_data)

for article_data in articles_data:
    print("Lease price:", article_data["dealOrWarrantPrc"])
    print("Realtor name:", article_data["realtorName"])
    print("\n")    
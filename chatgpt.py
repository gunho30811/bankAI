import openai

openai.api_key= "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"

def ask_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

def property_summary(property):
    prompt = f"""
다음과 같은 부동산 정보가 있습니다:
대표자 이름: {property['representativeName']}
주소: {property['address']}
휴대폰 번호: {property['cellPhoneNo']}
거래가격 또는 전세가격: {property['dealOrWarrantPrc']}
매물 이름: {property['articleName']}
노출 주소: {property['exposureAddress']}
매물 부동산 유형 이름: {property['articleRealEstateTypeName']}
태그: {','.join(property['tagList'])}
층 정보: {property['floorInfo']}
월 관리비: {property['monthlyManagementCost']}
금융 가격: {property['financePrice']}

이 부동산 정보를 요약해 주세요.
"""

    summary = ask_chatgpt(prompt)
    return summary
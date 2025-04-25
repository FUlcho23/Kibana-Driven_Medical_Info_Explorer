'''
Created on 2025. 4. 25.

@author: user
'''
import pandas as pd #pip install pandas
import re

df = pd.read_csv("C:/logstash-7.10.1-windows-x86_64/logstash-7.10.1/config/welfare.csv")

df = df.rename(columns={"시설기본주소": "주소"})

def extract_location_parts(address):
    if pd.isna(address):
        return None, None, None

    parts = address.split()
    시도 = None
    시군구 = None
    읍면동 = None

    # 시도 추출
    for 시도_후보 in ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", 
                   "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]:
        if 시도_후보 in parts[0]:
            시도 = 시도_후보
            break

    # 시군구 추출
    for p in parts[1:]:
        if p.endswith("시") or p.endswith("군") or p.endswith("구"):
            시군구 = p
            break

    # 읍면동 추출 (도로명 주소면 없음)
    for p in parts[2:]:
        if p.endswith("읍") or p.endswith("면") or p.endswith("동"):
            읍면동 = p
            break

    return 시도, 시군구, 읍면동

df[["시도코드명", "시군구코드명", "읍면동"]] = df["주소"].apply(
    lambda x: pd.Series(extract_location_parts(x))
)

df.head()

df.to_csv("C:/logstash-7.10.1-windows-x86_64/logstash-7.10.1/config/welfare_updated.csv", index=False)

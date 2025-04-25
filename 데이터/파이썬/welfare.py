'''
Created on 2025. 4. 22.

@author: user
'''
import time
import urllib.request
from xml.etree.ElementTree import fromstring, ElementTree
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch()

docs = []

for i in range(1, 183):  # 최대 20페이지
    page = i
    num = 1000

    url = f'http://apis.data.go.kr/B554287/DisabledPersonConvenientFacility/getDisConvFaclList?serviceKey=T1VmDHvNJ1RcboNmELV2VKQSddxhUXohWLri8427OsgABkInPOb9Pa4QFomqigzN7CWD2wUCakAFEIWTCd0jPQ%3D%3D&pageNo={page}&numOfRows={num}'  # ← 실제 API 주소 입력

    response = urllib.request.urlopen(url)
    xml_str = response.read().decode('UTF-8')

    tree = ElementTree(fromstring(xml_str))
    root = tree.getroot()

    for row in root.iter("servList"):  # 또는 "row"
        salStaDivCd = row.findtext('salStaDivCd')

        if salStaDivCd != "Y":
            continue  # 영업 중(Y)만 저장
                

        faclNm = row.findtext('faclNm') or ""
        faclTyCd = row.findtext('faclTyCd') or ""
        lcMnad = row.findtext('lcMnad') or ""
        lat = float(row.findtext('faclLat') or 0.0)
        lon = float(row.findtext('faclLng') or 0.0)
        wfcltDivCd = row.findtext('wfcltDivCd') or ""
        wfcltId = row.findtext('wfcltId') or ""

        doc = {
            "_index": "welfare",
            "_source": {
                "시설명": faclNm,
                "시설유형": faclTyCd,
                "시설기본주소": lcMnad,
                "location": {
                    "lat": lat,
                    "lon": lon
                },
                "복지로관리시설구분코드": wfcltDivCd,
                "시설ID": wfcltId,
                "영업상태구분코드": salStaDivCd
            }
        }

        docs.append(doc)
    print(f"Processed {page} ~ {num}")
    time.sleep(0.2)  # 0.2초 딜레이 넣기 → 너무 빠른 호출 방지

# 한 번에 넣기
res = helpers.bulk(es, docs)
print(res)
print("현재까지 수집된 doc 수:", len(docs))
print("✅ 데이터 저장 완료! 총 건수:", len(docs))


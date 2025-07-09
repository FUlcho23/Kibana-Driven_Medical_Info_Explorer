## 1. 프로젝트명
장애인 복지시설 주변의 의료접근성 분석

## 2. 프로젝트 설명
- ### **개발배경 및 기획 의도**
  장애인 복지 시설을 이용하는 사용자들은 대부분 병원에 갈 일이 많습니다. 그렇다 보니 급한 일이 생기는 경우, 갈 수 있는 병원이나 약국을 더욱 쉽게 찾을 수 있다면 좋지 않을까 싶어 해당 프로젝트를 진행하게 되었습니다.
- ### **기대 효과**
    - 개인
        - 복지시설 근처 병원이나 약국의 위치 및 운영시간,
          주말 진료 여부, 응급실 운영 여부 파악 가능
        - 의료 접근성 향상
          
    - 기업/민간 기관
        - 복지시설 운영 기업이나 돌봄 서비스 업체에서
          시설 이용자에게 맞춤 의료기관 정보 제공 가능
        - 새로운 복지시설 설립을 위한 의료 인프라 분석 도구로 활용

    - 공공기관/지자체
        - 장애인 복지시설 주변 인프라 분석 가능
        - 의료 인프라 취약 지역 파악
        - 새로운 복지시설 설립을 위한 근거 자료로 활용
- ### 사용 기술 및 개발 환경
  개발환경 - Windows 11 (64bit)<br/>
  데이터 수집 - 공공데이터포털(https://www.data.go.kr/)<br/>
  데이터 정제 - Python, Logstash<br/>
  데이터 저장/검색 - Elasticsearch<br/>
  시각화 - Kibana<br/>

## 3. 흐름도
![2](https://github.com/user-attachments/assets/bb8bfcce-a345-43f8-9d01-4e2adaf56de8)

## 4. 페이지 설계
![10](https://github.com/user-attachments/assets/0d5fcf5d-bf2a-4b9c-9674-b913eec93a8e)
![11](https://github.com/user-attachments/assets/6c90494a-f7e7-4434-ba09-a490f46da973)
<img width="991" alt="image" src="https://github.com/user-attachments/assets/79d9bedd-b2b0-4adb-a3ae-62167931b60e" />   

## 5. 실 사용 화면
https://github.com/user-attachments/assets/0e6e5263-a453-4acf-b0f7-4c01203c64a5

## 6. 팀원 및 참고자료
- ### **팀원**
    구선민(GitGu25) - 팀장/주제선정/자료수집/구현 <br/>
    변초은(FUlcho23) - 팀원/PPT제작/자료수집/데이터정제 <br/>
    정재은(rltjj) - 팀원/데이터정제/구현 <br/>

- ### **참고자료**
    [공공빅데이터-한국사회보장정보원_장애인편의시설 현황] <br/>
    https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15092317 <br/>
    [공공빅데이터-건강보험심사평가원_전국 병의원 및 약국 현황] <br/>
    https://www.data.go.kr/tcs/dss/selectFileDataDetailView.do?publicDataPk=15051059

## 7. 발표에 사용한 PPT
(Kibana-Driven_Medical_Info_Explorer) <br/>
[빅데이터검색엔진_복지시설의료접근성_구선민,변초은,정재은.pdf](https://github.com/user-attachments/files/21142143/_._.pdf)

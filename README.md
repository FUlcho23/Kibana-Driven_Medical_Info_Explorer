# 장애인 복지시설 주변의 의료접근성 분석
장애인 복지 시설을 이용하는 사용자들은 대부분 병원에 갈 일이 많습니다. 그렇다 보니 급한 일이 생기는 경우, 갈 수 있는 병원이나 약국을 더욱 쉽게 찾을 수 있다면 좋지 않을까 싶어 해당 프로젝트를 진행하게 되었습니다.

## 프로젝트 설명
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

## 팀 구성 및 역할
  - 구선민(팀장) - 주제선정/자료수집/구현
  - 변초은(팀원) - PPT제작/자료수집/데이터정제
  - 정재은(팀원) - 데이터정제/구현

- ### **페이지 소개**
    - **병원 대시보드**
      - 대시보드 이동
      - 맵(병원, 약국, 복지)
      - 병원 리스트 테이블
      - 도시별 병원 수
      - 종별코드명 파이 차트
      
    - **약국 대시보드**
      - 대시보드 이동
      - 맵(병원, 약국, 복지)
      - 약국 테이블
      - 도시별 약국 수
 
    - **복지시설 대시보드**
      - 대시보드 이동
      - 맵(병원, 약국, 복지)
      - 맵(복지시설 상세) - 한국장애인고용공단 및 지사, 보건소, 의료시설, 교육시설, 복지시설 등
      - 장애인편의시설 테이블
      - 도시별 복지시설 수
      - 복지시설유형 파이 차트
   
## 프로젝트 흐름도
![2](https://github.com/user-attachments/assets/bb8bfcce-a345-43f8-9d01-4e2adaf56de8))

## 사용 기술 및 개발 환경
개발환경 - Windows 11 (64bit)<br/>
데이터 수집 - 공공데이터포털(https://www.data.go.kr/)<br/>
데이터 정제 - Python, Logstash<br/>
데이터 저장/검색 - Elasticsearch<br/>
시각화 - Kibana<br/>

# 발표에 사용한 PPT (Kibana-Driven_Medical_Info_Explorer)
![Picture (1)](https://github.com/user-attachments/assets/f89e0d4c-a8b6-4c46-8a30-bddde12bc143)
![Picture (3)](https://github.com/user-attachments/assets/95daa37e-d690-402b-882e-a21e10f3c866)
![화면 캡처 2025-06-13 143403](https://github.com/user-attachments/assets/1d3095b7-9237-45f4-a906-1448ac837124)
![2](https://github.com/user-attachments/assets/bb8bfcce-a345-43f8-9d01-4e2adaf56de8)
![3](https://github.com/user-attachments/assets/8cd812cd-6d0e-4943-b8ab-b76f929ad350)
![4](https://github.com/user-attachments/assets/92636ca6-2742-499c-916e-3553dae0ce37)
![5](https://github.com/user-attachments/assets/08b9767a-f455-49d8-9059-55a7ac76e447)
![6](https://github.com/user-attachments/assets/d6ff242b-fbe6-4415-9f99-27be372dc031)
![7](https://github.com/user-attachments/assets/6c05774b-0ca5-4c37-af48-456b52c58bb5)
![8](https://github.com/user-attachments/assets/6f0435e7-d174-481d-843c-87e90ce8d813)
![9](https://github.com/user-attachments/assets/c38edd85-d5fa-4391-a8fe-40e58d880fd8)
![10](https://github.com/user-attachments/assets/0d5fcf5d-bf2a-4b9c-9674-b913eec93a8e)
![11](https://github.com/user-attachments/assets/6c90494a-f7e7-4434-ba09-a490f46da973)
<img width="991" alt="image" src="https://github.com/user-attachments/assets/79d9bedd-b2b0-4adb-a3ae-62167931b60e" />
![13](https://github.com/user-attachments/assets/1713df86-9553-4bbd-ad43-4ae4633de23e)
![14](https://github.com/user-attachments/assets/6a211280-c8b4-402a-b3c7-c9c2545ec6fe)

아래는 실 사용 화면입니다.

https://github.com/user-attachments/assets/0e6e5263-a453-4acf-b0f7-4c01203c64a5

